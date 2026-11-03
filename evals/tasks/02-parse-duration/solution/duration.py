import re

UNITS = [("d", 86400), ("h", 3600), ("m", 60), ("s", 1)]


def parse_duration(text):
    """Parse a human duration into whole seconds. See tests for the spec."""
    s = text.strip()
    if re.fullmatch(r"\d+", s):
        return int(s)
    parts = re.findall(r"(\d+)([dhms])\s*", s)
    if not parts or "".join(f"{n}{u}" for n, u in parts) != re.sub(r"\s+", "", s):
        raise ValueError(text)
    order = [u for u, _ in UNITS]
    idx = [order.index(u) for _, u in parts]
    if idx != sorted(set(idx)):
        raise ValueError(text)
    mult = dict(UNITS)
    return sum(int(n) * mult[u] for n, u in parts)
