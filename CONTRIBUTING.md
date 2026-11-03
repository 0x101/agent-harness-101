# Contributing

Agent Harness 101 is a course plus a kit. Contributions that make the course teach better or the kit measure better are welcome. Contributions that grow the tooling for its own sake are not the point; see the first paragraph of `tutor/SYSTEM.md`.

## What lives where

| Path | Owner | License |
|---|---|---|
| `course/` sessions, readings, guides | upstream | CC BY 4.0 |
| `tutor/`, `evals/run.py`, `evals/tasks/`, `site/`, `papers/fetch.sh` | upstream | MIT |
| `harness/`, `scripts/`, `log/`, `evals/results/` | each learner's copy | theirs |

Pull requests touch the upstream-owned paths. If you are a learner who found a curriculum bug while working in your own copy, send the `course/` change as a PR and keep your `harness/` and `log/` out of it.

## Adding a task

1. Create `evals/tasks/NN-short-name/` with `task.md`, `repo/`, `hidden/` and `solution/`. Follow an existing task.
2. `hidden/` holds `unittest` files the agent never sees. `solution/` holds the files that make them pass.
3. Run both sanity checks and paste the output in the PR:
   ```
   python evals/run.py --mode oracle --tasks NN-short-name   # must pass
   python evals/run.py --mode noop --tasks NN-short-name     # must fail
   ```
4. Say in the PR which failure class the task targets (context overflow, wrong edit, stuck loop, gave up, declared done without checking) and why the current 12 do not already cover it.
5. Never edit an existing task's `hidden/` or `solution/` to make a run pass. The tutor's hook refuses it, and a reviewer will too.

Public tasks have a shelf life. Once hidden tests are on GitHub, future models may train on them and pass rates will drift upward for reasons that have nothing to do with the harness. S32 has every learner write private tasks for exactly this reason; keep those out of upstream.

## Adding or changing a reading

1. Add a row to `course/readings.tsv`. The `license` column decides what the site may do: `CC-BY-4.0` and other CC licenses may be embedded, `arXiv-nonexclusive-1.0` and `copyright` are linked only. Check the arXiv abstract page for the license.
2. Add `course/readings/<KEY>.md` with a "How to read it for this course" section: which sections, what to skip, how long it takes.
3. Add the BibTeX entry to `course/readings.bib` under a `% KEY` comment. For arXiv papers, `https://arxiv.org/bibtex/<id>` gives it to you.
4. Do not commit the paper or post itself. `papers/fetch.sh` downloads it per machine.

## Changing a session

Sessions are `course/sessions/sNN-slug.md`. Keep the frontmatter keys (`id`, `module`, `title`, `order`, `reads`, `optional`, `cites`) and keep the Measure step runnable with `evals/run.py` as it exists. A session should fit in 45 to 60 minutes; if yours does not, split it rather than compressing the reading.

## Before you open a PR

```
make test     # harness and tutor unit tests, no API calls
make check    # oracle 12/12 and noop 0/12
make site     # the site still builds
```
