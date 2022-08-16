# Solicite al usuario su nombre y muestre por pantalla el mensaje: Hola [nombre]

def saludar(nombre):
    return f'Hola {nombre}'


def app():
    nombre = input('📌 Ingrese su nombre: ')
    print( saludar(nombre) )

app()