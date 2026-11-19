# Primer: what session 1 assumes

This page teaches the ideas session 1 takes for granted, each tied to the line of `harness/agent.py` that uses it. If you have already built something with a model API and tool use, skip to [session 1](sessions/s01-what-a-harness-is.md).

## A model call

A model is a function you call over the network. Text goes in, text comes out. This is a **model call**.

The model keeps no memory between calls. If you want it to know what was said before, you send it again. So a program that holds a conversation keeps the whole conversation in a list and sends the full list every time.

The conversation is made of turns, and each turn has a **role**:

- The **system prompt** is standing instructions from the program. In `agent.py` it is `SYSTEM`, sent as its own `system=` argument rather than as a turn.
- A **user** turn is what the program sends. The first one holds the task.
- An **assistant** turn is what the model replied.

In `agent.py` the list is `messages`. It starts as `[{"role": "user", "content": task}]`, and every reply and every result is appended to it. The call itself is `client.messages.create(...)`, which sends `SYSTEM`, the tool list and `messages`, and returns the reply.

## Tokens and the context window

A model does not read letters or whole words. It reads **tokens**, pieces of words. A short common word is often one token, and a long or rare word is several.

The model reads at most a fixed number of tokens per call. That limit is its **context window**. For the course's default model, `claude-haiku-4-5-20251001`, the price table in `evals/budget.py` records 200,000 tokens.

Because `agent.py` appends everything and never removes anything, the conversation grows with every step. When it no longer fits, the API refuses the call. `agent.py` has no special handling for this. The call raises an error, the `except anthropic.APIError` branch writes the error to the trajectory, and the run ends with status `api_error`. The comment in that branch says rate limits land there too, and telling the two apart is left to you.

## Tools

A model cannot run anything. It can only write text. A **tool** is an action the program offers to carry out on the model's behalf. The program describes it, and the description is all the model knows. This is the only tool in `agent.py`:

```python wrap
TOOLS = [{
    "name": "bash",
    "description": "Run a bash command in the repository and return its exit code, stdout and stderr.",
    "input_schema": {
        "type": "object",
        "properties": {"command": {"type": "string"}},
        "required": ["command"],
    },
}]
```

When the model wants the tool, its reply contains a **`tool_use`** block: the tool's name, the input, and an id. The program runs the command and sends the output back in a **`tool_result`** block that carries the same id, so the model can match the result to its request.

```text
program (agent.py)         model
------------------         -----
1. sends SYSTEM,  ------>
   TOOLS, messages
                           2. replies
                  <------     tool_use
                              id "abc"
                              "ls"
3. run_bash("ls")
   on your machine
4. sends          ------>
   tool_result
   tool_use_id "abc"
   "exit=0 ..."
                           5. replies
                  <------     text, no
                              tool_use
6. loop ends:
   status "done"
```

Step 3 is the only place anything happens to your files, and it happens in your program, not in the model.

## What a run costs

You pay per token, and **input tokens** (what you send) and **output tokens** (what the model writes) are priced separately. For the default model, `evals/budget.py` records $1.00 per million input tokens and $5.00 per million output tokens. Prices change. The [pricing page](https://platform.claude.com/docs/en/about-claude/pricing) is the authority, not this page.

A long run costs more than its step count suggests, because every step sends the whole conversation again. Take round numbers, chosen for the arithmetic and not measured on any task: the first call sends 1,000 tokens, each step adds 500 more, and each reply is 100 tokens.

```text
call 1 sends 1,000
call 2 sends 1,000 + 500     = 1,500
call 3 sends 1,000 + 2 x 500 = 2,000
...
call 10 sends 1,000 + 9 x 500 = 5,500

input over 10 calls:
  10 x 1,000 + 500 x (0+1+...+9)
  = 10,000 + 500 x 45 = 32,500 tokens
output: 10 x 100 = 1,000 tokens

32,500 x $1.00 / 1,000,000 = $0.0325
 1,000 x $5.00 / 1,000,000 = $0.0050
total                      = $0.0375
```

The conversation is only 5,500 tokens long at the end, but you paid for 32,500 input tokens to get there. Twice the steps costs more than twice as much. The `in=` figure the runner prints for each task is this sum: `agent.py` adds up `input_tokens` over every call.

## Agent, harness, trajectory

- An **agent** is a model, a set of tools, and a loop, where the model decides the next step. That is the definition in session 1 and in the [A1 guide](readings/A1.md).
- The **harness** is the program around the model: it sends the conversation, runs the tools, hands back the results and decides when to stop. `agent.py` is your harness.
- A **trajectory** is the full record of one run. `agent.py` writes one line per event to a file in `evals/trajectories/`.

## Evals

An **eval** measures the agent on fixed tasks. Each task in `evals/tasks/` has `task.md` (the instruction), `repo/` (the starting files), and **hidden tests** the agent never sees. The runner copies `repo/` to a fresh folder, lets the agent work, then runs the hidden tests. A task passes if they pass. The **pass rate** is the share of tasks that passed.

`make check` runs two sanity checks on the tasks themselves. **Oracle** mode copies each task's reference solution over the repo and must pass all 12. **Noop** mode changes nothing and must pass none. Together they show each task can be solved and none is solved already.

One run is not enough to judge a change. A model does not give the same answer every time, so the same agent can pass a task on one run and fail it on the next. With 12 tasks, one task changing moves the pass rate by 8 points. `--repeat N` runs every task N times, and the runner then prints the mean and standard deviation of the per-task pass rates.

## Check yourself

**1. The model's reply contains a `tool_use` block asking for `ls`. Where does `ls` run?**

- A. On the provider's servers, inside the model.
- B. On your machine, in `run_bash`.
- C. Nowhere until the eval runner checks the result.

<details>
<summary>Answer</summary>

**B.** `run_bash` passes the command to your shell in the task folder. A is wrong because a model only writes text; the `tool_use` block is a request, not an action. C is wrong because the runner only runs the hidden tests after the agent has finished.

</details>

**2. Every step adds about the same amount to the conversation. A run takes 20 steps instead of 10. What happens to the input tokens?**

- A. They stay about the same.
- B. They exactly double.
- C. They more than double.

<details>
<summary>Answer</summary>

**C.** Each call sends the whole conversation, and the later calls are the longest. With the numbers above, 20 calls send 115,000 input tokens against 32,500 for 10. A is wrong because every call is billed for everything it sends. B would be true only if each call sent just the new part, which `agent.py` does not do.

</details>

**3. After a change, one run goes from 5/12 to 6/12. What do you conclude?**

- A. The change adds 8 points.
- B. One task flipped, which is within noise. Repeat the runs before deciding.
- C. The change made the agent worse at the other tasks.

<details>
<summary>Answer</summary>

**B.** One task is 8 points, and the same agent can flip a task between runs. A is wrong because one run cannot separate the change from chance. C is wrong because the count went up, and a single run says nothing about why.

</details>

## Go deeper

- [Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview): the official description of `tool_use` and `tool_result`.
- [Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages): roles, turns and sending the conversation back.
- [Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows): what fills the window and what happens at the limit.
