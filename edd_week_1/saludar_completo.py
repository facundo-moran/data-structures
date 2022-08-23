#2 Solicite al usuario su nombre y apellido, luego, muestre por pantalla el mensaje: Hola[nombre] [apellido].

def greeting(name, surname):
    return f'Hola {name} {surname}'


def app():
    surname = input('📌 Ingrese su apellido: ')
    name = input('📌 Ingrese su nombre: ')
    print(greeting(name, surname))


if __name__ == '__main__':
    app()
