---
id: S11
module: M2
title: "Failure handling"
order: 11
reads: []
optional: []
cites: []
---
- Build: Separate retryable API errors (rate limits, overload) from fatal ones (context overflow). Add backoff for the retryable ones and a wall-clock limit.
- Measure: Run the full eval. `api_error` statuses should now tell you which kind of failure occurred.
