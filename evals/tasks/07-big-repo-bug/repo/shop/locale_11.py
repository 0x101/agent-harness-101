def locale_11_step_0(values, factor=9):
    """Helper 0 for locale_11. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def locale_11_step_1(values, factor=8):
    """Helper 1 for locale_11. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def locale_11_step_2(values, factor=2):
    """Helper 2 for locale_11. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def locale_11_step_3(values, factor=3):
    """Helper 3 for locale_11. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
