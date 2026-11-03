"""Unit tests for the agent loop, using a scripted fake client (no API calls).

Copy this pattern when you add harness components: script the model's turns,
run the loop, and assert on what the harness did.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import agent  # noqa: E402
from anthropic.types import Message, TextBlock, ToolUseBlock, Usage  # noqa: E402


def fake_client(turns):
    """turns: list of content-block lists, one per model response."""
    script = list(turns)

    class Messages:
        def __init__(self):
            self.calls = []

        def create(self, **kw):
            self.calls.append(kw)
            content = script.pop(0)
            return Message(id="m", type="message", role="assistant", model="fake", content=content,
                           stop_reason="end_turn", stop_sequence=None,
                           usage=Usage(input_tokens=100, output_tokens=10))

    class Client:
        messages = Messages()

    return Client()


def bash(cmd, i="t1"):
    return ToolUseBlock(type="tool_use", id=i, name="bash", input={"command": cmd})


class LoopTest(unittest.TestCase):
    def test_runs_tool_then_finishes(self):
        d = tempfile.mkdtemp()
        client = fake_client([[bash("echo hi > out.txt")], [TextBlock(type="text", text="done")]])
        result = agent.run("task", d, client=client)
        self.assertEqual(result["status"], "done")
        self.assertEqual(result["steps"], 2)
        self.assertEqual(result["input_tokens"], 200)
        self.assertEqual(open(os.path.join(d, "out.txt")).read().strip(), "hi")

    def test_step_cap(self):
        d = tempfile.mkdtemp()
        client = fake_client([[bash("true", f"t{i}")] for i in range(agent.MAX_STEPS)])
        result = agent.run("task", d, client=client)
        self.assertEqual(result["status"], "max_steps")

    def test_tool_output_reaches_model(self):
        d = tempfile.mkdtemp()
        client = fake_client([[bash("echo marker-42")], [TextBlock(type="text", text="done")]])
        agent.run("task", d, client=client)
        # messages: [task, assistant tool call, tool results, ...]; the list is shared, so index it
        tool_results = client.messages.calls[-1]["messages"][2]
        self.assertIn("marker-42", tool_results["content"][0]["content"])


if __name__ == "__main__":
    unittest.main()
