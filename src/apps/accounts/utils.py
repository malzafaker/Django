from django.utils.crypto import get_random_string


def get_password_random():
    passwd_random = get_random_string(
        length=10,
        allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ123456789'
    )
    return passwd_random
