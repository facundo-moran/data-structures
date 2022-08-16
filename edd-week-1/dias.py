# Pregunte al usuario por un número de días y calcule la cantidad de horas, minutos ysegundos que transcurren en ese número de días.

def calcular_unidad_temporal(tiempo=1, unidad=1):
    tiempo = int(tiempo)
    unidad = int(unidad)
    return tiempo * unidad


def imprimir_tiempo(cant_dias, cant_unidad_tiempo, unidad_tiempo):
    return f'\nEn {cant_dias} dias transcurrieron {cant_unidad_tiempo} {unidad_tiempo}.'


def app():
    cant_dias = input('Ingrese un numero de dias aleatorio: ')

    cant_horas = calcular_unidad_temporal(cant_dias,24)
    print(imprimir_tiempo(cant_dias, cant_horas, 'horas'))

    cant_minutos = calcular_unidad_temporal(cant_horas,60)
    print(imprimir_tiempo(cant_dias, cant_minutos, 'minutos'))

    cant_segundos = calcular_unidad_temporal(cant_minutos,60)
    print(imprimir_tiempo(cant_dias, cant_segundos, 'segundos'))

app()

# Solicite al usuario el ingreso de dos números e indique cuál es el mayor.