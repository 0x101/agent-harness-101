def warehouse_28_step_0(values, factor=6):
    """Helper 0 for warehouse_28. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 6 == 0:
            continue
        out.append(v * factor)
    return out


def warehouse_28_step_1(values, factor=7):
    """Helper 1 for warehouse_28. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def warehouse_28_step_2(values, factor=7):
    """Helper 2 for warehouse_28. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def warehouse_28_step_3(values, factor=9):
    """Helper 3 for warehouse_28. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out
