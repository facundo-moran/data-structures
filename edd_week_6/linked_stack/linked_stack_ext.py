from cmath import log
from this import d
from typing import Any, List
from linked_stack import LinkedStack
from linked_stack_ext_abstract import LinkedStackExtAbstract


class LinkedStackExt(LinkedStackExtAbstract, LinkedStack):

    def multi_pop(self, num: int) -> List[Any]:
        resultados = list()

        try:
            while num:
                resultados.append(self.pop())
                num -= 1
        except:
            None

        return resultados

    def replace_all(self, param1: Any, param2: Any) -> None:
        actual = self._head

        while actual:
            if actual.elemento == param1:
                actual.elemento = param2
            actual = actual.siguiente

    def exchange(self) -> None:

        if self.is_empty():
            raise Exception("Pila vacía. Operación no soportada")

        ultimo = self._head
        idx = 1

        while ultimo.siguiente:
            ultimo = ultimo.siguiente

            if idx == (len(self)-1):
                head_elm = self._head.elemento
                self._head.elemento = ultimo.elemento
                ultimo.elemento = head_elm

            idx += 1
