import argparse, os, time


def old_files(directory, days):
    cutoff = time.time() - days * 86400
    for name in sorted(os.listdir(directory)):
        path = os.path.join(directory, name)
        if os.path.isfile(path) and os.path.getmtime(path) < cutoff:
            yield path


def main(argv=None):
    ap = argparse.ArgumentParser(description="Delete files older than N days.")
    ap.add_argument("directory")
    ap.add_argument("--days", type=int, default=30)
    args = ap.parse_args(argv)
    for path in old_files(args.directory, args.days):
        os.remove(path)
        print(f"deleted {path}")


if __name__ == "__main__":
    main()
