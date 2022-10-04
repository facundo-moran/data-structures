from datetime import datetime

from modelos.MarcacionTipo import MarcacionTipo
from modelos.Empleado import Empleado


class Marcacion:
    last_record: int = 0

    def __init__(self, empleado: Empleado, fecha_hora: datetime, tipo: MarcacionTipo) -> None:
        self.__nro_registro = Marcacion.last_record
        self.__empleado = empleado
        self.__fecha_hora = fecha_hora.strftime('%d/%m/%Y %H:%M:%S')
        self.__tipo = tipo
        Marcacion.last_record += 1

    @property
    def nro_registro(self):
        return self.__nro_registro

    @property
    def empleado(self):
        return self.__empleado

    @property
    def tipo(self):
        return self.__tipo

    @property
    def fecha_hora(self) -> datetime:
        return self.__fecha_hora

    def __eq__(self, __o: object) -> bool:
        return self.__nro_registro == __o.nro_registro and self.tipo == __o.tipo

    def __repr__(self) -> str:
        return f"Marcacion(nro_registro={self.__nro_registro}, empleado={self.__empleado}, fecha_hora={self.__fecha_hora}, tipo={self.__tipo})"

    def __str__(self) -> str:
        return f"Marcacion {self.__nro_registro}, {self.__empleado}, {self.__fecha_hora}, {self.__tipo})"
