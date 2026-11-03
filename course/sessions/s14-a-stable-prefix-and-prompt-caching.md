---
id: S14
module: M3
title: "A stable prefix and prompt caching"
order: 14
reads: [B5]
optional: []
cites: []
---
- Read: B5, the Manus lessons.
- Build: Keep the system prompt and tools byte-stable, then add `cache_control` breakpoints. Count cache-read tokens separately in usage.
- Measure: Compare cost per task before and after.
