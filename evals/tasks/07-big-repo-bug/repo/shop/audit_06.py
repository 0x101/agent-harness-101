def audit_06_step_0(values, factor=7):
    """Helper 0 for audit_06. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def audit_06_step_1(values, factor=3):
    """Helper 1 for audit_06. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def audit_06_step_2(values, factor=3):
    """Helper 2 for audit_06. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 3 == 0:
            continue
        out.append(v * factor)
    return out


def audit_06_step_3(values, factor=2):
    """Helper 3 for audit_06. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out
