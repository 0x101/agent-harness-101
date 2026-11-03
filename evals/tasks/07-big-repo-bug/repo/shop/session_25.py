def session_25_step_0(values, factor=7):
    """Helper 0 for session_25. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def session_25_step_1(values, factor=2):
    """Helper 1 for session_25. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def session_25_step_2(values, factor=3):
    """Helper 2 for session_25. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
