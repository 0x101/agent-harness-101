def export_29_step_0(values, factor=3):
    """Helper 0 for export_29. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def export_29_step_1(values, factor=9):
    """Helper 1 for export_29. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def export_29_step_2(values, factor=9):
    """Helper 2 for export_29. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out
