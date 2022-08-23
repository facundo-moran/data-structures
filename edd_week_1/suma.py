#3 Solicite al usuario el ingreso de dos números, los sume y luego los muestre porpantalla diciendo: El total es [resultado].

def addition(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    return num1+num2


def app():
    num1 = input('📌 Ingrese un numero: ')
    num2 = input('📌 Ingrese otro numero: ')
    output = f'\nEl total es {addition(num1,num2)}'
    print(output)


if __name__ == '__main__':
    app()
