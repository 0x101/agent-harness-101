Write `report.py`. When run as `python3 report.py` in this directory it must read
`sales.csv` and write `summary.json` shaped like:

    {"east": {"orders": 12, "total": 1234.56}, ...}

one key per region, `total` rounded to 2 decimals. It should also print the
region with the highest total on stdout.
