from users.core import get_usr


def emails_name(uid):
    return get_usr(uid)["name"]


def emails_exists(uid):
    try:
        get_usr(uid)
        return True
    except KeyError:
        return False
