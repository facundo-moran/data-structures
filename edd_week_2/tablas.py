#1. Solicite al usuario el ingreso de un número entero entre 1 y 12 y muestre por pantalla las tablas de multiplicación del 1 al 10

def get_tabla_10(num):
    table = list(range(10))

    for n in range(len(table)):
        table[n] = num*(n+1)

    return table


def app():
    entero = input('Ingrese entero entre 1 y 12: ')
    tabla = get_tabla_10(int(entero))
    for n in range(len(tabla)):
        print(f'{entero} x {n+1} = {tabla[n]}')


if __name__ == "__main__":
    app()
