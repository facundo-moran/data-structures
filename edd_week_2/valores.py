#4. Solicite al usuario el ingreso de un número entre 10 y 20. Si ingresa un número
# menor que 10 muestre el mensaje “Valor inferior” y solicite que intente
# nuevamente. Si el valor ingresado es superior a 20 muestre el mensaje “Valor
# superior” y solicite que intente nuevamente. Repita esta situación hasta que el
# valor ingresado sea válido, en dicho caso, muestre el mensaje: “Gracias!!!”


def app():
    num = input('Ingrese un numero entre 10 y 20: ')
    while(int(num) < 10 or int(num) > 20):
        print( 'Valor inferior' if int(num) < 10 else 'Valor superior')
        num = input('Ingrese un numero entre 10 y 20: ')
    print('Gracias')

if __name__ == "__main__":
    app()