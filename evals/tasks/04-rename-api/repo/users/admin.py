from users.core import get_usr


def admin_name(uid):
    return get_usr(uid)["name"]


def admin_exists(uid):
    try:
        get_usr(uid)
        return True
    except KeyError:
        return False
