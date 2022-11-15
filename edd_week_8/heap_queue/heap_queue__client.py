from heap_queue import HeapQueue

def app():
    queue = HeapQueue()

    print(f'queue is empty {queue.is_empty()}')
    print(f'queue is full {queue.is_full()}')
    print(f'queue: {queue}')

    print(f'enqueue 1 {queue.enqueue(1)}')
    print(f'enqueue 99 {queue.enqueue(99)}')
    print(f'enqueue 58 {queue.enqueue(58)}')
    print(f'enqueue 46 {queue.enqueue(46)}')
    print(f'enqueue 35 {queue.enqueue(35)}')
    print(f'enqueue 75 {queue.enqueue(75)}')
    print(f'enqueue 64 {queue.enqueue(64)}')
    print(f'enqueue 82 {queue.enqueue(82)}')
    print(f'enqueue 34 {queue.enqueue(34)}')
    print(f'enqueue 19 {queue.enqueue(19)}')

    print(f'queue: {queue}')
    print(f'queue is empty {queue.is_empty()}')
    print(f'queue is full {queue.is_full()}')

    print(f'dequeue {queue.dequeue()}')
    print(f'queue peek: {queue.peek()}')

    print(f'queue: {queue}')

if __name__ == '__main__':
    app()
