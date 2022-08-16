# Solicite al usuario el ingreso de dos números e indique cuál es el mayor.

def app():
    num1 = input('Ingrese el primer numero: ')
    num2 = input('Ingrese el segundo numero: ')

    num1 = int(num1)
    num2 = int(num2)

    mayor = num1 if num1 > num2 else num2
    print(f'El mayor es {mayor}')


app()
