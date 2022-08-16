# Solicite al usuario el ingreso de dos números, los sume y luego los muestre porpantalla diciendo: El total es [resultado].

def suma(num1, num2):
    num1 = int(num1)
    num2 = int(num2)

    return num1+num2


def app():
    num1 = input('📌 Ingrese un numero: ')
    num2 = input('📌 Ingrese otro numero: ')
    salida = f'\nEl total es {suma(num1,num2)}'
    print(salida)


app()

# Solicite al usuario que ingrese tres números, sume los dos primeros y multiplique lasumatoria por el tercero. Muestre por pantalla: El resultado es [resultado].