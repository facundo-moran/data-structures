# Solicite al usuario que ingrese tres números, sume los dos primeros y multiplique lasumatoria por el tercero. Muestre por pantalla: El resultado es [resultado].

def suma(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    return num1+num2

def app():
    sum1 = input('📌 Ingrese un numero: ')
    sum2 = input('📌 Ingrese otro numero: ')
    mul3 = input('📌 Ingrese el tercer numero: ')
    salida = f'\nEl resultado es {suma(sum1,sum2) * int(mul3)}'
    print(salida)


app()