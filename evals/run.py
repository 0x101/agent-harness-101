#!/usr/bin/env python3
"""Eval runner for Agent Harness 101.

Each task lives in evals/tasks/<name>/ with:
  task.md    the instruction the agent receives
  repo/      the starting files (copied to a fresh temp dir per run)
  hidden/    unittest files the agent never sees, run against the repo afterwards
  solution/  reference files overlaid in --mode oracle, to prove the task is solvable

Modes:
  agent   run harness/agent.py on each task (default)
  oracle  overlay solution/ and check it passes (sanity check for the task itself)
  noop    change nothing and check it fails (sanity check that the task is not already solved)

Examples:
  python evals/run.py --label baseline
  python evals/run.py --tasks 01-pagination,06-needle-in-logs --repeat 3 --label truncation
  python evals/run.py --mode oracle
"""
import argparse
import datetime as dt
import json
import os
import shutil
import statistics
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TASKS = ROOT / "evals" / "tasks"
RESULTS = ROOT / "evals" / "results"
TRAJ = ROOT / "evals" / "trajectories"
sys.path.insert(0, str(ROOT / "harness"))


def check(task_dir, repo):
    env = dict(os.environ, PYTHONPATH=str(repo), PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", str(task_dir / "hidden"), "-p", "test_*.py"],
        cwd=repo, env=env, capture_output=True, text=True, timeout=300)
    return p.returncode == 0, (p.stdout + p.stderr)[-1500:]


def run_one(task_dir, mode, label, rep):
    tmp = Path(tempfile.mkdtemp(prefix=f"hl-{task_dir.name}-"))
    repo = tmp / "repo"
    shutil.copytree(task_dir / "repo", repo)
    t0 = time.time()
    outcome = {"status": mode, "steps": 0, "input_tokens": 0, "output_tokens": 0}
    traj_path = None
    if mode == "oracle":
        shutil.copytree(task_dir / "solution", repo, dirs_exist_ok=True)
    elif mode == "agent":
        import agent  # imported lazily so oracle/noop work without an API key
        TRAJ.mkdir(parents=True, exist_ok=True)
        traj_path = TRAJ / f"{label}-{task_dir.name}-r{rep}.jsonl"
        outcome = agent.run((task_dir / "task.md").read_text(), str(repo), str(traj_path))
    passed, tail = check(task_dir, repo)
    shutil.rmtree(tmp, ignore_errors=True)
    return {"task": task_dir.name, "rep": rep, "passed": passed,
            "seconds": round(time.time() - t0, 1), "trajectory": str(traj_path) if traj_path else None,
            "check_tail": None if passed else tail, **outcome}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["agent", "oracle", "noop"], default="agent")
    ap.add_argument("--tasks", default="", help="comma-separated task names; default all")
    ap.add_argument("--repeat", type=int, default=1)
    ap.add_argument("--label", default="run")
    args = ap.parse_args()

    names = [n for n in args.tasks.split(",") if n] or sorted(p.name for p in TASKS.iterdir() if p.is_dir())
    stamp = dt.datetime.now().strftime("%Y%m%d-%H%M")
    rows = []
    for name in names:
        for rep in range(1, args.repeat + 1):
            r = run_one(TASKS / name, args.mode, args.label, rep)
            rows.append(r)
            mark = "PASS" if r["passed"] else "fail"
            print(f"{mark}  {name:<24} status={r['status']:<10} steps={r['steps']:<3} "
                  f"in={r['input_tokens']:<8} out={r['output_tokens']:<6} {r['seconds']}s", flush=True)

    n = len(rows)
    passed = sum(r["passed"] for r in rows)
    tokens = sum(r["input_tokens"] + r["output_tokens"] for r in rows)
    print(f"\n{args.label}: {passed}/{n} passed ({passed / n:.0%}), {tokens:,} tokens total")

    if args.repeat > 1:
        per_task = {}
        for r in rows:
            per_task.setdefault(r["task"], []).append(r["passed"])
        rates = [sum(v) / len(v) for v in per_task.values()]
        print(f"per-task pass rate: mean {statistics.mean(rates):.2f}, "
              f"stdev {statistics.pstdev(rates):.2f}")

    if args.mode == "agent":
        RESULTS.mkdir(parents=True, exist_ok=True)
        with open(RESULTS / f"{stamp}-{args.label}.jsonl", "w") as f:
            for r in rows:
                f.write(json.dumps(r) + "\n")
        hist = RESULTS / "history.tsv"
        new = not hist.exists()
        prev = None
        if not new:
            lines = hist.read_text().strip().splitlines()[1:]
            prev = lines[-1].split("\t") if lines else None
        with open(hist, "a") as f:
            if new:
                f.write("when\tlabel\tmodel\tpassed\tn\ttokens\n")
            model = os.environ.get("HARNESS_MODEL", "claude-haiku-4-5-20251001")
            f.write(f"{stamp}\t{args.label}\t{model}\t{passed}\t{n}\t{tokens}\n")
        if prev:
            print(f"previous run ({prev[1]}): {prev[3]}/{prev[4]} passed, {int(prev[5]):,} tokens")

    sys.exit(0 if args.mode != "noop" else (1 if passed else 0))


if __name__ == "__main__":
    main()
