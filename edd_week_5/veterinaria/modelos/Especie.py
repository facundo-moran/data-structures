class Especie:
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __eq__(self, __o):
        return self.__nombre == __o.nombre

    def __repr__(self) -> str:
        return f"Especie(nombre={self.__nombre})"

    def __str__(self) -> str:
        return f"Especie {self.__nombre}"
