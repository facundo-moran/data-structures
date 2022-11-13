from typing import List, Any
import copy

class PriorityQueueNode():

    def __init__(self, node_key) -> None:
        self.__node_key = node_key
        self.__values: list[Any] = []

    def __len__(self) -> int:
        return len(self.__values)

    def __eq__(self, __o: object) -> bool:
        return self.__node_key == __o.__node_key

    def __repr__(self) -> str:
        return f"\tPriorityQueueNode(nombre={self.__node_key}, values={self.__values})"

    def __del__(self):
        print('__del__ was called')
        
    def get_key(self):
        return copy.copy(self.__node_key)

    def get_head_value(self) -> Any:
        return self.__values.copy()[0]

    def get_values(self) -> List[Any]:
        return self.__values.copy()

    def add_value(self, v: Any) -> None:
        self.__values.append(v)

    def remove_head_value(self) -> Any:
        head_value = self.__values.copy()[0]

        self.__values.remove(head_value)

        return head_value