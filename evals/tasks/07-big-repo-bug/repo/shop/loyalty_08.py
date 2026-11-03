def loyalty_08_step_0(values, factor=7):
    """Helper 0 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_08_step_1(values, factor=6):
    """Helper 1 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 6 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_08_step_2(values, factor=5):
    """Helper 2 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_08_step_3(values, factor=4):
    """Helper 3 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_08_step_4(values, factor=5):
    """Helper 4 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_08_step_5(values, factor=3):
    """Helper 5 for loyalty_08. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
