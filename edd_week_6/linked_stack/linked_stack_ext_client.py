from linked_stack_ext import LinkedStackExt
from util import h1, h2


def linked_stack_ext_client():

    stack = LinkedStackExt()

    h1("LinkedStackExt")
    for i in range(1, 11):
        stack.push(i)

    print(stack, "\n")
    h2("Poniendo a prueba los metodos")

    print(("\n"), "Reemplazando los 1 por la palabra 'Hola'..")
    stack.replace_all(1, "hola")
    print(stack)

    print(("\n"), "Multiple pop de 100")
    print(stack.multi_pop(100), '\n')

    h1("LinkedStackExt")
    for i in range(1, 11):
        stack.push(i)
    print(stack)

    print(("\n"), "Multiple pop de 5")
    print(stack.multi_pop(5))

    h1("LinkedStackExt")
    for i in range(1, 11):
        stack.push(i)
    print(stack)

    print(("\n"), "Exchange'..")
    stack.exchange()
    print(stack)


if __name__ == '__main__':
    linked_stack_ext_client()
