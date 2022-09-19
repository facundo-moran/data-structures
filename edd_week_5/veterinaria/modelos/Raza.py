class Raza:
    def __init__(self, nombre, especie) -> None:
        self.__nombre = nombre
        self.__especie = especie

    @property
    def nombre(self):
        return self.__nombre

    @property
    def especie(self):
        return self.__especie

    def __eq__(self, __o):
        return self.__especie == __o.especie and self.__nombre == __o.nombre

    def __repr__(self) -> str:
        return f"Raza(nombre={self.__nombre}, especie={self.__especie})"

    def __str__(self) -> str:
        return f"Raza {self.__nombre}, {self.__especie}"
