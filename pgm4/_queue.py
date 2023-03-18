class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def __iter__(self):
        node = self.first
        while node:
            yield node
            node = node.next

    def enqueue(self, value):
        node = Node(value)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.size += 1

    def dequeue(self):
        if self.first is None:
            return None
        node = self.first
        self.first = self.first.next
        self.size -= 1
        return node.value

    def peek(self):
        if self.first is None:
            return None
        return self.first.value

    def is_empty(self):
        return self.first is None
