def locale_26_step_0(values, factor=4):
    """Helper 0 for locale_26. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def locale_26_step_1(values, factor=3):
    """Helper 1 for locale_26. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def locale_26_step_2(values, factor=7):
    """Helper 2 for locale_26. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out
