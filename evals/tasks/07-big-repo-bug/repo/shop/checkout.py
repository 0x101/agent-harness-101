from shop import discounts

TAX = 0.08


def total(cart, code=None):
    subtotal = sum(price * qty for price, qty in cart)
    discounted = discounts.apply(code, subtotal)
    return round(discounted * (1 + TAX), 2)
