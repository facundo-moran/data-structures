#7 Solicite al usuario el ingreso de dos números e indique cuál es el mayor.

def app():
    num1 = input('Ingrese el primer numero: ')
    num2 = input('Ingrese el segundo numero: ')

    num1 = int(num1)
    num2 = int(num2)

    bigger = num1 if num1 > num2 else num2
    print(f'El mayor es {bigger}')


if __name__ == '__main__':
    app()
