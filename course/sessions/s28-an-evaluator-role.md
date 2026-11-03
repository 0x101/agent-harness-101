---
id: S28
module: M6
title: "An evaluator role"
order: 28
reads: [A6, P26]
optional: []
cites: []
---
- Read: A6, Rajasekaran on planner, generator and evaluator roles. Then P26, The Unreliable Progress Bar (abstract and main findings): models misreport their own progress mid-task, which is why the evaluator is a separate call and not a question to the agent.
- Build: A separate model call grades the diff against the task before the run finishes.
- Measure: How many false "done" claims does it catch? What does it cost in tokens?
