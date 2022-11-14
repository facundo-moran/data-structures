from unsorted_priority_queue import unsorted_priority_queue

def app():

    """
        TODO: al imprimir queue se imprime dos veces
    """

    queue = unsorted_priority_queue()

    print(f'\n1. queue len {len(queue)}')
    print(f'\n2. queue is empty {queue.is_empty()}')

    print('\n3. add harina: 1000')
    queue.add("harina", 1000)
    print('\n4. add 1: 1000')
    queue.add(1, 1000)
    print('\n5. add auto: renault')
    queue.add('auto', 'renault')
    print('\n6. add auto: ferrari')
    queue.add('auto', 'ferrari')
    print('\n7. add dni: 9999999')
    queue.add('dni', 9999999)

    print(f'\n8. queue len {len(queue)}')
    print(f'\n9. queue is empty {queue.is_empty()}')
    print(f'\n10. {queue}')
    print(f'\n11. min = {queue.min()}')
    print(f'\n12. remove_min = {queue.remove_min()}')

    print(f'\n13. queue len {len(queue)}')
    print(f'\n14. queue is empty {queue.is_empty()}')

    print(f'\n15. {queue}')

if __name__ == '__main__':
    app()
