from min_heap import Heap

def app():
    heap = Heap()

    print(f'heap is empty: {heap.is_empty()}')
    print(f'heap str: {heap}')

    print('heap insert 31')
    heap.insert(31)
    print('heap insert 83')
    heap.insert(83)
    print('heap insert 40')
    heap.insert(40)
    print('heap insert 36')
    heap.insert(36)
    print('heap insert 4')
    heap.insert(4)
    print('heap insert 1')
    heap.insert(1)
    print('heap insert 68')
    heap.insert(68)

    print(f'heap is empty: {heap.is_empty()}')
    print(f'heap str: {heap}')
    print(f'heap len: {len(heap)}')
    print(f'heap min: {heap.find_min()}')
    print(f'heap is empty: {heap.is_empty()}')
    print(f'heap delete: 40 {heap.delete(40)}')
    print(f'heap str: {heap}')
    print(f'heap len: {len(heap)}')
    print(f'heap remove min: {heap.remove_min()}')
    print(f'heap str: {heap}')
    print(f'heap len: {len(heap)}')


if __name__ == '__main__':
    app()