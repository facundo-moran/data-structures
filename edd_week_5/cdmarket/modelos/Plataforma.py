class Plataforma:
    def __init__(self, nombre: str, portatil: bool) -> None:
        self.__nombre = nombre
        self.__es_portatil = portatil

    @property
    def nombre(self):
        return self.__nombre

    @property
    def es_portatil(self):
        return self.__es_portatil

    def __eq__(self, __o: object) -> bool:
        return self.__nombre == __o.nombre and self.__es_portatil == __o.es_portatil

    def __repr__(self) -> str:
        return f"Plataforma(nombre={self.__nombre}, portatil={self.__es_portatil})"

    def __str__(self) -> str:
        return f"Plataforma {self.__nombre}, {self.__es_portatil}"

    def __hash__(self):
        return hash(str(self))
