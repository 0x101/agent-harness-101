#!/bin/bash
# Web sessions start from a fresh clone: install Python deps and fetch the
# gitignored course material (papers/pdf, papers/web, papers/repos).
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"

pip install -q -r requirements.txt

# fetch.sh skips files it already has; a single failed URL shouldn't block the session.
bash papers/fetch.sh || echo "papers/fetch.sh reported errors; continuing" >&2
