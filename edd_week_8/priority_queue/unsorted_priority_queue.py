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

                try:
                    if self._elements[self._elements.index(item)]:
                        self._elements[self._elements.index(item)].add_value(v)
                        return
                except:
                    pass

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

        min_elm = self._elements.copy()[len(self._elements)-1]

        if len(min_elm.get_values()) > 1:
            return (min_elm.get_key(), min_elm.get_values().copy()[len(min_elm.get_values())-1])

        return (min_elm.get_key(), min_elm.get_values())

    def __repr__(self) -> str:
        return f"PriorityQueue(elements={self._elements})"

    def __str__(self) -> str:
        salida = 'PriorityQueue['

        for elm in self._elements:
            salida += f'\n{str(elm)}'

        salida += '\t\n]'
        return salida

    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        min_elm = self._elements[len(self._elements)-1]

        if len(min_elm.get_values()) > 1:
            min_elm_val = min_elm.get_values()[len(min_elm.get_values())-1]
            min_elm.get_values().reverse()
            min_elm.get_values().remove(min_elm_val)
            min_elm.get_values().reverse()
            return (min_elm.get_key(), min_elm_val)

        self._elements.remove(min_elm)

        return (min_elm.get_key(), min_elm.get_head_value())
