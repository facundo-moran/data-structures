from typing import Any

class Heap:

    def __init__(self) -> None:
        self._nodes: list[Any] = []

    def __len__(self) -> int:
        return len(self._nodes)

    def is_empty(self) -> bool:
        return True if len(self) == 0 else False

    def __swap(self, idx_1: Any, idx_2: Any) -> None:
        aux = self._nodes[idx_1]
        self._nodes[idx_1] = self._nodes[idx_2]
        self._nodes[idx_2] = aux

    def __str__(self) -> str:
        return str(self._nodes)

    def __heapify_up(self):

        if len(self) == 2:
            if self._nodes[1] < self._nodes[0]:
                self.__swap(1, 0)
        elif len(self) > 2:
            last_pos = len(self._nodes)-1

            while last_pos != 0:
                if last_pos % 2 == 0:
                    root_node = int(last_pos/2)

                    if self._nodes[last_pos] < self._nodes[root_node]:
                        self.__swap(last_pos, root_node)

                    last_pos = root_node
                else:
                    root_node = int((last_pos-1)/2)

                    if self._nodes[last_pos] < self._nodes[root_node]:
                        self.__swap(last_pos, root_node)

                    last_pos = root_node

    def __heapify_down(self):

        if len(self) == 2:
            if self._nodes[1] < self._nodes[0]:
                self.__swap(1, 0)
        elif len(self) > 2:
            root = 0
            left_child = (root*2)+1

            self.__swap(len(self)-1, root)
            del self._nodes[len(self)-1]

            while True:
                try:
                    if self._nodes[root] > self._nodes[left_child]:
                        left_child = (left_child*2)+1
                    else:
                        right_child = left_child*2
                        try:
                            if self._nodes[root] > self._nodes[right_child]:
                                left_child = right_child*2
                        except:
                            self._nodes.insert(right_child, self._nodes[root])
                            self._nodes.remove(self._nodes[root])
                            break
                except:
                    self._nodes.insert(left_child, self._nodes[root])
                    self._nodes.remove(self._nodes[root])
                    break

    def find_min(self):
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        return self._nodes.copy()[0]

    def insert(self, v: Any) -> None:
        if not v:
            raise Exception("La operación no se puede llevar a cabo.")

        if len(self) > 0:
            try:
                if type(self._nodes[0]) != type(v):
                    raise Exception(
                        f"Type Error: Key Type must be {type(self._nodes[0])}")
            except:
                return

        self._nodes.append(v)
        self.__heapify_up()

    def delete(self, v: Any) -> bool:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        try:
            index = self._nodes.index(v)

            if not index:
                self.remove_min()
                return

            del self._nodes[index]

            return True
        except:
            return False

    def remove_min(self) -> Any:
        if self.is_empty():
            raise Exception("La operación no se puede llevar a cabo.")

        min = self._nodes[0]

        self.__heapify_down()

        return min
