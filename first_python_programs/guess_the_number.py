import random


def app():
    num_ale = random.randint(1, 100)
    num_chosen = int(input('Insert integer between 1 - 100: '))

    while num_chosen != num_ale:
        rsp = "\Insert a smaller number" if num_ale < num_chosen else "\tinsert a bigger number"
        print(rsp)
        num_chosen = int(input('Insert integer between 1 - 100: '))

    print('\Congrats! The number is ' + str(num_ale))


# entrypoint
if __name__ == '__main__':
    app()
