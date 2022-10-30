def print_if_prime(int_number):
    count = 0

    for i in range(1, int_number + 1):
        if not int_number % 2:
            count = count + 1

        return "\tis prime" if not count else "isnt prime"


def app():
    print('Prime numbers: ')
    for i in range(1, 101):
        print(str(print_if_prime(i)) + ':' + str(i))


if __name__ == '__main__':
    app()
