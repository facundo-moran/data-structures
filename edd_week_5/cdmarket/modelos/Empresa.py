class Empresa:
    def __init__(self, nombre: str) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    def __eq__(self, __o: object) -> bool:
        return self.__nombre == __o.nombre

    def __repr__(self) -> str:
        return f"Empresa(nombre={self.__nombre})"

    def __str__(self) -> str:
        return f"Empresa {self.__nombre}"
