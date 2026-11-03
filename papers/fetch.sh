#!/usr/bin/env bash
# Download every paper and post listed in course/readings.tsv.
#   arxiv -> papers/pdf/<file>.pdf
#   web   -> papers/web/<file>.html   (the tutor can read these, or re-fetch the URL)
#   repo  -> shallow clone into papers/repos/<file>
# Everything lands in gitignored directories: most of these items may not be redistributed.
# Safe to re-run: existing files are skipped.
set -euo pipefail
cd "$(dirname "$0")"
MANIFEST="../course/readings.tsv"
mkdir -p pdf web repos
UA="Mozilla/5.0 (agent-harness-101 study fetcher)"

# columns: key kind source file title authors year license read skip bibkey
tail -n +2 "$MANIFEST" | while IFS=$'\t' read -r key kind source file _rest; do
  case "$kind" in
    arxiv)
      out="pdf/$file.pdf"
      [[ -s "$out" ]] && { echo "have  $key $out"; continue; }
      if curl -fsSL -A "$UA" "https://arxiv.org/pdf/$source" -o "$out"; then echo "got   $key $out"; else echo "FAIL  $key $source"; rm -f "$out"; fi
      sleep 3  # be polite to arXiv
      ;;
    web)
      out="web/$file.html"
      [[ -s "$out" ]] && { echo "have  $key $out"; continue; }
      if curl -fsSL -A "$UA" "$source" -o "$out"; then echo "got   $key $out"; else echo "FAIL  $key $source (open the URL in a browser instead)"; rm -f "$out"; fi
      ;;
    repo)
      out="repos/$file"
      [[ -d "$out" ]] && { echo "have  $key $out"; continue; }
      if git clone --depth 1 -q "$source" "$out"; then echo "got   $key $out"; else echo "FAIL  $key $source"; fi
      ;;
  esac
done
echo "done. PDFs: $(ls pdf | wc -l | tr -d ' '), posts: $(ls web | wc -l | tr -d ' ')"
