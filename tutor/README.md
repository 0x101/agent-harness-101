# tutor/

The tutor harness. Claude Code loads `SYSTEM.md` through the `@tutor/SYSTEM.md` line in the root `CLAUDE.md`; the slash commands live in `.claude/commands/`; the hook in `hooks/` is wired in `.claude/settings.json`.

Phase 3 of `docs/rearchitecture-proposal.md` adds an Agent SDK tutor in `server/tutor.py` that uses the same `SYSTEM.md` and the same hook, so the browser tutor and the terminal tutor never drift.

Run the hook's tests with `python -m unittest discover tutor/tests`.
