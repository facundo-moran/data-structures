from typing import Any, Tuple

from unsorted_priority_queue import unsorted_priority_queue

class PriorityQueueStack():

    def __init__(self, size: int = 10) -> None:
        self._size = size
        self._elements = unsorted_priority_queue()

    def __len__(self) -> int:
        return len(self._elements)

    def __str__(self) -> str:
        salida = ''

        for elm in self._elements:
            salida += str(elm.get_values())

        return salida

    def is_empty(self) -> bool:
        return True if len(self) == 0 else False

    def is_full(self):
        return True if len(self) == self._size else False

    def top(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")
            
        return self._elements.min().get_values()[0]

    def push(self, elm: Any) -> None:
        if not elm or self.is_full():
            raise Exception("La operación no se puede llevar a cabo.")

        self._elements.add(elm,elm)
        
    def pop(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        return self._elements.remove_min().get_values()[0]

    def make_empty(self) -> bool:
        try:
            self._elements = unsorted_priority_queue()
            return True
        except:
            return False
    
        



