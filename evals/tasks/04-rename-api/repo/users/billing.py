from users.core import get_usr


def billing_name(uid):
    return get_usr(uid)["name"]


def billing_exists(uid):
    try:
        get_usr(uid)
        return True
    except KeyError:
        return False
