---
id: S37
module: M8
title: "The outer loop"
order: 37
reads: [P28]
optional: []
cites: []
---
- Read: P28, HarnessLens (abstract, introduction and the verification-budget argument). Scoring every candidate on the full task set is the cost that limits today's loop; P28 verifies each candidate only on the tasks its change could affect.
- Build: Chain the steps. Propose a change, apply it on a git branch, evaluate on a train split of 9 tasks, and accept the change only if it scores better. Then test on 3 held-out tasks.
- Log: Did anything the loop accepted fail on the held-out tasks? That is overfitting.
