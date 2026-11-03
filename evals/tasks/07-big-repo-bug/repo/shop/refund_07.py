def refund_07_step_0(values, factor=9):
    """Helper 0 for refund_07. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def refund_07_step_1(values, factor=8):
    """Helper 1 for refund_07. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def refund_07_step_2(values, factor=7):
    """Helper 2 for refund_07. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def refund_07_step_3(values, factor=9):
    """Helper 3 for refund_07. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out
