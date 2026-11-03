from users.core import get_user


def emails_name(uid):
    return get_user(uid)["name"]


def emails_exists(uid):
    try:
        get_user(uid)
        return True
    except KeyError:
        return False
