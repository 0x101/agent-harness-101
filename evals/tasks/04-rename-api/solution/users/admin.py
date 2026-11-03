from users.core import get_user


def admin_name(uid):
    return get_user(uid)["name"]


def admin_exists(uid):
    try:
        get_user(uid)
        return True
    except KeyError:
        return False
