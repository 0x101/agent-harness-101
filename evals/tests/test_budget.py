"""Tests for the spend guard, using a scripted fake client (no API calls)."""
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import budget  # noqa: E402
from budget import BudgetClient, BudgetExceeded, Ledger  # noqa: E402

MODEL = "claude-haiku-4-5-20251001"


class FakeInner:
    """Stands in for anthropic.Anthropic(): every call reports the same usage."""

    def __init__(self, input_tokens=1000, output_tokens=100):
        self.calls = 0
        outer = self

        class Messages:
            def create(self, **kw):
                outer.calls += 1
                return SimpleNamespace(content=[], usage=SimpleNamespace(
                    input_tokens=input_tokens, output_tokens=output_tokens))

            def count_tokens(self, **kw):
                return 7

            def stream(self, **kw):
                raise AssertionError("must not be reached")

        self.messages = Messages()


def call(client, text="hi", max_tokens=4096):
    return client.messages.create(model=MODEL, max_tokens=max_tokens, system="s", tools=[],
                                  messages=[{"role": "user", "content": text}])


class BudgetTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = Path(self.dir.name) / "spend.json"
        for k in ("HARNESS_PRICE_IN", "HARNESS_PRICE_OUT", "HARNESS_CONTEXT_TOKENS"):
            os.environ.pop(k, None)

    def tearDown(self):
        self.dir.cleanup()

    def test_adds_real_cost(self):
        client = BudgetClient(FakeInner(1000, 100), Ledger(self.path, 1.0))
        call(client)
        # 1000 input at $1 per million plus 100 output at $5 per million
        self.assertAlmostEqual(client.ledger.spent, 0.0015)

    def test_refuses_before_the_cap_can_be_passed(self):
        inner = FakeInner()
        client = BudgetClient(inner, Ledger(self.path, 0.025))
        # Each call reserves about $0.0225 (output plus the fixed allowance) and then costs $0.0015.
        # After two calls $0.003 is spent, so a third could reach $0.0255 and is refused unmade.
        call(client)
        call(client)
        with self.assertRaises(BudgetExceeded):
            call(client)
        self.assertEqual(inner.calls, 2)
        self.assertLessEqual(client.ledger.spent, 0.025)

    def test_reserve_grows_with_the_request_and_stops_at_the_context_window(self):
        small = budget.worst_case_usd({"model": MODEL, "max_tokens": 0, "messages": "x" * 1000})
        huge = budget.worst_case_usd({"model": MODEL, "max_tokens": 0, "messages": "x" * 5_000_000})
        self.assertLess(small, 0.004)
        self.assertAlmostEqual(huge, 0.20)

    def test_ledger_is_shared_across_runs(self):
        call(BudgetClient(FakeInner(), Ledger(self.path, 1.0)))
        again = Ledger(self.path, 1.0)
        self.assertAlmostEqual(again.spent, 0.0015)
        self.assertEqual(again.calls, 1)

    def test_unknown_model_needs_a_price(self):
        with self.assertRaises(ValueError):
            budget.price_for("some-new-model")
        os.environ["HARNESS_PRICE_IN"], os.environ["HARNESS_PRICE_OUT"] = "0.1", "0.5"
        self.assertEqual(budget.price_for("some-new-model")[:2], (0.1, 0.5))

    def test_cache_tokens_are_counted(self):
        usage = SimpleNamespace(input_tokens=0, output_tokens=0,
                                cache_creation_input_tokens=1_000_000, cache_read_input_tokens=1_000_000)
        self.assertAlmostEqual(budget.actual_usd(MODEL, usage), 2.0 + 0.1)

    def test_other_call_paths_are_refused(self):
        client = BudgetClient(FakeInner(), Ledger(self.path, 1.0))
        self.assertEqual(client.messages.count_tokens(), 7)
        with self.assertRaises(NotImplementedError):
            client.messages.stream()
        with self.assertRaises(NotImplementedError):
            client.messages.create(model=MODEL, max_tokens=1, messages=[], stream=True)


if __name__ == "__main__":
    unittest.main()
