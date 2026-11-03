from users.core import get_user


def search_name(uid):
    return get_user(uid)["name"]


def search_exists(uid):
    try:
        get_user(uid)
        return True
    except KeyError:
        return False
