from ctypes.wintypes import CHAR
import random


def generate_password():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[',
             '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    CHARACTERS_ = MAYUS + MINUS + NUMS + CHARS
    password = []

    for i in range(15):
        random_char = random.choice(CHARACTERS_)
        password.append(random_char)

    return ''.join(password)


def app():
    password = generate_password()
    print('Your password is: ' + password)
    print('Please save it cause i usually dont use to do it')


if __name__ == '__main__':
    app()
