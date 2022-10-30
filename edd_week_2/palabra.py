#3. Pida al usuario que ingrese una palabra por consola de comandos y muestre en
# orden inverso los caracteres que la forman, uno por línea.


def app():
    palabra = input('Ingrese una palabra: ')
    palabra = palabra[::-1]
    for n in range(len(palabra)):
        print(palabra[n])

if __name__ == "__main__":
    app()
