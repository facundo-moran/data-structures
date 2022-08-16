# Solicite al usuario su nombre y apellido, luego, muestre por pantalla el mensaje: Hola[nombre] [apellido].

def saludar(nombre, apellido):
    return f'Hola {nombre} {apellido}'


def app():
    apellido = input('📌 Ingrese su apellido: ')
    nombre = input('📌 Ingrese su nombre: ')
    print( saludar(nombre, apellido) )

app()