
from modelos.Oficina import Oficina


class Empleado:

    def __init__(self, legajo: int, documento: str, apellido: str, nombre: str, oficina: Oficina):
        self.__legajo = legajo
        self.__documento = documento
        self.__apellido = apellido
        self.__nombre = nombre
        self.__oficina = oficina

    @property
    def apellido(self):
        return self.__apellido

    @property
    def nombre(self):
        return self.__nombre

    @property
    def legajo(self):
        return self.__legajo

    @property
    def oficina(self):
        return self.__oficina
    
    @property
    def documento(self):
        return self.__documento
    
    def __eq__(self, __o: object) -> bool:
        return self.__legajo == __o.legajo and self.__documento == __o.documento

    def __repr__(self) -> str:
        return f"Empleado(legajo={self.__legajo}, documento={self.__documento}, apellido={self.__apellido}, nombre={self.__nombre}, oficina={self.__oficina})"

    def __str__(self) -> str:
        return f"Empleado {self.__legajo}, {self.__documento}, {self.__apellido}, {self.__nombre}, {self.__oficina})"

    def __lt__(self, other: object):
        return (self.__legajo < other.legajo)

    def __hash__(self):
        return hash(str(self))