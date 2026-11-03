def invoice_24_step_0(values, factor=5):
    """Helper 0 for invoice_24. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def invoice_24_step_1(values, factor=9):
    """Helper 1 for invoice_24. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def invoice_24_step_2(values, factor=4):
    """Helper 2 for invoice_24. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out
