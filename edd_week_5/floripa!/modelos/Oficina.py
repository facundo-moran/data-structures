from datetime import time


class Oficina:

    def __init__(self, nombre: str, hora_entrada: time, hora_salida: time) -> None:
        self.__nombre = nombre
        self.__hora_entrada = hora_entrada.strftime('%H:%M:%S')
        self.__hora_salida = hora_salida.strftime('%H:%M:%S')

    @property
    def hora_entrada(self):
        return self.__hora_entrada

    @property
    def hora_salida(self):
        return self.__hora_salida

    def __eq__(self, __o: object) -> bool:
        return self.__nombre == __o.nombre

    def __repr__(self) -> str:
        return f"Oficina(nombre={self.nombre}, hora_entrada={self.__hora_entrada}, hora_salida={self.__hora_salida})"

    def __str__(self) -> str:
        return f"Oficina {self.__nombre}, {self.__hora_entrada}, {self.__hora_salida}"
