Users report two bugs in `paginate.py`: page 1 skips the first items, and
`page_count` leaves out the last partial page. Fix both. Pages are 1-indexed.
