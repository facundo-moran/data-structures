# from collections import defaultdict

from binary_tree_node import BinaryTreeNode
from LinkedBinaryTreeExt import LinkedBinaryTreeExt


def app_1():
    # dictiona = defaultdict(list)

    treee = LinkedBinaryTreeExt()
    
    raiz = BinaryTreeNode('A');
    node_b = BinaryTreeNode('B')
    node_c = BinaryTreeNode('C')
    node_d = BinaryTreeNode('D')
    node_e = BinaryTreeNode('E')
    node_f = BinaryTreeNode('F')
    node_g = BinaryTreeNode('G')
    node_h = BinaryTreeNode('H')
    node_i = BinaryTreeNode('I')
    node_j = BinaryTreeNode('J')
    node_k = BinaryTreeNode('K')

    treee.add_right_child(None, raiz)

    treee.add_left_child(raiz, node_b )
    treee.add_right_child(raiz, node_c )

    treee.add_left_child(node_c, node_d )
    treee.add_right_child(node_c, node_h )

    treee.add_left_child(node_b, node_f )
    treee.add_right_child(node_b, node_g )

    treee.add_left_child(node_d, node_e )

    treee.add_left_child(node_e, node_i )
    
    treee.add_right_child(node_f, node_j )

    treee.add_right_child(node_g, node_k )


    print(f'hojas: {treee.hojas()}')
    print(f'internos: {treee.internos()}')
    print(f'todos: {treee.level_order_traversal()}')

    print(f'produndidad de e: {treee.profundidad(node_e)}')
    print(f'produndidad de raiz: {treee.profundidad(raiz)}')
    print(f'produndidad de g: {treee.profundidad(node_g)}')
    print(f'produndidad de i: {treee.profundidad(node_i)}')
    print(f'produndidad de c: {treee.profundidad(node_c)}')

    print(f'altura de raiz: {treee.altura(raiz)}')
    print(f'altura de j: {treee.altura(node_j)}')
    print(f'altura de k: {treee.altura(node_k)}')
    print(f'altura de i: {treee.altura(node_i)}')
    print(f'altura de h: {treee.altura(node_h)}')
    print(f'altura de d: {treee.altura(node_d)}')
    print(f'altura de b: {treee.altura(node_b)}')
    print(f'altura de f: {treee.altura(node_f)}')
    print(f'altura de g: {treee.altura(node_g)}')
    print(f'altura de c: {treee.altura(node_c)}')

def app():
    nodo_a = BinaryTreeNode('A')
    nodo_b = BinaryTreeNode('B')
    nodo_c = BinaryTreeNode('C')
    nodo_d = BinaryTreeNode('D')
    nodo_f = BinaryTreeNode('F')
    nodo_g = BinaryTreeNode('G')
    nodo_h = BinaryTreeNode('H')
    nodo_i = BinaryTreeNode('I')
    nodo_k = BinaryTreeNode('K')
    nodo_m = BinaryTreeNode('M')
    nodo_n = BinaryTreeNode('N')
    arbol = LinkedBinaryTreeExt()

    arbol.add_left_child(None, nodo_a)
    arbol.add_left_child(nodo_a, nodo_b)
    arbol.add_right_child(nodo_a, nodo_f)
    arbol.add_left_child(nodo_b, nodo_c)
    arbol.add_right_child(nodo_b, nodo_d)
    arbol.add_left_child(nodo_f, nodo_g)
    arbol.add_right_child(nodo_f, nodo_k)
    arbol.add_left_child(nodo_g, nodo_h)
    arbol.add_right_child(nodo_g, nodo_i)
    arbol.add_left_child(nodo_k, nodo_m)
    arbol.add_right_child(nodo_k, nodo_n)
    
    print(arbol)

if __name__ == '__main__':
    app()
