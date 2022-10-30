# 10. Para facilitar el relevamiento de datos de la ropa de trabajo de una empresa, se le
# solicita un programa que permita cargar para cada empleado los siguientes datos


class Empleado:
    def __init__(self) -> None:
        self.legajo: int
        self.apellido: str
        self.nombre: str
        self.talle_camisa: int
        self.talle_pantalon: int
        self.zapatos_seguridad: bool

    def __str__(self) -> str:
        return f"Marcacion {self.legajo} {self.apellido} {self.nombre} {self.talle_camisa} {self.talle_pantalon} {self.zapatos_seguridad}"


def app():
    empleados = list()

    print('start:')
    print(f'\t{empleados}')

    emp_marcelo = Empleado()
    emp_marcelo.legajo = 1
    emp_marcelo.apellido = 'Miranda'
    emp_marcelo.nombre = 'Marcelo'
    emp_marcelo.talle_camisa = '4'
    emp_marcelo.talle_pantalon = '45'
    emp_marcelo.zapatos_seguridad = True

    emp_marcela = Empleado()
    emp_marcela.legajo = 2
    emp_marcela.apellido = 'Mirinda'
    emp_marcela.nombre = 'Marcela'
    emp_marcela.talle_camisa = '2'
    emp_marcela.talle_pantalon = '40'
    emp_marcela.zapatos_seguridad = False

    emp_ana = Empleado()
    emp_ana.legajo = 3
    emp_ana.apellido = 'Ana'
    emp_ana.nombre = 'Ayala'
    emp_ana.talle_camisa = '2'
    emp_ana.talle_pantalon = '38'
    emp_ana.zapatos_seguridad = True

    empleados.append(emp_marcela)
    empleados.append(emp_marcelo)
    empleados.append(emp_ana)

    print('add:')
    for emp in empleados:
        print(f'\t{emp}')

    print('sorted by legajo:')
    empleados.sort(key=lambda em: em.legajo)
    for emp in empleados:
        print(f'\t{emp}')

    print('sorted by apellido and nombre:')
    empleados.sort(key=lambda em: em.apellido)
    empleados.sort(key=lambda em: em.nombre)
    for emp in empleados:
        print(f'\t{emp}')


if __name__ == "__main__":
    app()
