from double_linked_list import DoubleLinkedList
from util import h1, h2


def double_linked_list_client():
    lista = DoubleLinkedList()
    h1("DoubleLinkedList")

    for i in range(1, 5):
        lista.append(i)
    print(lista, "\n")
    h2("Poniendo a prueba los metodos")

    print("Cantidad de elementos de la lista: ", len(lista), "\n")

    for i in range(len(lista)):
        print(
            f"Elemento ubicado en la posicion {i} -> {lista.__getitem__(i)} \n")

    print("Cambiando nro '1' por nro '100'..")
    lista.__setitem__(0, 100)
    print(lista, "\n")

    print("Eliminando ultimo elemento..")
    lista.__delitem__(len(lista)-1)
    print(lista, "\n")

    print("¿La lista está vacía?", lista.is_empty())

    print('Iterando la lista../n')

    iterador = iter(lista)
    if iterador:
        try:
            print(f'Nodo iterado: {next(iterador)}')
            print(f'Nodo iterado: {next(iterador)}')
            print(f'Nodo iterado: {next(iterador)}')
            print(f'Nodo iterado: {next(iterador)}')
        except StopIteration:
            print("Iteration finished!")

if __name__ == '__main__':
    double_linked_list_client()
