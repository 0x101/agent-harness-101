def currency_27_step_0(values, factor=3):
    """Helper 0 for currency_27. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def currency_27_step_1(values, factor=5):
    """Helper 1 for currency_27. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def currency_27_step_2(values, factor=8):
    """Helper 2 for currency_27. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out
