---
id: S17
module: M3
title: "The context ablation grid"
order: 17
reads: [P24]
optional: []
cites: [P10]
---
- Read: P24, Toward Reliable Context Compression (abstract and the empirical findings). Compaction can weaken the influence of recent steps and cause repeated exploration. Know what that looks like before you read your own trajectories.
- Build: Add a `HARNESS_CONTEXT_BUDGET` environment variable that forces a small budget, such as 30k tokens.
- Measure: Run four configurations (none, elision, summarization, both) on 06, 07, 11 and two tasks of your choice, each with `--repeat 2`.
- Log: Does your result match P10's finding that elision staged before summarization is most efficient? In the summarization runs, did you see P24's symptoms (a repeated command, a re-read file) right after a compaction event?
