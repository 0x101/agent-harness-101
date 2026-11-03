from users.core import get_usr


def search_name(uid):
    return get_usr(uid)["name"]


def search_exists(uid):
    try:
        get_usr(uid)
        return True
    except KeyError:
        return False
