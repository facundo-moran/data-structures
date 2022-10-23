from typing import Any
from deque_abstract import DequeAbstract

class Deque(DequeAbstract):

    def __init__(self, size=100):
        
        self._data : list[Any] = [None] * size
        self.capacity = size
        self._frente: int = 0
        self._final: int = -1
        self._tamanio : int = 0

    def __len__(self) -> int:
        return self._tamanio
    
    def __str__(self) -> str:
        str_deque = [str(elem) for elem in self._data if elem != None]
                
        return "Deque(" + ", ".join(str_deque) + ")"

    def is_empty(self) -> bool:
        return self.__len__() == 0

    def first(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura está vacía")
            exit(-1)
        return self._data[self._frente]

    def last(self) -> Any:
        if self.is_empty():
            raise Exception("La estructura está vacía")
            exit(-1)
        return self._data[self._final]

    def add_first(self, element: Any) -> None:
        self._frente = (self._frente) % self.capacity
        self._data[self._frente] = element
        self._tamanio += 1

    def add_last(self, element: Any) -> None:
        self._final = (self._final + 1) % self.capacity
        self._data[self._final] = element
        self._tamanio = self._tamanio + 1

    def delete_first(self) -> None:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        self._data[self._frente] = None
        self._frente = (self._frente) % self.capacity
        self._tamanio += 1

    def delete_last(self) -> None:
        if self.is_empty():
            raise Exception("La estructura está vacía")

        self._data[self._final] = None
        self._final = (self._final) % self.capacity
        self._tamanio += 1