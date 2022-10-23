from double_linked_list import DoubleLinkedList
from util import h1, h2


def double_linked_list_client():
    lista = DoubleLinkedList()
    h1("DoubleLinkedList")

    for i in range(1, 11):
        lista.append(i)
    print(lista, "\n")
    h2("Poniendo a prueba los metodos")

    print("Cantidad de elemento de la lista: ", len(lista), "\n")

    print("Elemento ubicado en la posicion 5 ->", lista.__getitem__(5))
    print("Elemento ubicado en la posicion 0 ->", lista.__getitem__(0), "\n")

    print("Cambiando nro '10' por nro '100'..")
    lista.__setitem__(9, 100)
    print(lista, "\n")

    print("Eliminando ultimo elemento..")
    lista.__delitem__(9)
    print(lista, "\n")

    print("Elementos de la lista: ")
    lista.__iter__()
    print("\n")

    print("¿La lista está vacía?", lista.is_empty())


if __name__ == '__main__':
    double_linked_list_client()
