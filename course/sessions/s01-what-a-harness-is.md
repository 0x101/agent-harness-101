---
id: S01
module: M0
title: "What a harness is"
order: 1
reads: [A1]
optional: []
cites: []
---
A language model can write a shell command, but it cannot run one. The program that runs the command, hands the result back and decides when to stop is the **harness**. In this session you read the hundred-line harness you will grow for the rest of the course, and you run it once.

Time: about 15 minutes reading, 20 with the code, 5 for the run. Before you start: the setup in [Start here](../start-here.md). Spend: one task on the default model, capped at $1 by the command in this session.

## The problem

Ask a model to fix a bug and it replies with text. The text may contain exactly the right command, but nothing has happened in your repository. Someone has to run the command, read what it printed, and tell the model, and then do it again for the next command.

Doing that by hand works for one command. A bug fix takes ten or twenty: list the files, read one, run the tests, edit, run the tests again. The harness is the code that does the carrying, so the model can take those steps without you.

## Predict first

**The starter agent is about a hundred lines and can run any shell command. Which of these does it also do?**

- A. Shortens long command output before the model sees it.
- B. Stops after a fixed number of steps.
- C. Runs the tests before it says it is finished.
- D. Notices when it repeats the same command.

<details>
<summary>Answer</summary>

**B.** `MAX_STEPS` is 30 unless you set `HARNESS_MAX_STEPS`. A is wrong because `run_bash` returns everything the command printed. C is wrong because the loop ends as soon as the model replies without asking for a tool. D is wrong because nothing compares one step with another. The comment at the top of `harness/agent.py` lists these gaps, and each one is the subject of a later module.

</details>

## The idea

An agent is a model, a set of **tools** (actions the model may ask for), and a loop. The model never runs anything. It replies with a request, the harness carries it out, and the result goes back as the next message.

```text
            task
              |
              v
   +----------------------+
   | send the whole       |<--------------+
   | conversation to the  |               |
   | model                |               |
   +----------------------+               |
              |                           |
     does the reply ask                   |
        for a tool?                       |
        |          |                      |
        no        yes                     |
        |          |                      |
        v          v                      |
      done    +-----------------+         |
              | run the command |---------+
              | (run_bash)      |  the output joins
              +-----------------+  the conversation
```

Open `harness/agent.py` and find each part:

- **The tool.** `TOOLS` describes one tool, `bash`, which takes a `command` string. That description is all the model knows about what it can do.
- **The conversation.** `messages` starts as a list holding the task. Every reply and every result is appended to it, and the whole list is sent again on each call.
- **The call.** `client.messages.create(...)` sends the system prompt, the tool description and the conversation.
- **Carrying out a request.** A reply can contain `tool_use` blocks. For each one, `run_bash` runs the command and the output goes back in a `tool_result` block carrying the same id, so the model can match result to request.
- **Stopping.** The function returns `done` when a reply has no `tool_use` block, `max_steps` when the loop has run 30 times, and `api_error` when the API refuses the call.
- **The record.** `record(...)` writes one line per event to a **trajectory** file, the full history of a run. You will read these files more than any others in this course.

Most of what you build in the next 41 sessions is a change to one of these six parts.

## What the reading says

**A1, Building effective agents**, is the vocabulary for the course. It separates workflows from agents, describes an agent as a model using tools in a loop, and argues for adding complexity only when it measurably helps. Read it with `agent.py` open and tick off what the starter has. The [A1 guide](../readings/A1.md) says which sections to read and which to skip.

## How real harnesses do it

