#!/usr/bin/env python3
"""PreToolUse hook: keep the tutor out of the learner's code.

Blocks Edit, Write and MultiEdit when the target is
  - under harness/, unless .lab/unlock-harness exists and is under an hour old (`make unlock`)
  - under evals/tasks/*/hidden/ or evals/tasks/*/solution/, always.

Protocol: tool input arrives as JSON on stdin; exit 2 blocks the call and sends stderr to the model.
Wired in .claude/settings.json. The Agent SDK tutor (phase 3) registers the same function.
"""
import json
import os
import sys
import time

UNLOCK_SECONDS = 3600


def project_root(payload):
    return os.environ.get("CLAUDE_PROJECT_DIR") or payload.get("cwd") or os.getcwd()


def decide(payload, now=None):
    """Return None to allow, or a message to block. Pure, so tests can call it."""
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not path:
        return None
    root = os.path.realpath(project_root(payload))
    target = os.path.realpath(path if os.path.isabs(path) else os.path.join(root, path))
    try:
        rel = os.path.relpath(target, root)
    except ValueError:
        return None
    parts = rel.split(os.sep)
    if rel.startswith(".."):
        return None
    if len(parts) >= 4 and parts[0] == "evals" and parts[1] == "tasks" and parts[3] in ("hidden", "solution"):
        return (f"Refused: {rel} is a hidden test or reference solution. These are never edited to make "
                "a run pass. Add a new task in a new folder instead.")
    if parts[0] == "harness":
        marker = os.path.join(root, ".lab", "unlock-harness")
        now = now or time.time()
        if os.path.exists(marker) and now - os.path.getmtime(marker) < UNLOCK_SECONDS:
            return None
        return (f"Refused: {rel} is under harness/, which is the learner's code. Give a hint, a location, or "
                "pseudocode instead. If the learner explicitly asked you to write it, ask them to run "
                "`make unlock` (a one-hour window) and retry.")
    return None


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0
    message = decide(payload)
    if message:
        print(message, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
