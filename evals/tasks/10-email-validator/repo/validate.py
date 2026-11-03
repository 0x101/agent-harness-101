def is_valid_email(s):
    """Return True if s is a valid address under these rules, else False.

    - Exactly one "@".
    - Local part: letters, digits, and . _ + -  ; must not start or end with "."
      and must not contain "..".
    - Domain: two or more labels separated by "."; each label is letters, digits
      and "-", 1-63 chars, and must not start or end with "-".
    - The last label (TLD) is letters only, at least 2 chars.
    """
    raise NotImplementedError