- [mini-swe-agent, `agents/default.py`](https://github.com/SWE-agent/mini-swe-agent/blob/main/src/minisweagent/agents/default.py). The same loop in a harness used for research: `run` calls `step` until an exit message appears. Look at `query`, which checks a step limit, a cost limit and a time limit before every model call. Yours has only the first.
- [How Claude Code works: the agentic loop](https://code.claude.com/docs/en/how-claude-code-works#the-agentic-loop). The official description of a production harness. Notice that it names the same two parts, a model that reasons and tools that act, and calls the layer around them the harness.

## Build

There is no code to write today. You read the file and run it once.

1. Read `harness/agent.py` from top to bottom. It is short enough to read every line.
2. Decide where the agent will run. `run_bash` passes the model's command to your shell with `shell=True`, with your permissions and no restrictions. The runner copies each task into a temporary folder, but nothing keeps a command inside it. Use the Codespace or the dev container from [Start here](../start-here.md) unless you have a reason not to.
3. Run one task:

```bash
python evals/run.py --tasks 01-pagination --label smoke --budget-usd 1
```

### What done looks like

- `make check` ends its two runs with `12/12 passed (100%)` and `0/12 passed (0%)`. That shows the tasks themselves are sound: each can be solved, and none is solved already.
- The smoke run prints one line for `01-pagination` with `steps` and `in=` above zero and a `status` other than `api_error`. If you get a traceback that ends in "Could not resolve authentication method", the key is not set. An `api_error` on this small task usually means the key is wrong or the account has no credit; the trajectory file holds the full message.
- `evals/trajectories/smoke-01-pagination-r1.jsonl` exists. Open it and follow one step: the model's request, the command, the output.

The task does not have to pass. Today is about the loop running.

## Measure

Nothing to compare yet. Write down the steps, tokens and dollars from the smoke line. This course has not yet published a reference cost for this run, so yours is the first number you have. In S02 you run all 12 tasks, and that run is the baseline every later change is measured against.

## Check yourself

**1. In A1's terms, what separates a workflow from an agent?**

- A. A workflow makes one model call and an agent makes many.
- B. In a workflow your code decides the path, and in an agent the model does.
- C. A workflow has no tools.

<details>
<summary>Answer</summary>

**B.** A is wrong because several of A1's workflows chain many calls. C is wrong because a workflow step can use tools. What matters is who chooses the next step.

</details>

**2. Why does the harness send every command's output back to the model?**

- A. So the model can choose its next step from what actually happened.
- B. So the eval runner can score the run.
- C. So the API can count tokens.

<details>
<summary>Answer</summary>

**A.** A1 calls this getting "ground truth" from the environment at each step. Without it the model is guessing at the state of the repository. B is wrong because the runner scores a run by running hidden tests afterwards and never reads the conversation. C is wrong because token counts come from the API whatever the messages hold.

</details>

**3. Task 06 has a 5 MB log file. The agent runs `cat` on it. What does `agent.py` do next?**

- A. It cuts the output to fit and carries on.
- B. It appends all of the output to `messages`, the next call is refused, and the run ends with `api_error`.
- C. It skips the output and asks the model to try another command.

<details>
<summary>Answer</summary>

**B.** `run_bash` returns everything, the loop appends it, and the conversation no longer fits in the model's context window. The `except anthropic.APIError` branch returns `api_error`. A and C describe behaviour the file does not have. You build A in module M1.

</details>

## Design choices

- **One tool, and it is bash.** The alternative is a tool for each job: read a file, edit a file, search. Separate tools let you shape what the model sees and stop some mistakes before they happen. One tool keeps the starting point small, so each later addition can be measured against it. You build the alternative in S06 to S08 and measure it in S09.
- **A step cap is the only limit.** mini-swe-agent also stops on cost and on time. A cost limit is the better choice once tasks differ a lot in length, because 30 short steps and 30 long ones cost very different amounts.
- **The model decides when it is finished.** The alternative is for the harness to check, for example by running the tests before accepting "done". That is module M6.

## Log

Which of A1's patterns does `agent.py` implement, and which does it lack? Add the three numbers from your smoke run.

## Next

S02 runs the untouched agent on all 12 tasks, after you write down which ones you expect to fail.
