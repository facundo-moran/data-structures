from typing import Any, Iterator
from double_linked_list_abstract import DoubleLinkedListAbstract
from nodo import Nodo

class DoubleLinkedList(DoubleLinkedListAbstract):

    def __init__(self) -> None:
        self._header: Nodo = None
        self._size: int = 0

    @property
    def size(self) -> int:
        actual = self._header
        while actual is not None:
            self._size = self._size + 1
            actual = actual.siguiente

        return self._size

    
    def __len__(self) -> int:
        i=0
        actual = self._header
        while actual is not None:
            i = i + 1
            actual = actual.siguiente 
            
        return i

    def __getitem__(self, key: int) -> Any:
        if key < 0 or key >= self.size:
            raise Exception("Índice fuera de rango")

        i=0
        actual =self._header
        while actual:
            if i == key:
                return actual.elemento
            actual = actual.siguiente
            i += 1

    def __setitem__(self, key: int, value: Any) -> None:
        if key < 0 or key >= self.size:
            raise Exception("Índice fuera de rango. Intente nuevamente.")

        i = 0 
        
        actual = self._header
        
        while actual: 
            if i == key: 
                actual.elemento = value
            actual = actual.siguiente
            i += 1

    def __delitem__(self, key: int) -> None:
        if key < 0 or key >= self.size:
            raise Exception("Índice fuera de rango. Intente nuevamente.")

        i = 0
        previo = None
        actual = self._header
        while actual is not None: 
            if i == key: 
                break
            previo = actual 
            actual = actual.siguiente
            i += 1

        if previo: 
            previo.siguiente = actual.siguiente
        else:
            self._header.siguiente = actual.siguiente

        self.size - 1

    def __iter__(self) -> Iterator[Any]:
        if self._header is None:
            print ("La lista está vacía")
            return
        else: 
            actual = self._header
            while actual is not None:
                print (actual.elemento, "")
                actual = actual.siguiente

    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleLinkedList()"
        
        res = "" 

        actual = self._header

        while actual: 
            res += str(actual.elemento) + ", "
            actual = actual.siguiente

        res = res[:-2]
        return f"LinkedList({res})"

    def is_empty(self) -> bool:
        if self._header is None:
            return True
        else:
            return False

    def append(self, elem: Any) -> None:
        nuevoNodo = Nodo(elem)
        if self._header is None:
            self._header = nuevoNodo
        else:
            actual = self._header
           
            while actual.siguiente is not None:
                actual = actual.siguiente
            
            actual.siguiente = nuevoNodo

        
