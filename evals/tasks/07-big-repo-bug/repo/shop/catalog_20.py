def catalog_20_step_0(values, factor=2):
    """Helper 0 for catalog_20. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def catalog_20_step_1(values, factor=9):
    """Helper 1 for catalog_20. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def catalog_20_step_2(values, factor=4):
    """Helper 2 for catalog_20. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def catalog_20_step_3(values, factor=6):
    """Helper 3 for catalog_20. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 6 == 0:
            continue
        out.append(v * factor)
    return out
