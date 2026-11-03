# Agent Harness 101 curriculum

This curriculum has 42 sessions of 45 to 60 minutes each. At five sessions a week it takes about eight and a half weeks.

Every session follows the same shape:

- **Read** (about 20 min). One paper, post or section. The keys (A1, P10, ...) refer to `readings.tsv`.
- **Build** (about 30 min). One change to `harness/agent.py` or the lab tooling.
- **Measure** (about 10 min). Run the evals, then write the log entry.

Some sessions are read-heavy and some are build-heavy. If a build overruns, finish it next session rather than skipping ahead. The log is the source of truth for where you are.

The eval set has 12 tasks, so one task flipping moves the pass rate by 8 points. Treat single-run deltas of one task as noise until repeats confirm them. Session S33 formalizes this.

Each session has its own file under `sessions/`. The keys (A1, P10, ...) refer to `readings.tsv`, and each has a guide under `readings/`.

## M0. Orientation and baseline (S01 to S03)

- [S01. What a harness is](sessions/s01-what-a-harness-is.md)
- [S02. The baseline](sessions/s02-the-baseline.md)
- [S03. Reading trajectories](sessions/s03-reading-trajectories.md)

## M1. The agent-computer interface (S04 to S09)

- [S04. Interfaces matter](sessions/s04-interfaces-matter.md)
- [S05. Truncate tool output](sessions/s05-truncate-tool-output.md)
- [S06. Designing tools](sessions/s06-designing-tools.md)
- [S07. File viewing and search](sessions/s07-file-viewing-and-search.md)
- [S08. An edit tool that teaches](sessions/s08-an-edit-tool-that-teaches.md)
- [S09. Checkpoint: the minimalist's challenge](sessions/s09-checkpoint-the-minimalists-challenge.md)

## M2. Loop control and reliability (S10 to S12)

- [S10. Stuck detection](sessions/s10-stuck-detection.md)
- [S11. Failure handling](sessions/s11-failure-handling.md)
- [S12. Harness bugs](sessions/s12-harness-bugs.md)

## M3. Context management (S13 to S18)

- [S13. Seeing the context](sessions/s13-seeing-the-context.md)
- [S14. A stable prefix and prompt caching](sessions/s14-a-stable-prefix-and-prompt-caching.md)
- [S15. Rule-based elision](sessions/s15-rule-based-elision.md)
- [S16. Summarization compaction](sessions/s16-summarization-compaction.md)
- [S17. The context ablation grid](sessions/s17-the-context-ablation-grid.md)
- [S18. Checkpoint 1](sessions/s18-checkpoint-1.md)

## M4. Planning (S19 to S22)

- [S19. A to-do tool](sessions/s19-a-to-do-tool.md)
- [S20. Enforcing a read-only planner](sessions/s20-enforcing-a-read-only-planner.md)
- [S21. Who planning helps](sessions/s21-who-planning-helps.md)
- [S22. Workflow versus agent](sessions/s22-workflow-versus-agent.md)

## M5. Subagents and orchestration (S23 to S26)

- [S23. The multi-agent debate](sessions/s23-the-multi-agent-debate.md)
- [S24. An explore subagent](sessions/s24-an-explore-subagent.md)
- [S25. Where your design sits](sessions/s25-where-your-design-sits.md)
- [S26. An event stream](sessions/s26-an-event-stream.md)

## M6. Verification and long-running work (S27 to S30)

- [S27. A verification gate](sessions/s27-a-verification-gate.md)
- [S28. An evaluator role](sessions/s28-an-evaluator-role.md)
- [S29. Repo-local instructions and permissions](sessions/s29-repo-local-instructions-and-permissions.md)
- [S30. Checkpoint 2](sessions/s30-checkpoint-2.md)

## M7. Evaluation rigor (S31 to S34)

- [S31. Cost matters](sessions/s31-cost-matters.md)
- [S32. Writing tasks](sessions/s32-writing-tasks.md)
- [S33. Noise](sessions/s33-noise.md)
- [S34. Ablations and interference](sessions/s34-ablations-and-interference.md)

## M8. Harness optimization (S35 to S38)

- [S35. Search over agent designs](sessions/s35-search-over-agent-designs.md)
- [S36. Proposing changes from traces](sessions/s36-proposing-changes-from-traces.md)
- [S37. The outer loop](sessions/s37-the-outer-loop.md)
- [S38. Open-ended improvement](sessions/s38-open-ended-improvement.md)

## M9. Porting to a domain (S39 to S42)

- [S39. Choosing a domain](sessions/s39-choosing-a-domain.md)
- [S40. Domain tasks](sessions/s40-domain-tasks.md)
- [S41. Domain tools and skills](sessions/s41-domain-tools-and-skills.md)
- [S42. Capstone](sessions/s42-capstone.md)
