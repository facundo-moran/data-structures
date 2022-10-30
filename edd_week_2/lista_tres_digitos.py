#7. Cree una lista formada por cuatro elementos de tres dígitos y muestre esa lista al
# usuario (un número por línea). Solicite al usuario el ingreso de otro número de tres
# dígitos. Si el número ingresado forma parte de la lista, muestre la posición en la
# lista que ocupa ese número. En caso contrario muestre el mensaje: “El valor
# ingresado no es parte de la lista”.


from operator import indexOf


def app():
    lista_tres_digitos = [154, 956, 673, 654]

    print('Mira esta lista: ')
    for n in range(len(lista_tres_digitos)):
        print(lista_tres_digitos[n])

    num_tres_digitos = int(input('Ingrese num de tres digitos: '))

    print(lista_tres_digitos.index(num_tres_digitos)
          if num_tres_digitos in lista_tres_digitos else 'El valor ingresado no es parte de la lista')


if __name__ == "__main__":
    app()
