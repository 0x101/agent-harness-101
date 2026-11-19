"""Spend guard for eval runs.

`python evals/run.py --budget-usd 30` wraps the model client so that no call is made once the
ledger could pass the cap. The guard is conservative by design:

  - Before each call it reserves the worst case for that call: every byte of the request counted
    as one input token plus a fixed allowance (capped at the model's context window), plus
    `max_tokens` of output.
    If the ledger plus that reserve would pass the cap, it raises BudgetExceeded and the run stops.
  - After each call it adds the real cost from the response's usage.
  - The ledger is a JSON file, saved after every call, so separate runs share one cap.
    Delete the file (or point --budget-ledger elsewhere) to start a new budget.

Only `client.messages.create` is covered. Other ways of calling the model (`stream`, batches)
are refused while a budget is active, so nothing can spend outside the guard.
"""
import json
import os
from pathlib import Path

# USD per million tokens (input, output) and the context window in tokens.
PRICES = {
    "claude-haiku-4-5-20251001": (1.00, 5.00, 200_000),
}
CACHE_WRITE = 2.0   # upper bound: a 1-hour cache write costs 2x input, a 5-minute one 1.25x
CACHE_READ = 0.1
UNKNOWN_CONTEXT = 1_000_000
OVERHEAD_TOKENS = 2_000  # tokens the API adds that are not in the request body, such as the tool-use preamble


class BudgetExceeded(Exception):
    """Raised before a call that could take the ledger past its cap."""


def price_for(model):
    """Return (input, output, context) for a model. Env vars override the table."""
    p_in, p_out = os.environ.get("HARNESS_PRICE_IN"), os.environ.get("HARNESS_PRICE_OUT")
    if p_in and p_out:
        ctx = int(os.environ.get("HARNESS_CONTEXT_TOKENS", PRICES.get(model, (0, 0, UNKNOWN_CONTEXT))[2]))
        return float(p_in), float(p_out), ctx
    if model in PRICES:
        return PRICES[model]
    raise ValueError(
        f"no price known for model {model!r}. Set HARNESS_PRICE_IN and HARNESS_PRICE_OUT "
        "(USD per million tokens) to run it under a budget.")


class Ledger:
    def __init__(self, path, cap_usd):
        self.path = Path(path)
        self.cap = float(cap_usd)
        self.spent = 0.0
        self.calls = 0
        if self.path.exists():
            data = json.loads(self.path.read_text())
            self.spent = float(data.get("spent_usd", 0.0))
            self.calls = int(data.get("calls", 0))

    def add(self, usd):
        self.spent += usd
        self.calls += 1
        self.save()

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(self.path.suffix + ".tmp")
        tmp.write_text(json.dumps(
            {"cap_usd": self.cap, "spent_usd": round(self.spent, 6), "calls": self.calls}, indent=2) + "\n")
        os.replace(tmp, self.path)


def _plain(obj):
    return obj.model_dump() if hasattr(obj, "model_dump") else str(obj)


def worst_case_usd(kw):
    p_in, p_out, ctx = price_for(kw.get("model"))
    nbytes = len(json.dumps([kw.get("system"), kw.get("tools"), kw.get("messages")], default=_plain).encode())
    return (min(ctx, nbytes + OVERHEAD_TOKENS) * p_in + int(kw.get("max_tokens", 0)) * p_out) / 1e6


def actual_usd(model, usage):
    p_in, p_out, _ = price_for(model)
    get = lambda name: getattr(usage, name, 0) or 0  # noqa: E731
    tokens_in = (get("input_tokens") + CACHE_WRITE * get("cache_creation_input_tokens")
                 + CACHE_READ * get("cache_read_input_tokens"))
    return (tokens_in * p_in + get("output_tokens") * p_out) / 1e6


class _Messages:
    def __init__(self, inner, ledger):
        self._inner = inner
        self._ledger = ledger

    def create(self, **kw):
        if kw.get("stream"):
            raise NotImplementedError("streaming is not covered by the spend guard")
        reserve = worst_case_usd(kw)
        led = self._ledger
        if led.spent + reserve > led.cap:
            raise BudgetExceeded(
                f"spent ${led.spent:.2f} of ${led.cap:.2f}; the next call could cost up to ${reserve:.2f}")
        resp = self._inner.create(**kw)
        led.add(actual_usd(kw.get("model"), resp.usage))
        return resp

    def __getattr__(self, name):
        if name == "count_tokens":  # free, so let it through
            return getattr(self._inner, name)
        raise NotImplementedError(f"messages.{name} is not covered by the spend guard")


class BudgetClient:
    """Drop-in for anthropic.Anthropic() that refuses calls past the ledger's cap."""

    def __init__(self, inner, ledger):
        self.messages = _Messages(inner.messages, ledger)
        self.ledger = ledger
