# 6. Defina colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta', 'Rosa',
# 'Negro', 'Celeste', 'Gris', 'Blanco']. Solicite al usuario el ingreso del número
# entero inicio con valor entre 0 y 4 y del número entero fin entre 5 y 9. Muestre la
# sublista formada por los colores entre los números inicio y fin.


def app():
    colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta',
               'Rosa', 'Negro', 'Celeste', 'Gris', 'Blanco']
    inicio = int(input('Ingrese entero entre 0 y 4: '))
    fin = int(input('Ingrese entero entre 5 y 9: '))
    print('sublista generada: ', colores[inicio:fin])


if __name__ == "__main__":
    app()
