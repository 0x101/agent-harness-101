---
id: S24
module: M5
title: "An explore subagent"
order: 24
reads: [P25]
optional: []
cites: []
---
- Read: P25, SWE-Edit (abstract, introduction and the Viewer subagent). Its Viewer is the same idea as today's build: reading happens in a clean context and only the distilled result comes back.
- Build: Add an explore subagent with a fresh context. It returns a summary of at most 300 words to the main agent.
- Measure: On 07, compare main-context tokens and pass rate with and without it.
