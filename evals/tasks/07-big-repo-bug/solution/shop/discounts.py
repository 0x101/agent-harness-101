CODES = {"WELCOME10": 10, "HALF": 50, "VIP25": 25}


def apply(code, subtotal):
    """Return the subtotal after applying a percentage discount code."""
    pct = CODES.get(code, 0)
    return subtotal - subtotal * (pct / 100)
