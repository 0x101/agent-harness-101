import os
import sys
import tempfile
import time
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hooks"))
import guard_harness  # noqa: E402


class GuardTest(unittest.TestCase):
    def setUp(self):
        self.root = tempfile.mkdtemp()
        os.makedirs(os.path.join(self.root, "harness"))
        os.makedirs(os.path.join(self.root, "evals", "tasks", "01-x", "hidden"))
        os.makedirs(os.path.join(self.root, "log"))

    def payload(self, path, tool="Edit"):
        return {"cwd": self.root, "tool_name": tool, "tool_input": {"file_path": os.path.join(self.root, path)}}

    def test_blocks_harness_by_default(self):
        self.assertIn("harness/", guard_harness.decide(self.payload("harness/agent.py")))

    def test_allows_harness_when_unlocked(self):
        os.makedirs(os.path.join(self.root, ".lab"))
        open(os.path.join(self.root, ".lab", "unlock-harness"), "w").close()
        self.assertIsNone(guard_harness.decide(self.payload("harness/agent.py")))

    def test_unlock_expires(self):
        os.makedirs(os.path.join(self.root, ".lab"))
        marker = os.path.join(self.root, ".lab", "unlock-harness")
        open(marker, "w").close()
        old = time.time() - guard_harness.UNLOCK_SECONDS - 1
        os.utime(marker, (old, old))
        self.assertIsNotNone(guard_harness.decide(self.payload("harness/agent.py")))

    def test_hidden_and_solution_never_unlock(self):
        os.makedirs(os.path.join(self.root, ".lab"))
        open(os.path.join(self.root, ".lab", "unlock-harness"), "w").close()
        self.assertIn("hidden", guard_harness.decide(self.payload("evals/tasks/01-x/hidden/test_x.py")))
        self.assertIn("hidden", guard_harness.decide(self.payload("evals/tasks/01-x/solution/x.py")))

    def test_allows_log_and_relative_paths(self):
        self.assertIsNone(guard_harness.decide(self.payload("log/2026-11-02-S01.md")))
        rel = {"cwd": self.root, "tool_input": {"file_path": "scripts/pareto.py"}}
        self.assertIsNone(guard_harness.decide(rel))

    def test_no_path_allows(self):
        self.assertIsNone(guard_harness.decide({"cwd": self.root, "tool_input": {}}))


if __name__ == "__main__":
    unittest.main()
