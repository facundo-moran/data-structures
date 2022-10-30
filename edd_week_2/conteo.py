# 2. Escriba un programa que pregunte al usuario en qué dirección quiere iniciar un
# conteo (ascedente ó descendente | asc ó desc). Si selecciona ascendente, luego
# solicite el límite superior y luego cuente desde 1 a ese número. Si selecciona
# descendente, solicite el límite inferior (deberá ser un número menor que 20 y la
# cuenta descendente será desde 20 a ese número. Si ingresa otra cosa que no sea
# “ascendente” o “descendente” muestre por pantalla el mensaje: “Incorrecto. No
# se puede continuar”.


def app():
    print("En que direccion quiere iniciar un conteo? ascendente o descendente")
    direccion = input('ingrese \'ascendente\' o \'descencente\': ')

    if direccion == 'ascendente':
        limite_superior = input('Ingrese un numero para limite superior: ')
        for n in range(int(limite_superior)):
            print(f'contando {n+1}')
    elif direccion == 'descendente':
        limite_superior = input('Ingrese un numero menor a 20: ')
        for n in range(21-int(limite_superior)):
            print(f'contando {20-n}')
    else:
        print('Incorrecto. Nose puede continuar')


if __name__ == "__main__":
    app()
