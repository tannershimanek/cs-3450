# A single node of a singly linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'Node data is {self.data} and next is {self.next}'

    def __repr__(self):
        return f'Node(data={self.data}, next={self.next})'


# singly linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        return f'LinkedList head is {self.head}'

    def __repr__(self):
        return 'LinkedList()'

    def add(self, data):
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def remove(self):
        pass

    def get(self):
        pass

    def size(self):
        pass

    def clear(self):
        pass

    def print_list(self):
        current = self.head
        while (current):
            print(current.data)
            current = current.next


class DynamicArray:
    def __init__(self):
        self.arr = list()
        self._size = len(self.arr)

    def __str__(self):
        return f'DynamicArray has a size of {self._size} and items {self.arr}'

    def __repr__(self):
        return 'DynamicArray()'

    def add(self, item):
        self.arr.append(item)
        self._size = len(self.arr)

    def remove(self, item):
        self.arr.remove(item)
        self._size = len(self.arr)

    def get(self):
        return self.arr[0]

    def size(self):
        return self._size

    def clear(self):
        self.arr = list()
        self._size = len(self.arr)
