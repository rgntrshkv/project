import random

SECRET_KEY_LENGTH = 66
BAD_SYMBOLS = [34, 39, 46, 61, 96]


def generate_random_symbol():
    """Генерация кода символа в ASCII кодировке в диапазоне (33, 126),
     за исключением BAD_SYMBOLS, т.е. пробелов, кавычек"""
    z = random.randint(33, 126)
    return random.randint(33, 126) if z not in BAD_SYMBOLS else generate_random_symbol()


def generate_secret_key():
    return ''.join([chr(generate_random_symbol()) for _ in range(SECRET_KEY_LENGTH)])
