# Agent Harness 101

@tutor/SYSTEM.md

## Facts about the lab

- The default model is `claude-haiku-4-5-20251001`, which is cheap and makes harness effects visible. Override it with `HARNESS_MODEL`. Always report token counts next to pass rates.
- `python evals/run.py --mode oracle` should score 12/12, and `--mode noop` should score 0/12. Run both after touching the runner.
- Trajectories are in `evals/trajectories/`, one JSONL file per task run. Read them before theorizing about failures.
- `harness/tests/` holds unit tests that use a fake client, with no API calls. Run them with `python -m unittest discover harness/tests`.
- The curriculum is `course/curriculum.md` (overview) and `course/sessions/` (one file per session). Readings are `course/readings.tsv` (metadata and licenses) and `course/readings/` (one guide per key).
- Ownership: `course/`, `tutor/`, `evals/run.py`, `evals/tasks/` and `site/` come from upstream. `harness/`, `scripts/`, `log/` and `evals/results/` belong to the learner and are protected by a merge driver (see `.gitattributes`).
