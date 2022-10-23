from typing import Any, List
from linked_stack import LinkedStack
from linked_stack_ext_abstract import LinkedStackExtAbstract

class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num:int) -> List[Any]:
        pass
    
    def replace_all(self, param1: Any, param2: Any) -> None:
        actual = self._head

        while actual:
            if actual. elemento== param1:
                actual.elemento = param2
            actual = actual.siguiente

    def exchange(self) -> None:
        if self.is_empty():
            raise Exception("La pila está vacia")
