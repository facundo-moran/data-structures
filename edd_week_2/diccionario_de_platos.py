# 9 Solicite al usuario que ingrese por consola de comandos sus cuatro platos favoritos
# y almacénelos en un diccionario de manera que sean indexados con números a
# partir del 1. Muestre por pantalla el diccionario completo (claves y valores). A
# continuación el programa deberá preguntar al usuario qué elemento quiere quitar
# del diccionario y hacerlo. Muestre por pantalla el resultado final.


def int_generator() -> int:
    first = 1

    while True:
        yield first
        first = first+1


def is_yes_or_no(asw: str) -> bool:
    asw = asw.lower().strip()
    return asw == 'yes' or asw == 'no'


def raise_on_false(val: bool) -> None:
    if not val:
        raise Exception


def app():
    print('Ingrese sus 4 platos favoritos: ')
    dishes = {}
    generador = int_generator()
    more_dishes = True

    try:
        while more_dishes:
            user_input = str(input('\nInsert favourite dish: \t'))

            raise_on_false(user_input.isalpha())

            dishes[next(generador)] = user_input.strip()

            if len(dishes) > 3:
                print(f'\nYour favourite dishes -> {dishes}')
                user_input = str(
                    input(f'\nDo you want to modify one of them? \tyes|no'))

                raise_on_false(is_yes_or_no(user_input))

                if user_input == 'no':
                    more_dishes = not more_dishes
                else:
                    user_input = str(
                        input(f'\nInsert index from 1 to {len(dishes)}: \t'))
                    raise_on_false(user_input.isnumeric())
                    dishes.pop(int(user_input))
                    print(f'\nYour favourite dishes -> {dishes}')

    except:
        print('Input not valid!')


if __name__ == "__main__":
    app()
