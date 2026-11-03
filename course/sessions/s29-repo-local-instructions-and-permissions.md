---
id: S29
module: M6
title: "Repo-local instructions and permissions"
order: 29
reads: [A7, B7, B2]
optional: []
cites: []
---
- Read: A7, Claude Code best practices (the sections on CLAUDE.md and on giving Claude tools). Then B7, Codex as a platform, for what the harness does at the sandbox and approval boundary. B2, OpenAI's harness engineering post, is the origin of the idea; skim it in a browser, since openai.com blocks the fetcher.
- Build: Load `AGENTS.md` from the working directory into the system prompt when it exists. Write one for a task repo and measure the effect. Then the other half of the environment layer: `agent.py` runs every command with `shell=True` and no restriction. Add a deny-list (or a confirm step) for destructive commands such as `rm -rf`, `git push` and anything that leaves the workdir, and a unit test that proves it fires.
- Log: A harness decides what the model sees and what it may do. Which of the two has your harness been ignoring until today?
