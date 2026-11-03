def currency_12_step_0(values, factor=7):
    """Helper 0 for currency_12. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def currency_12_step_1(values, factor=7):
    """Helper 1 for currency_12. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def currency_12_step_2(values, factor=9):
    """Helper 2 for currency_12. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def currency_12_step_3(values, factor=9):
    """Helper 3 for currency_12. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def currency_12_step_4(values, factor=3):
    """Helper 4 for currency_12. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
