
from datetime import datetime, time
from modelos.MarcacionTipo import MarcacionTipo
from modelos.Empleado import Empleado
from modelos.abstract.MarcacionesAdminAbstract import MarcacionesAdminAbstract
from modelos.Marcacion import Marcacion


class MarcacionesAdmin(MarcacionesAdminAbstract):

    def agregar(self, marcacion: Marcacion) -> None:
        self.marcaciones.append(marcacion)

    def empleados(self) -> list:
        empleados = set()
        for marca in self.marcaciones:
            empleados.add(marca.empleado)

        return list(empleados)

    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        marcaciones = list(filter(lambda m: m.empleado ==
                           empleado, self.marcaciones))

        return marcaciones

    def filtrar_por_tipo(self, tipo: MarcacionTipo) -> list:
        marcaciones = list(filter(lambda m: m.tipo == tipo, self.marcaciones))

        return marcaciones

    def llegadas_tarde(self) -> list:

        marcaciones = list(filter(lambda marca: datetime.strptime(
            marca.fecha_hora, '%d/%m/%Y %H:%M:%S').strftime('%H:%M:%S') > marca.empleado.oficina.hora_entrada, self.marcaciones))

        return marcaciones

    def ordenar_legajo(self) -> None:
        self.marcaciones.sort(key=lambda m: {m.empleado.legajo, m.fecha_hora})

    def ordenar_apellido_nombre(self) -> None:
        self.marcaciones.sort(key=lambda m: {m.empleado.apellido, m.empleado.nombre, m.fecha_hora})