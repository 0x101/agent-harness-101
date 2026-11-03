---
id: S31
module: M7
title: "Cost matters"
order: 31
reads: [P5, P27]
optional: []
cites: []
---
- Read: Re-read P5's cost-controlled evaluation section (first read in S09). Optional: P27, Stop Comparing LLM Agents Without Disclosing the Harness, a position paper arguing that harness configuration explains more variance than model choice. Decide whether your history.tsv supports it.
- Build: Write `scripts/pareto.py` to plot cost against accuracy for every labeled run in `evals/results/history.tsv`.
