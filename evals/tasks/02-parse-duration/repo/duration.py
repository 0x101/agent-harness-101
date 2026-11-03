def parse_duration(text):
    """Parse a human duration into whole seconds.

    Spec:
      - Units: d (86400), h (3600), m (60), s (1). Example: "1h30m" -> 5400.
      - Parts may be separated by spaces: "2h 5s" -> 7205.
      - Units must appear in descending order and at most once: "5m1h" is invalid.
      - A bare integer means seconds: "90" -> 90.
      - Leading/trailing whitespace is ignored.
      - Anything else (empty string, unknown unit, negative numbers, decimals)
        raises ValueError.
    """
    raise NotImplementedError
