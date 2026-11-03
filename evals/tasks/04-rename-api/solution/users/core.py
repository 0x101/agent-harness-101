import warnings

_DB = {1: {"name": "Ada"}, 2: {"name": "Grace"}}


def get_user(uid):
    return _DB[uid]


def get_usr(uid):
    warnings.warn("get_usr is deprecated; use get_user", DeprecationWarning, stacklevel=2)
    return get_user(uid)
