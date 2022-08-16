# Solicite al usuario el ingreso de tres números e indique cuál es el mayor.

def app():
    num1 = input('Ingrese el primer numero: ')
    num2 = input('Ingrese el segundo numero: ')
    num3 = input('Ingrese el tercer numero: ')

    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    mayor = num1 if num1 > num2 else num2
    mayor = mayor if mayor > num3 else num3
    
    print(f'El mayor es {mayor}')


app()
