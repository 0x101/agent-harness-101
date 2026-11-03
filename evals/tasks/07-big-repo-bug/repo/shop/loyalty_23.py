def loyalty_23_step_0(values, factor=8):
    """Helper 0 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_23_step_1(values, factor=3):
    """Helper 1 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_23_step_2(values, factor=9):
    """Helper 2 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_23_step_3(values, factor=8):
    """Helper 3 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_23_step_4(values, factor=2):
    """Helper 4 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def loyalty_23_step_5(values, factor=5):
    """Helper 5 for loyalty_23. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out
