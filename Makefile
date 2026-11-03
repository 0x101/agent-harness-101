# Agent Harness 101. `make help` lists the targets.
PY := $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
LABEL ?= run

.PHONY: help init papers check eval test unlock lock site site-dev

help:
	@echo "init      first-time setup of a fresh copy: merge driver, learner name, reset state"
	@echo "papers    download the readings into papers/ (gitignored)"
	@echo "check     validate the tasks: oracle must pass 12/12, noop must pass 0/12"
	@echo "eval      run your agent on every task: make eval LABEL=truncation"
	@echo "test      unit tests for the harness and the tutor hook (no API calls)"
	@echo "unlock    let the tutor edit harness/ for one hour; lock ends it early"
	@echo "site      build the website from course/; site-dev serves it with reload"

init:
	@git config merge.ours.driver true
	@entries=$$(ls log 2>/dev/null | grep -vE '^(STATE|TEMPLATE)\.md$$' | wc -l | tr -d ' '); \
	if [ "$$entries" != "0" ] && [ "$(FORCE)" != "1" ]; then \
	  echo "log/ already has $$entries entries. This looks like a copy in use, not a fresh one."; \
	  echo "Run 'make init FORCE=1' to reset state anyway."; exit 1; fi
	@mkdir -p .lab
	@if [ ! -f .lab/config.toml ]; then \
	  printf "Your name, as the tutor should use it: "; read name; \
	  printf 'name = "%s"\n' "$$name" > .lab/config.toml; \
	fi
	@printf 'current_session: S01\nlast_completed: none\n' > log/STATE.md
	@find log -type f ! -name STATE.md ! -name TEMPLATE.md -delete
	@find evals/results -type f ! -name .gitkeep -delete
	@rm -rf evals/trajectories
	@echo "ready. Next: make papers, then open the repo in Claude Code and type /today"

papers:
	@bash papers/fetch.sh

check:
	@$(PY) evals/run.py --mode oracle
	@$(PY) evals/run.py --mode noop

eval:
	@$(PY) evals/run.py --label $(LABEL) $(ARGS)

test:
	@$(PY) -m unittest discover harness/tests
	@$(PY) -m unittest discover tutor/tests

unlock:
	@mkdir -p .lab && touch .lab/unlock-harness && echo "harness/ unlocked for the tutor until $$(date -v+1H '+%H:%M' 2>/dev/null || date -d '+1 hour' '+%H:%M')"

lock:
	@rm -f .lab/unlock-harness && echo "harness/ locked"

site:
	@cd site && npm install && npm run build

site-dev:
	@cd site && npm install && npm run dev
