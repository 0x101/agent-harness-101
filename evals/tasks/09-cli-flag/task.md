Add a `--dry-run` flag to `cleanup.py`. With it, the tool prints
`would delete <path>` for each file it would remove, in sorted order, and deletes
nothing. Without it, behavior is unchanged.
