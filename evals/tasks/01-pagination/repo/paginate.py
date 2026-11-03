def paginate(items, page, per_page):
    """Return the items on a 1-indexed page. Pages past the end return []."""
    start = page * per_page
    return items[start:start + per_page]


def page_count(n_items, per_page):
    """Number of pages needed to show n_items."""
    return n_items // per_page
