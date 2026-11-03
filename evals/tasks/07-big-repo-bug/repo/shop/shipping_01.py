def shipping_01_step_0(values, factor=2):
    """Helper 0 for shipping_01. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def shipping_01_step_1(values, factor=5):
    """Helper 1 for shipping_01. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def shipping_01_step_2(values, factor=2):
    """Helper 2 for shipping_01. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def shipping_01_step_3(values, factor=3):
    """Helper 3 for shipping_01. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def shipping_01_step_4(values, factor=8):
    """Helper 4 for shipping_01. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out
