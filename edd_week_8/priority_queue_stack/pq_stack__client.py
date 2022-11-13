from priority_queue_stack import PriorityQueueStack


def app():
    queue_stack = PriorityQueueStack()

    print('queue push: 55')
    queue_stack.push(55)
    print('queue push: hola')
    queue_stack.push('hola')
    print('queue push: 99')
    queue_stack.push(99)
    print('queue push: 47')
    queue_stack.push(47)
    print('queue push: 23')
    queue_stack.push(23)
    print('queue push: 58')
    queue_stack.push(58)
    print('queue push: 46')
    queue_stack.push(46)
    print('queue push: 46')
    queue_stack.push(46)
    print('queue push: 89')
    queue_stack.push(89)

    print(f'queue len: {len(queue_stack)}')
    print(f'queue is empty: {queue_stack.is_empty()}')
    print(f'queue is full: {queue_stack.is_full()}')
    print(f'queue top: {queue_stack.top()}')
    print(f'queue pop: {queue_stack.pop()}')
    print(f'queue len: {len(queue_stack)}')
    print(f'queue stack: {queue_stack}')
    print(f'queue top: {queue_stack.top()}')
    print(f'queue pop: {queue_stack.pop()}')
    print(f'queue stack: {queue_stack}')
    print(f'make empty: {queue_stack.make_empty()}')
    print(f'queue stack: {queue_stack}')

if __name__ == "__main__":
    app()
