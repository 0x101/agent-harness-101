def ledger_02_step_0(values, factor=3):
    """Helper 0 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_02_step_1(values, factor=5):
    """Helper 1 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 5 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_02_step_2(values, factor=3):
    """Helper 2 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_02_step_3(values, factor=8):
    """Helper 3 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_02_step_4(values, factor=2):
    """Helper 4 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def ledger_02_step_5(values, factor=3):
    """Helper 5 for ledger_02. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out
