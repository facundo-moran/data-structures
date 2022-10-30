from deque import Deque
from util import h1, h2

def deque_client():
    deque = Deque()
    h1("Double Ended Queue")

    for i in range(1, 49):
        deque.add_last(i)   

    print(deque, "\n")
    h2("Poniendo a prueba los metodos")

    print("Cantidad incial de elemento en la estructura: ", len(deque), "\n" )

    print("¿La estructura está vacía?", deque.is_empty(), "\n")

    print("Elemento ubicado al frente de la estructura: ", deque.first())
    print("Elemento ubicado al final de la estructura:", deque.last(), "\n")

    print("Agregando el nro '0' al principio de la estructura..")
    deque.add_first(0)
    print(deque)

    print("Agregando el nro '11' al final de la estructura..")
    deque.add_last(11)
    print(deque, "\n")

    print("Eliminando primer elemento..")
    deque.delete_first()
    print(deque,"\n")

    print("Eliminando ultimo elemento..")
    deque.delete_last()
    print(deque, "\n")

    print("Cantidad final de elementos en la estructura: ", len(deque), "\n" )

if __name__ == '__main__':  
    deque_client()