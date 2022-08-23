#1 Solicite al usuario su nombre y muestre por pantalla el mensaje: Hola [nombre]

def greeting(name):
    return f'Hola {name}'


def app():
    name = input('📌 Ingrese su nombre: ')
    print(greeting(name))


if __name__ == '__main__':
    app()
