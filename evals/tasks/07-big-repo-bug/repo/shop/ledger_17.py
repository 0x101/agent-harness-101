def ledger_17_step_0(values, factor=9):
    """Helper 0 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_17_step_1(values, factor=3):
    """Helper 1 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_17_step_2(values, factor=4):
    """Helper 2 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_17_step_3(values, factor=9):
    """Helper 3 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 9 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_17_step_4(values, factor=8):
    """Helper 4 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_17_step_5(values, factor=6):
    """Helper 5 for ledger_17. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 6 == 0:
            continue
        out.append(v * factor)
    return out
