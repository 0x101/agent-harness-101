Write `migrate.py`. Running `python3 migrate.py` must read `config.ini` and write
`config.json`. Rules:

- Dotted section names nest: `[database.primary]` becomes `{"database": {"primary": {...}}}`.
- Values that are integers become ints; `true`/`false`/`yes`/`no` (any case) become booleans;
  everything else stays a string.
