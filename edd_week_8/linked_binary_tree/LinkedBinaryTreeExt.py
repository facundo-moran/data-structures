from LinkedBinaryTreeExtAbstract import LinkedBinaryTreeExtAbstract
from binary_tree_node import BinaryTreeNode
from linked_binary_tree import LinkedBinaryTree

from typing import Any, List, Iterable


class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):

    def __init__(self) -> None:
        super().__init__()

    def _node_level_order_traversal(self) -> Iterable[Any]:

        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        return self.__node_level_order_traversal(self._root)

    def __node_level_order_traversal(self, node : BinaryTreeNode) -> Iterable[Any]:

        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        if not node or not self._contains(node):
            raise Exception(
                "Nodo no encontrado. La operación no se puede llevar a cabo.")

        nodos = []
        nodos.append(node)
        iterador_nodos = iter(nodos)
        while True:
            try:
                actual = next(iterador_nodos)
                yield actual

                if actual.left_child:
                    nodos.append(actual.left_child)

                if actual.right_child:
                    nodos.append(actual.right_child)

            except StopIteration:
                break

    def level_order_traversal(self) -> Iterable[Any]:
        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        elementos = []
        iterador_nodos = self._node_level_order_traversal()

        while True:
            try:
                elementos.append(next(iterador_nodos).element)
            except StopIteration:
                break

        return elementos

    def hermanos(self, nodo1: BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:

        if not nodo1 or not nodo2:
            return False

        if nodo1 == self._root or nodo2 == self._root:
            return False

        return self._search_parent(nodo1) == self._search_parent(nodo2)

    def hojas(self) -> List[Any]:
        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        hojas = []
        iterador_nodos = self._node_level_order_traversal()
        while True:
            try:
                actual = next(iterador_nodos)

                if not (actual.left_child or actual.right_child):
                    hojas.append(actual.element)

            except StopIteration:
                break

        return hojas

    def internos(self) -> List[Any]:
        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        internNodes = set(self.preorder_traversal()) - \
            set(self.hojas()) - set(self.root())

        return list(internNodes)

    def profundidad(self, nodo: BinaryTreeNode) -> int:
        profundidad = 0

        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        if not nodo or not self._contains(nodo):
            raise Exception(
                "Nodo no encontrado. La operación no se puede llevar a cabo.")

        if nodo == self._root:
            return profundidad

        actual = nodo

        while True:

            if self._search_parent(actual) == self._root:
                profundidad += 1
                break
            else:
                profundidad += 1
                actual = self._search_parent(actual)

        return profundidad

    def altura(self, nodo: BinaryTreeNode) -> int:

        if self.is_empty():
            raise Exception(
                "Estructura vacía. La operación no se puede llevar a cabo.")

        if not nodo or not self._contains(nodo):
            raise Exception(
                "Nodo no encontrado. La operación no se puede llevar a cabo.")

        if set(self.hojas()) & set(nodo.element):
            return 0

        def calcular_altura_recursiva(nodo: BinaryTreeNode) -> int:

            altura = 0

            if set(self.internos()) & set(nodo.element):
                if nodo.left_child:
                    altura = max(altura, calcular_altura_recursiva(nodo.left_child))

                if nodo.right_child:
                    altura = max(altura, calcular_altura_recursiva(nodo.right_child))
                
                altura+=1

            return altura
            
        return calcular_altura_recursiva(nodo)
                    
                
            

