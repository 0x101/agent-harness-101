def session_10_step_0(values, factor=8):
    """Helper 0 for session_10. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def session_10_step_1(values, factor=4):
    """Helper 1 for session_10. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def session_10_step_2(values, factor=7):
    """Helper 2 for session_10. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out
