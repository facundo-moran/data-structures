# 5. Escriba un programa Python realice su cometido invocando a las siguientes funciones:
#    a) Solicita al usuario dos números enteros para usar como límite inferior y otro
#   superior y genera un número aleatorio entre esos dos números.
#    b) Imprime por pantalla el mensaje: “Estoy pensando en el número…” y pide al
#   usuario adivinar ese número.
#    c) Controla que el número aleatorio es el mismo que el ingresado por el usuario y
#   si es así, muestra por pantalla el mensaje: “Correcto, has ganado!!”, en caso
#   contrario se ejecuta iterativamente indicando al usuario que el número
#   ingresado es mayor o menor y vuelve a solicitar el ingreso hasta que el número
#   es adivinado.


from random import randint


def generar_numero_aleatorio(lim_inf, lim_sup):
    lim_inf = lim_inf if lim_inf < lim_sup else lim_sup
    lim_sup = lim_sup if lim_sup > lim_inf else lim_inf

    return randint(lim_inf, lim_sup)


def app():
    lim_inf = int(input('Ingrese limite inferior (numero): '))
    lim_sup = int(input('Ingrese limite superior (numero): '))

    num_ale = generar_numero_aleatorio(lim_inf, lim_sup)

    print('Estoy pensando en el numero...')
    num_elegido = int(input('Adivina el numero: '))

    while num_elegido != num_ale:
        rsp = "\tIngresa un numero mas chico" if num_ale < num_elegido else "\tIngresa un numero mas grande"
        print(rsp)
        num_elegido = int(input('Adivina el numero: '))

    print('\nCorrecto, has ganado!! ' + str(num_ale))


if __name__ == "__main__":
    app()
