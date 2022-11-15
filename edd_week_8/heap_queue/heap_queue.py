from typing import Any
from min_heap import Heap

class HeapQueue(Heap):
    def __init__(self, size=10) -> None:
        super().__init__()
        self._size = size

    def is_full(self) -> bool:
        return len(self) == self._size

    def enqueue(self, v: Any) -> None:
        if self.is_full() or not v:
            raise Exception("La operación no se puede llevar a cabo.")

        self._insert(v)

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        return self._remove_min()

    def peek(self) -> None:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        return self._find_min()
