# A single node of a singly linked list
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f'Node data is {self.data} and next is {self.next}'

    def __repr__(self) -> str:
        return f'Node(data={self.data}, next={self.next})'


# A singly linked list
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return f'LinkedList head is {self.head}'

    def __repr__(self) -> str:
        return 'LinkedList()'

    def __iter__(self):
        node = self.head
        while node is not None:
            # we yield the data instead of the node so that
            # our queue can easily change implementations to
            # tyield the node just delete the .data
            yield node.data
            node = node.next

    def __next__(self) -> Node:
        yield self.head.next

    def add(self, data) -> None:
        '''Add an item to the linked list.'''
        newNode = Node(data)
        if (self.head):
            current = self.head
            while (current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def removeNode(self, item) -> None:
        '''Remove a node by its value.'''
        if self.head is None:
            return None

        def _remove_helper(current, item) -> None:
            temp = current
            if current.next is None:
                return None
            if temp.next.data == item:
                temp.next = temp.next.next
                return None
            else:
                return _remove_helper(temp.next, item)

        if self.head.data == item:
            self.head = self.head.next
            return None
        else:
            return _remove_helper(self.head, item)
    
    def remove(self) -> Node:
        '''Removes the head of the linked list.'''
        if self.head is not None:
            item = self.head.data
            self.head = self.head.next
            return item

    def getNode(self, item) -> Node:
        '''Returns the node whose data matches item.'''
        if self.head is None:
            return None
        
        def _get_helper(current, item):
            temp = current
            if current.next is None:
                return None
            if temp.next.data == item:
                return temp.next
            else:
                return _get_helper(temp.next, item)
        
        if self.head.data == item:
            return self.head.data
        else:
            return _get_helper(self.head, item)
    
    def get(self) -> any:
        '''Returns the head of the list.'''
        if self.head is None:
            return None
        return self.head.data

    def size(self) -> int:
        '''Get the size of the linked list.'''
        count = 0
        current = self.head
        while (current):
            count += 1
            current = current.next
        return count

    def clear(self) -> None:
        '''Remove all items from the linked list.'''
        if self.head is not None:
            self.head = self.head.next
            self.clear()
        return self

    def print_list(self) -> None:
        '''Print all list items'''
        current = self.head
        while (current):
            print(current.data)
            current = current.next


# This is a hack of a way to approach this.
# It should be properly redone in the future.
class DynamicArray:
    def __init__(self):
        self.arr = list()
        self._size = len(self.arr)

    def __str__(self):
        return f'DynamicArray has a size of {self._size} and items {self.arr}'

    def __repr__(self):
        return 'DynamicArray()'
    
    def __iter__(self):
        for item in self.arr:
            yield item

    def add(self, item):
        self.arr.append(item)
        self._size = len(self.arr)

    def remove_item(self, item):
        self.arr.remove(item)
        self._size = len(self.arr)

    def remove(self):
        item = self.arr[0]
        self.arr.remove(item)
        self._size = len(self.arr)

    def get(self):
        return self.arr[0]

    def size(self):
        return self._size

    def clear(self):
        self.arr = list()
        self._size = len(self.arr)
        return self
