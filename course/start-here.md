# Start here

Agent Harness 101 teaches how coding agents work by having you build one. You start with `harness/agent.py`, a deliberately naive agent of about a hundred lines. Over 42 sessions you add one component at a time, read the paper or post behind it, and measure the change on 12 eval tasks. At the end you have your own harness and a log of what each change was worth.

## Who this is for

You can write a small Python function, use a terminal, and clone, commit and pull with git. You do not need a machine learning background or a GPU: the model runs on the provider's servers. If you have never called a model from code, read the [primer](primer.md) first.

## What you need

- A GitHub account.
- An Anthropic API key, from the [Claude Console](https://platform.claude.com/settings/keys).
- [Claude Code](https://code.claude.com/docs/en/quickstart), your tutor.
- A GitHub Codespace, or your own machine with Python 3, git, make and curl. The dev container uses Python 3.12 and Node 24. `requirements.txt` asks for `anthropic>=0.40`.

**Cost.** The course has not yet published a measured cost for a full run of the 12 tasks. The default model is `claude-haiku-4-5-20251001`. Put `--budget-usd N` on every paid run. Before each model call, the runner reserves the most that call could cost, and stops if that could take the spend past N dollars. The spend is kept in a ledger file, `evals/results/spend.json`, so one cap covers all your runs together. Delete the file to start a new budget. Setting `HARNESS_BUDGET_USD` in your environment applies the cap to every run started from that shell. The cap covers the eval runs only, not what Claude Code itself uses as your tutor.

## Pick how you will work

1. **Read the course on the site.** No setup and no key, but you run nothing.
2. **A GitHub Codespace (recommended).** `harness/agent.py` runs whatever shell command the model writes, with `shell=True`, with your permissions, and nothing confines it to the task folder. A Codespace is a disposable machine that holds none of your other files. In session 29 you add a check on destructive commands. Until then, nothing stops them.
3. **Your own machine.** The same lab, but every command the model writes runs as you, among your files.

## Set up

1. On GitHub, open the course repository and choose **Use this template** to create your own copy.
2. Codespace route: add a [Codespaces secret](https://docs.github.com/en/codespaces/managing-your-codespaces/managing-your-account-specific-secrets-for-github-codespaces) named `ANTHROPIC_API_KEY`, give your copy access to it, then create a codespace on your copy. The dev container creates `.venv`, installs `requirements.txt` into it, and installs Claude Code. Run `source .venv/bin/activate` and go to step 4.
3. Own-machine route:

```bash
git clone git@github.com:your-name/agent-harness-101.git
cd agent-harness-101
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
```

4. Both routes:

```bash
git remote add upstream \
  https://github.com/0x101/agent-harness-101.git
make init     # merge driver, your name, fresh state
make papers   # downloads the readings into papers/
make check    # oracle 12/12, noop 0/12
make test     # unit tests, no API calls
```

## Check your setup

Neither command calls the API. `make check` tests the tasks, not your agent, and prints one line per task, twice. In the first pass each reference solution is copied in, every line starts with `PASS`, and the last line is `run: 12/12 passed (100%), 0 tokens total`. In the second nothing changes, every line starts with `fail`, and the last line is `run: 0/12 passed (0%), 0 tokens total`.

`make test` runs three suites, and each one ends with `OK`. A `ResourceWarning` from `harness/tests/test_loop.py` may appear first; it does not fail anything.

## How a session goes

Open the repository in Claude Code and type `/today`. The tutor reads `log/STATE.md` and the session file, checks your last log entry for an unfinished build, and asks you to predict something before you read. After the reading it asks three questions: recall, "why", and how the idea would change `agent.py`. You build, it runs the evals and compares them with your previous comparable run, and it drafts the log entry for you to edit.

The tutor does not write `harness/` for you. It gives a hint, then where the change goes, then pseudocode, and code only when you ask. A hook blocks its edits under `harness/` until you run `make unlock`, which opens a one-hour window.

Every session page on the site also stands on its own.

## Where your work lives

- `harness/`, `scripts/`, `log/` and `evals/results/` are yours.
- `log/STATE.md` holds your place.
- `evals/results/history.tsv` is your scoreboard: one row per agent run, with label, model, tasks passed and tokens.
- `evals/trajectories/` holds one file per task run. It is gitignored.

To take course updates, run `git fetch upstream && git merge upstream/main`. `.gitattributes` marks your four folders `merge=ours`, and `make init` turns that driver on with `git config merge.ours.driver true`. If both you and upstream changed a file there, the merge keeps your version whole. A file you never changed takes upstream's version. The setting is per clone, so run that `git config` line in any new clone or codespace.

## If you get stuck

- **A traceback ending in "Could not resolve authentication method".** The key is not set in this shell. In a Codespace, a new secret appears only after you stop and restart it.
- **"BUDGET STOP".** The next call could have taken the ledger in `evals/results/spend.json` past the cap. The run exits with code 3 and keeps the tasks it finished. Raise N, or delete the file.
- **`make init` says "log/ already has N entries".** It will not reset a copy in use. `make init FORCE=1` deletes your log, results and trajectories.
- **`make papers` prints `FAIL` for a post.** Some sites block the fetcher. Open the URL in a browser.

## Next

New to tool use and context windows? Read the [primer](primer.md). Otherwise go to [session 1](sessions/s01-what-a-harness-is.md).
