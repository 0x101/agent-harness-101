from users.core import get_user


def billing_name(uid):
    return get_user(uid)["name"]


def billing_exists(uid):
    try:
        get_user(uid)
        return True
    except KeyError:
        return False
