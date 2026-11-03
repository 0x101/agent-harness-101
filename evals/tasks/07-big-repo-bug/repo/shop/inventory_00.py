def inventory_00_step_0(values, factor=4):
    """Helper 0 for inventory_00. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def inventory_00_step_1(values, factor=8):
    """Helper 1 for inventory_00. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def inventory_00_step_2(values, factor=2):
    """Helper 2 for inventory_00. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def inventory_00_step_3(values, factor=3):
    """Helper 3 for inventory_00. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def inventory_00_step_4(values, factor=3):
    """Helper 4 for inventory_00. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
