from copy import deepcopy
from re import S
from typing import Any, Iterator
from double_linked_list_abstract import DoubleLinkedListAbstract
from nodo import Nodo


class DoubleLinkedList(DoubleLinkedListAbstract):

    def __init__(self) -> None:
        self._head: Nodo | None = None
        self._tail: Nodo | None = None
        self._size: int = 0

    @property
    def size(self) -> int:
        return self._size

    def __is_valid_argument(self, element: Any) -> bool:
        return not element == None

    def __initialize(self, element: Any):
        new_end = Nodo(element)

        self._tail = deepcopy(new_end)
        self._head = deepcopy(new_end)

    def _replace_tail(self, element: Any):
        aux = self._tail
        self._tail = Nodo(element)

        if len(self) == 1:
            self._head.siguiente = self._tail
            self._tail.anterior = self._head
        else:
            aux.siguiente = self._tail
            self._tail.anterior = aux
            self._tail.siguiente = None

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, key: int) -> Any:
        if key < 0 or key >= len(self):
            raise Exception("Índice fuera de rango")

        i = 0
        actual = self._head
        while actual:
            if i == key:
                return actual.elemento
            actual = actual.siguiente
            i += 1

    def __setitem__(self, key: int, value: Any) -> None:
        if key < 0 or key >= len(self):
            raise Exception("Índice fuera de rango")

        i = 0
        actual = self._head

        while actual:
            if i == key:
                actual.elemento = value
                return

            actual = actual.siguiente
            i += 1

    def __delitem__(self, key: int) -> None:

        if key < 0 or key >= len(self):
            raise Exception("Índice fuera de rango")

        if self.is_empty():
            raise Exception("La estructura está vacía")

        if key == 0:
            if len(self) == 1:
                self._head = None
                self._tail = None
            else:
                self._head.siguiente.anterior = None
                self._head = self._head.siguiente

            self._size -= 1
            return

        if key == len(self)-1:
            self._tail.anterior.siguiente = None
            self._tail = self._tail.anterior

            self._size -= 1
            return

        i = 0
        actual = self._head

        while actual:
            if i == key:
                anterior = actual.anterior
                siguiente = actual.siguiente
                anterior.siguiente = siguiente
                siguiente.anterior = anterior
                actual = None
                return
            actual = actual.siguiente
            i += 1

    def __iter__(self) -> Iterator[Any]:
        if self.is_empty():
            yield None

        head = self._head

        while head:
            yield head.elemento
            head = head.siguiente

    def __str__(self) -> str:

        if self.is_empty():
            return "DoubleLinkedList()"

        actual = self._head
        resultado = ""

        while actual:
            resultado += str(actual.elemento) + ", "
            actual = actual.siguiente

        resultado = resultado[:len(resultado)-2]

        return f"LinkedList({resultado})"

    def is_empty(self) -> bool:
        return len(self) == 0

    def append(self, elem: Any) -> None:
        if not self.__is_valid_argument(elem):
            raise Exception("Invalid argument")

        if not self._tail:
            self.__initialize(elem)
        else:
            self._replace_tail(elem)

        self._size += 1
