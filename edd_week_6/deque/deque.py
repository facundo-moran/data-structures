from typing import Any
from deque_abstract import DequeAbstract
from nodo import Nodo


class Deque(DequeAbstract):

    def __init__(self, max_size=50):
        self._head: Nodo | None = None
        self._tail: Nodo | None = None
        self._size: int = 0
        self._capacity: int = max_size

    def __is_valid_argument(self, element: Any) -> bool:
        return not element == None

    def __initialize(self, element: Any):
        new_end = Nodo(element)

        self._tail = new_end
        self._head = new_end

        self._tail.anterior = self._head
        self._tail.siguiente = self._head

        self._head.anterior = self._tail
        self._head.siguiente = self._tail

    def __replace_end(self, element: any, endNode: Nodo):

        if endNode == self._tail:
            aux = self._tail
            self._tail = Nodo(element, aux, aux.siguiente)
            aux.siguiente = self._tail
            return

        if endNode == self._head:
            aux = self._head
            self._head = Nodo(element, aux.anterior, aux)
            aux.anterior = self._head
            return

    def _replace_tail(self, element: Any):
        self.__replace_end(element, self._tail)

    def _replace_head(self, element: Any):
        self.__replace_end(element, self._head)

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:

        if self.is_empty():
            return "Deque()"

        resultado = ""

        actual = self._head
        while actual:
            resultado += str(actual.elemento) + ", "

            if actual == self._tail:
                break

            actual = actual.siguiente

        resultado = resultado[:len(resultado)-2]

        return f"Deque({resultado})"

    def is_empty(self) -> bool:
        return len(self) == 0

    def is_full(self) -> bool:
        return len(self) == self._capacity

    def first(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        return self._head.elemento

    def last(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        return self._tail.elemento

    def add_first(self, element: Any) -> None:

        if self.is_full():
            raise Exception("Deque overflow error")

        if not self.__is_valid_argument(element):
            raise Exception("Invalid argument")

        if not self._head:
            self.__initialize(element)
        else:
            self._replace_head(element)

        self._size += 1

    def add_last(self, element: Any) -> None:

        if self.is_full():
            raise Exception("Deque overflow error")

        if not self.__is_valid_argument(element):
            raise Exception("Invalid argument")

        if not self._tail:
            self.__initialize(element)
        else:
            self._replace_tail(element)

        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        self._tail.siguiente = self._head.siguiente
        self._head = self._tail.siguiente

        self._size -= 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        self._head.anterior = self._tail.anterior
        self._tail = self._head.anterior

        self._size -= 1
