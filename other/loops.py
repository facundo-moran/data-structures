

def app():
    name = input("Insert your first name: ").replace(' ', '')

    for ch in name:
        print(ch)


def app_2():
    LIMIT = 1000

    for i in range(1, LIMIT+1):
        print(i)


def app_1():
    LIMIT= 1000

    count = 0
    squared = 0

    while squared < LIMIT:
        count = count + 2
        squared = 2**count
        print('2 ** ' + str(count) +
              ' equal to: ' + str(squared))


if __name__ == '__main__':
    app()
