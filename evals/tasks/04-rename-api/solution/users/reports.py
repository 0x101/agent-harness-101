from users.core import get_user


def reports_name(uid):
    return get_user(uid)["name"]


def reports_exists(uid):
    try:
        get_user(uid)
        return True
    except KeyError:
        return False
