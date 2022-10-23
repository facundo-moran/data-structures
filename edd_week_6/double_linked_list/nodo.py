from typing import Any, Union


class Nodo:

    __slots__ = "elemento", "siguiente"
    def __init__(self, elemento: Any, siguiente = None) -> None:
        self.elemento = elemento
        self.siguiente: Union[Nodo, None] = siguiente
