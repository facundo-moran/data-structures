from typing import Tuple, Any
from UnsortedPriorityQueueAbstract import UnsortedPriorityQueueAbstract
from priority_queue_node import PriorityQueueNode

class unsorted_priority_queue(UnsortedPriorityQueueAbstract):

    def __init__(self) -> None:
        self._elements: list[PriorityQueueNode] = []

    def __len__(self) -> int:
        return len(self._elements)

    def is_empty(self) -> bool:
        return True if len(self) == 0 else False

    def add(self, k: Any, v: Any) -> None:
        if (not (k and v)):
            raise Exception("La operación no se puede llevar a cabo.")

        item = PriorityQueueNode(k)

        if len(self._elements) > 0:
            try:
                last_item = self._elements[len(self._elements)-1]

                if type(last_item.get_key()) != type(k):
                    raise Exception(
                        f"Type Error: Key Type must be {type(last_item.get_key())}")

                if last_item.get_key() < item.get_key():
                    item.add_value(v)
                    self._elements.append(item)
                    self._elements.append(last_item)
                    self._elements.remove(last_item)
                else:
                    item.add_value(v)
                    self._elements.append(item)

                self._elements.sort(key=lambda node: node.get_key(),reverse=True)
            except Exception as ex:
                print(ex)
        else:
            item.add_value(v)
            self._elements.append(item)

    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        return (self._elements.copy()[len(self._elements)-1])

    def __repr__(self) -> str:
        return f"PriorityQueue(elements={self._elements})"

    def __str__(self) -> str:
        salida = 'PriorityQueue['

        if len(self._elements) > 0:
            for elm in self._elements:
                salida += f'\n{str(elm)}'

        salida += ']'
        return salida

    def __iter__(self):
        return iter(self._elements)

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        last_item = self._elements[len(self._elements)-1]
        self._elements.remove(last_item)

        return (last_item)
