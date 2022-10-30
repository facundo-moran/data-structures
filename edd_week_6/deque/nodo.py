from typing import Any


class Nodo:

    __slots__ = "elemento", "anterior", "siguiente"

    def __init__(self, elemento: Any, anterior=None, siguiente=None) -> None:
        self.elemento = elemento
        self.anterior: Nodo | None = anterior
        self.siguiente: Nodo | None = siguiente
