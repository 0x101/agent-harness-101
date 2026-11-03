import re

LOCAL = re.compile(r"[A-Za-z0-9._+-]+")
LABEL = re.compile(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?")


def is_valid_email(s):
    if s.count("@") != 1:
        return False
    local, domain = s.split("@")
    if not LOCAL.fullmatch(local) or local.startswith(".") or local.endswith(".") or ".." in local:
        return False
    labels = domain.split(".")
    if len(labels) < 2 or not all(LABEL.fullmatch(l) for l in labels):
        return False
    tld = labels[-1]
    return tld.isalpha() and len(tld) >= 2
