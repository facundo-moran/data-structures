from unsorted_priority_queue import unsorted_priority_queue

def app():

    """
        TODO: al imprimir queue se imprime dos veces
    """

    queue = unsorted_priority_queue()

    print(f'\n1. queue len {len(queue)}')
    print(f'\n2. queue is empty {queue.is_empty()}')

    queue.add("harina", 1000)
    queue.add(1, 1000)
    queue.add('auto', 'renault')
    queue.add('auto', 'ferrari')
    queue.add('dni', 9999999)

    print(f'\n3. queue len {len(queue)}')
    print(f'\n4. queue is empty {queue.is_empty()}')
    print(f'\n5. {queue}')
    print(f'\n6. min = {queue.min()}')
    print(f'\n7. remove_min = {queue.remove_min()}')

    print(f'\n8. queue len {len(queue)}')
    print(f'\n9. queue is empty {queue.is_empty()}')

    print(f'\n10. {queue}')

if __name__ == '__main__':
    app()
