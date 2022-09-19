from pydoc import doc


class Persona:
    def __init__(self, apellido, nombre, documento) -> None:
        self.__apellido = apellido
        self.__nombre = nombre
        self.__documento = documento

    @property
    def apellido(self):
        return self.__apellido

    @property
    def nombre(self):
        return self.__nombre

    @property
    def documento(self):
        return self.__documento

    def __eq__(self, __o):
        return isinstance(__o, Persona) and self.__documento == __o.documento

    def __hash__(self) -> int:
        return hash(self.__documento)

    def __repr__(self) -> str:
        return f"Persona(apellido={self.__apellido}, nombre={self.__nombre}, documento={self.__documento})"

    def __str__(self) -> str:
        return f"Persona {self.__apellido}, {self.__nombre}, {self.__documento}"
