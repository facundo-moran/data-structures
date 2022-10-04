from datetime import datetime, time

from modelos.MarcacionTipo import MarcacionTipo
from modelos.MarcacionesAdmin import MarcacionesAdmin
from modelos.Oficina import Oficina
from modelos.Empleado import Empleado
from modelos.Marcacion import Marcacion


def app():
    # init
    marcaciones = list()
    marcaciones_admin = MarcacionesAdmin()

    # 3 oficinas
    ofi_sistemas_entrada = time(8, 0, 0)
    ofi_sistemas_salida = time(15, 0, 0)
    ofi_sistemas = Oficina(
        "sistemas", ofi_sistemas_entrada, ofi_sistemas_salida)

    ofi_administracion_entrada = time(9, 0, 0)
    ofi_administracion_salida = time(16, 0, 0)
    ofi_administracion = Oficina(
        "administracion", ofi_administracion_entrada, ofi_administracion_salida)

    ofi_gerencia_entrada = time(7, 0, 0)
    ofi_gerencia_salida = time(13, 0, 0)
    ofi_gerencia = Oficina(
        "administracion", ofi_gerencia_entrada, ofi_gerencia_salida)

    # 5 empleados
    juan_emp = Empleado(1, '11111111', "Juan", "Perez", ofi_sistemas)
    malin_emp = Empleado(2, '22222222', "Malin", "Melen", ofi_administracion)
    maria_emp = Empleado(3, '33333333', "Maria", "Mazzola", ofi_gerencia)
    mikey_emp = Empleado(4, '44444444', "Mikey", "Mouse", ofi_gerencia)
    harry_emp = Empleado(5, '55555555', "Harry", "Potter", ofi_sistemas)

    # fechas de marcaciones entrada
    fecha_marcacion_entrada_1 = datetime(2022, 1, 1, 9, 0, 0, 0)
    fecha_marcacion_entrada_2 = datetime(2022, 1, 1, 7, 5, 0, 0)
    fecha_marcacion_entrada_3 = datetime(2022, 1, 1, 7, 0, 0, 0)
    fecha_marcacion_entrada_4 = datetime(2022, 1, 1, 8, 0, 0, 0)
    fecha_marcacion_entrada_5 = datetime(2022, 1, 1, 9, 2, 0, 0)
    fecha_marcacion_entrada_7 = datetime(2022, 1, 1, 7, 10, 0, 0)
    fecha_marcacion_entrada_8 = datetime(2022, 1, 1, 8, 4, 0, 0)
    fecha_marcacion_entrada_9 = datetime(2022, 1, 1, 8, 0, 0, 0)
    fecha_marcacion_entrada_10 = datetime(2022, 1, 1, 8, 22, 0, 0)

    # fechas de marcaciones salida
    fecha_marcacion_salida_1 = datetime(2022, 1, 1, 9, 0, 0, 0)
    fecha_marcacion_salida_2 = datetime(2022, 1, 1, 7, 0, 0, 0)
    fecha_marcacion_salida_3 = datetime(2022, 1, 1, 8, 0, 0, 0)
    
    # marcaciones juan
    marcacion_entrada_juan_1 = Marcacion(juan_emp, fecha_marcacion_entrada_4, MarcacionTipo.ENTRADA)
    marcacion_entrada_juan_2 = Marcacion(juan_emp, fecha_marcacion_entrada_8, MarcacionTipo.ENTRADA)
    marcacion_entrada_juan_3 = Marcacion(juan_emp, fecha_marcacion_entrada_9, MarcacionTipo.ENTRADA)
    marcacion_entrada_juan_4 = Marcacion(juan_emp, fecha_marcacion_entrada_9, MarcacionTipo.ENTRADA)
    marcacion_entrada_juan_5 = Marcacion(juan_emp, fecha_marcacion_entrada_10, MarcacionTipo.ENTRADA)
    
    marcacion_salida_juan_1 = Marcacion(juan_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_juan_2 = Marcacion(juan_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_juan_3 = Marcacion(juan_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_juan_4 = Marcacion(juan_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_juan_5 = Marcacion(juan_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)

    marcaciones_de_juan = [
        marcacion_entrada_juan_1,
        marcacion_entrada_juan_2,
        marcacion_entrada_juan_3,
        marcacion_entrada_juan_4,
        marcacion_entrada_juan_5,
        marcacion_salida_juan_1,
        marcacion_salida_juan_2,
        marcacion_salida_juan_3,
        marcacion_salida_juan_4,
        marcacion_salida_juan_5]

    marcaciones.extend(marcaciones_de_juan)

    # marcaciones malin
    marcacion_entrada_malin_1 = Marcacion(malin_emp, fecha_marcacion_entrada_1, MarcacionTipo.ENTRADA)
    marcacion_entrada_malin_2 = Marcacion(malin_emp, fecha_marcacion_entrada_1, MarcacionTipo.ENTRADA)
    marcacion_entrada_malin_3 = Marcacion(malin_emp, fecha_marcacion_entrada_5, MarcacionTipo.ENTRADA)
    marcacion_entrada_malin_4 = Marcacion(malin_emp, fecha_marcacion_entrada_1, MarcacionTipo.ENTRADA)
    marcacion_entrada_malin_5 = Marcacion(malin_emp, fecha_marcacion_entrada_5, MarcacionTipo.ENTRADA)
    
    marcacion_salida_malin_1 = Marcacion(malin_emp, fecha_marcacion_salida_1, MarcacionTipo.SALIDA)
    marcacion_salida_malin_2 = Marcacion(malin_emp, fecha_marcacion_salida_1, MarcacionTipo.SALIDA)
    marcacion_salida_malin_3 = Marcacion(malin_emp, fecha_marcacion_salida_1, MarcacionTipo.SALIDA)
    marcacion_salida_malin_4 = Marcacion(malin_emp, fecha_marcacion_salida_1, MarcacionTipo.SALIDA)
    marcacion_salida_malin_5 = Marcacion(malin_emp, fecha_marcacion_salida_1, MarcacionTipo.SALIDA)

    marcaciones_de_malin = [
        marcacion_entrada_malin_1,
        marcacion_entrada_malin_2,
        marcacion_entrada_malin_3,
        marcacion_entrada_malin_4,
        marcacion_entrada_malin_5,
        marcacion_salida_malin_1,
        marcacion_salida_malin_2,
        marcacion_salida_malin_3,
        marcacion_salida_malin_4,
        marcacion_salida_malin_5]

    marcaciones.extend(marcaciones_de_malin)

    # marcaciones maria
    marcacion_entrada_maria_1 = Marcacion(maria_emp, fecha_marcacion_entrada_2, MarcacionTipo.ENTRADA)
    marcacion_entrada_maria_2 = Marcacion(maria_emp, fecha_marcacion_entrada_3, MarcacionTipo.ENTRADA)
    marcacion_entrada_maria_3 = Marcacion(maria_emp, fecha_marcacion_entrada_3, MarcacionTipo.ENTRADA)
    marcacion_entrada_maria_4 = Marcacion(maria_emp, fecha_marcacion_entrada_3, MarcacionTipo.ENTRADA)
    marcacion_entrada_maria_5 = Marcacion(maria_emp, fecha_marcacion_entrada_7, MarcacionTipo.ENTRADA)
    
    marcacion_salida_maria_1 = Marcacion(maria_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_maria_2 = Marcacion(maria_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_maria_3 = Marcacion(maria_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_maria_4 = Marcacion(maria_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_maria_5 = Marcacion(maria_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)

    marcaciones_de_maria = [
        marcacion_entrada_maria_1,
        marcacion_entrada_maria_2,
        marcacion_entrada_maria_3,
        marcacion_entrada_maria_4,
        marcacion_entrada_maria_5,
        marcacion_salida_maria_1,
        marcacion_salida_maria_2,
        marcacion_salida_maria_3,
        marcacion_salida_maria_4,
        marcacion_salida_maria_5]

    marcaciones.extend(marcaciones_de_maria)

    # marcaciones mikey
    marcacion_entrada_mikey_1 = Marcacion(mikey_emp, fecha_marcacion_entrada_3, MarcacionTipo.ENTRADA)
    marcacion_entrada_mikey_2 = Marcacion(mikey_emp, fecha_marcacion_entrada_2, MarcacionTipo.ENTRADA)
    marcacion_entrada_mikey_3 = Marcacion(mikey_emp, fecha_marcacion_entrada_7, MarcacionTipo.ENTRADA)
    marcacion_entrada_mikey_4 = Marcacion(mikey_emp, fecha_marcacion_entrada_7, MarcacionTipo.ENTRADA)
    marcacion_entrada_mikey_5 = Marcacion(mikey_emp, fecha_marcacion_entrada_2, MarcacionTipo.ENTRADA)
    
    marcacion_salida_mikey_1 = Marcacion(mikey_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_mikey_2 = Marcacion(mikey_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_mikey_3 = Marcacion(mikey_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_mikey_4 = Marcacion(mikey_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)
    marcacion_salida_mikey_5 = Marcacion(mikey_emp, fecha_marcacion_salida_2, MarcacionTipo.SALIDA)

    marcaciones_de_mikey = [
        marcacion_entrada_mikey_1,
        marcacion_entrada_mikey_2,
        marcacion_entrada_mikey_3,
        marcacion_entrada_mikey_4,
        marcacion_entrada_mikey_5,
        marcacion_salida_mikey_1,
        marcacion_salida_mikey_2,
        marcacion_salida_mikey_3,
        marcacion_salida_mikey_4,
        marcacion_salida_mikey_5]

    marcaciones.extend(marcaciones_de_mikey)

    # marcaciones harry
    marcacion_entrada_harry_1 = Marcacion(harry_emp, fecha_marcacion_entrada_9, MarcacionTipo.ENTRADA)
    marcacion_entrada_harry_2 = Marcacion(harry_emp, fecha_marcacion_entrada_9, MarcacionTipo.ENTRADA)
    marcacion_entrada_harry_3 = Marcacion(harry_emp, fecha_marcacion_entrada_4, MarcacionTipo.ENTRADA)
    marcacion_entrada_harry_4 = Marcacion(harry_emp, fecha_marcacion_entrada_9, MarcacionTipo.ENTRADA)
    marcacion_entrada_harry_5 = Marcacion(harry_emp, fecha_marcacion_entrada_10, MarcacionTipo.ENTRADA)
    

    marcacion_salida_harry_1 = Marcacion(harry_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_harry_2 = Marcacion(harry_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_harry_3 = Marcacion(harry_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_harry_4 = Marcacion(harry_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)
    marcacion_salida_harry_5 = Marcacion(harry_emp, fecha_marcacion_salida_3, MarcacionTipo.SALIDA)

    marcaciones_de_harry= [
        marcacion_entrada_harry_1,
        marcacion_entrada_harry_2,
        marcacion_entrada_harry_3,
        marcacion_entrada_harry_4,
        marcacion_entrada_harry_5,
        marcacion_salida_harry_1,
        marcacion_salida_harry_2,
        marcacion_salida_harry_3,
        marcacion_salida_harry_4,
        marcacion_salida_harry_5]

    marcaciones.extend(marcaciones_de_harry)
    marcaciones_admin.marcaciones = marcaciones

    print(f"admin len: {marcaciones_admin.__len__()} \n")
    print(f"admin get item: \n")
    print(f"admin del item: \n")
    print(f"admin str \n")
    
    print(f"\nadmin empleados: \n")
    for emp in marcaciones_admin.empleados():
        print(f'\n\temp: {emp}')
    
    print(f"\nfiltrar_por_empleado: \n")
    for marca in marcaciones_admin.filtrar_por_empleado(mikey_emp):
        print(f'\n\tde {mikey_emp.nombre}: {marca}')
    
    print(f"\nfiltrar_por_tipo: \n")
    for marca in marcaciones_admin.filtrar_por_tipo(MarcacionTipo.ENTRADA):
        print(f'\n\tmarca {MarcacionTipo.ENTRADA}: {marca}')

    print(f"\nllegadas_tarde: \n")
    for marca in marcaciones_admin.llegadas_tarde():
        print(f'\n\marca tarde: {marca}')
    print(f"\n")

    print(f"\nmarcaciones original: \n")
    for marca in marcaciones_admin.marcaciones:
        print(f'{marca}\n\t')

    print(f"\nordenar_legajo: \n")
    marcaciones_admin.ordenar_legajo()
    for marca in marcaciones_admin.marcaciones:
        print(f'{marca}\n\t')

    print(f"\nordenar_apellido_nombre: \n")
    marcaciones_admin.ordenar_apellido_nombre()
    for marca in marcaciones_admin.marcaciones:
        print(f'{marca}\n\t')
    

if __name__ == "__main__":
    app()
