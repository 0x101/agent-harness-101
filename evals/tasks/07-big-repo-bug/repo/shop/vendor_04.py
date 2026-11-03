def vendor_04_step_0(values, factor=4):
    """Helper 0 for vendor_04. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def vendor_04_step_1(values, factor=6):
    """Helper 1 for vendor_04. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 6 == 0:
            continue
        out.append(v * factor)
    return out


def vendor_04_step_2(values, factor=8):
    """Helper 2 for vendor_04. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out
