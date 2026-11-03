def audit_21_step_0(values, factor=2):
    """Helper 0 for audit_21. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 2 == 0:
            continue
        out.append(v * factor)
    return out


def audit_21_step_1(values, factor=4):
    """Helper 1 for audit_21. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 4 == 0:
            continue
        out.append(v * factor)
    return out


def audit_21_step_2(values, factor=8):
    """Helper 2 for audit_21. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 8 == 0:
            continue
        out.append(v * factor)
    return out


def audit_21_step_3(values, factor=7):
    """Helper 3 for audit_21. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out


def audit_21_step_4(values, factor=7):
    """Helper 4 for audit_21. Scales and filters a list of numbers."""
    out = []
    for v in values:
        if v % 7 == 0:
            continue
        out.append(v * factor)
    return out
