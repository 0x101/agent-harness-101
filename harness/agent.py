#!/usr/bin/env python3
"""harness-lab v0: a deliberately naive coding agent.

This file is the thing you will grow over the curriculum. It is naive on purpose.
Known gaps, each one the subject of a later module:
  - one tool (bash), whose raw output is returned in full with no truncation   (M1)
  - no stuck detection beyond a step cap                                       (M2)
  - the message history grows without bound until the API refuses it           (M3)
  - no planning, no subagents                                                  (M4, M5)
  - it declares victory without checking its own work                          (M6)

Usage:
  python harness/agent.py --workdir path/to/repo "Fix the failing test"
"""
import argparse
import json
import os
import subprocess
import sys

import anthropic

MODEL = os.environ.get("HARNESS_MODEL", "claude-haiku-4-5-20251001")
MAX_STEPS = int(os.environ.get("HARNESS_MAX_STEPS", "30"))

SYSTEM = (
    "You are a coding agent working in a repository that is your current working directory. "
    "Use the bash tool to inspect and change files. "
    "When the task is complete, reply with a one-paragraph summary and no tool call."
)

TOOLS = [{
    "name": "bash",
    "description": "Run a bash command in the repository and return its exit code, stdout and stderr.",
    "input_schema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"],
    },
}]


def run_bash(command, cwd):
    try:
        p = subprocess.run(command, shell=True, cwd=cwd, capture_output=True, text=True, timeout=120)
        return f"exit={p.returncode}\n{p.stdout}{p.stderr}"
    except subprocess.TimeoutExpired:
        return "error: command timed out after 120s"


def run(task, workdir, trajectory_path=None, client=None):
    """Run the agent on one task. Returns a dict of outcome metrics."""
    client = client or anthropic.Anthropic()
    messages = [{"role": "user", "content": task}]
    usage = {"input_tokens": 0, "output_tokens": 0}
    log = open(trajectory_path, "w") if trajectory_path else None

    def record(event):
        if log:
            log.write(json.dumps(event) + "\n")
            log.flush()

    try:
        for step in range(1, MAX_STEPS + 1):
            try:
                resp = client.messages.create(
                    model=MODEL, max_tokens=4096, system=SYSTEM, tools=TOOLS, messages=messages)
            except anthropic.APIError as e:
                # Context overflow lands here. So do rate limits. Telling them apart is your job.
                record({"step": step, "error": str(e)})
                return {"status": "api_error", "steps": step, "error": str(e)[:300], **usage}

            usage["input_tokens"] += resp.usage.input_tokens
            usage["output_tokens"] += resp.usage.output_tokens
            messages.append({"role": "assistant", "content": resp.content})
            record({"step": step, "assistant": [b.model_dump() for b in resp.content],
                    "usage": resp.usage.model_dump()})

            calls = [b for b in resp.content if b.type == "tool_use"]
            if not calls:
                return {"status": "done", "steps": step, **usage}

            results = []
            for call in calls:
                output = run_bash(call.input.get("command", ""), workdir)
                record({"step": step, "tool": call.input, "output": output})
                results.append({"type": "tool_result", "tool_use_id": call.id, "content": output})
            messages.append({"role": "user", "content": results})

        return {"status": "max_steps", "steps": MAX_STEPS, **usage}
    finally:
        if log:
            log.close()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("task")
    ap.add_argument("--workdir", default=".")
    ap.add_argument("--trajectory", default=None)
    args = ap.parse_args()
    print(json.dumps(run(args.task, os.path.abspath(args.workdir), args.trajectory), indent=2))
    sys.exit(0)
