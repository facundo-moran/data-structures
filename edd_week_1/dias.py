#6 Pregunte al usuario por un número de días y calcule la cantidad de horas, minutos ysegundos que transcurren en ese número de días.

def calc_temporal_unit(time, unit):
    time = int(time)
    unit = int(unit)
    return time * unit


def print_time(days, time_units, time_unit_str):
    return f'\nEn {days} dias transcurrieron {time_units} {time_unit_str}.'


def app():
    days = input('Ingrese un numero de dias aleatorio: ')

    hours = calc_temporal_unit(days, 24)
    print(print_time(days, hours, 'horas'))

    minutes = calc_temporal_unit(hours, 60)
    print(print_time(days, minutes, 'minutos'))

    seconds = calc_temporal_unit(minutes, 60)
    print(print_time(days, seconds, 'segundos'))


if __name__ == '__main__':
    app()
