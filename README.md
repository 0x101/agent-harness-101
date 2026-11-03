# Agent Harness 101

Learn agent harness engineering by building one. You start with a deliberately naive coding agent, about a hundred lines with a single bash tool, and grow it one component at a time over 42 sessions: tool design, loop control, context management, planning, subagents, verification, evaluation rigor, and harness optimization. Every session reads the paper or post that motivates a component, builds it, and measures it against a 12-task eval set. The deliverable is your understanding, not the code.

The tutor is Claude Code with a set of rules in `tutor/SYSTEM.md`: it quizzes you on the reading, gives hints in escalating steps, reviews your changes, and refuses to write your agent for you unless you ask it to.

## Three ways in

1. **Read the course on the site.** The curriculum, every session, and a reading guide for each of the 47 papers and posts, with citations that link. No setup. (Site URL goes here once deployed; until then, `make site-dev`.)
2. **Run the lab on your machine.** Create your own repository from this template, clone it, and work through the sessions with Claude Code. This is the intended path.
3. **Run it in Codespaces.** Open your copy in a GitHub Codespace; `.devcontainer/` installs Python, Node and Claude Code. Set `ANTHROPIC_API_KEY` as a Codespaces secret first.

## Setup for path 2

```bash
# on GitHub: "Use this template" -> your-name/agent-harness-101, then
git clone git@github.com:your-name/agent-harness-101.git && cd agent-harness-101
git remote add upstream https://github.com/0x101/agent-harness-101.git
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export ANTHROPIC_API_KEY=...
make init                         # merge driver, your name, fresh state
make papers                       # downloads the readings into papers/ (gitignored)
make check                        # oracle 12/12, noop 0/12
make test                         # unit tests, no API calls
```

Then open the repo in Claude Code and type `/today`. Claude reads your place in `log/STATE.md`, runs the session from `course/sessions/`, quizzes you on the reading, reviews your build, and drafts the log entry. After every tenth session, `/review` revises the remaining plan from your log.

To pull curriculum updates later: `git fetch upstream && git merge upstream/main`. Your `harness/`, `scripts/`, `log/` and `evals/results/` are protected by a merge driver, so an upstream change never overwrites your work.

## Layout

| Path | What it is | Owner |
|---|---|---|
| `course/curriculum.md` | Overview and the module index | upstream |
| `course/sessions/` | 42 session files, one per session, with read, build and measure steps | upstream |
| `course/readings.tsv`, `course/readings/`, `course/readings.bib` | The reading list with licenses, a guide per reading, BibTeX | upstream |
| `tutor/` | The tutor rules, and a hook that keeps the tutor out of your code | upstream |
| `evals/run.py`, `evals/tasks/` | The runner and 12 tasks: `task.md`, `repo/`, hidden tests, reference solution | upstream |
| `site/` | The website, built from `course/` | upstream |
| `harness/agent.py` | Your agent. Starts naive on purpose | you |
| `harness/tests/` | Loop tests with a fake client, so they make no API calls | you |
| `scripts/` | Tooling you write during the course | you |
| `log/` | `STATE.md`, one entry per session, checkpoints | you |
| `evals/results/` | Per-run JSONL files plus `history.tsv`, the running scoreboard | you |
| `evals/trajectories/` | One JSONL file per task run (gitignored). Read these before theorizing about failures | you |
| `papers/` | `fetch.sh`; the downloads are gitignored | upstream |

## The eval tasks

| Task | What it stresses |
|---|---|
| 01-pagination, 05-lru-cache | Small, well-scoped bug fixes |
| 02-parse-duration, 10-email-validator, 12-toposort | Implementing to a spec with edge cases |
| 03-csv-report, 08-ini-to-json, 09-cli-flag | Writing or extending small programs |
| 04-rename-api | Coordinated edits across several files |
| 06-needle-in-logs | A 5 MB log file. Running `cat` on it overflows the context |
| 07-big-repo-bug | Locating a bug among 30 noise modules |
| 11-noisy-tests | A test suite that prints about 6,000 lines around a single failure |

The default model is `claude-haiku-4-5-20251001`: cheap, and weak enough that harness changes show up in the numbers. Override with `HARNESS_MODEL`. With 12 tasks one flip is 8 points, so use `--repeat` before believing a delta.

## Licenses

Code is MIT (`LICENSE`). Course content under `course/` is CC BY 4.0 (`course/LICENSE`). The papers and posts belong to their authors and are never committed; `course/readings.tsv` records each item's license. See `CONTRIBUTING.md` for adding tasks and readings.
