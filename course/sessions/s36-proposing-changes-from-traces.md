---
id: S36
module: M8
title: "Proposing changes from traces"
order: 36
reads: [P17, P13]
optional: [P29]
cites: []
---
- Read: P17 (Meta-Harness) and P13 (Agentic Harness Engineering).
- Optional: P29, SoL-Pi. The same propose-and-select loop, but scored on token traffic rather than pass rate. Note which four mechanisms survived its selection and where each one appears in this curriculum.
- Build: Write `scripts/propose.py`. It gives Claude the failed trajectories and `agent.py`, and asks for exactly one targeted change as a diff.
