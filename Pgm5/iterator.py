class Iterator:
    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def is_done(self):
        raise NotImplementedError

    def current(self):
        raise NotImplementedError


class Iterable:
    def create_iterator(self):
        raise NotImplementedError


class Sequence:
    def add(self, item):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

    def capacity(self):
        raise NotImplementedError

    def get(self, index):
        raise NotImplementedError


class IterableSequence(Sequence, Iterable):
    def first(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

    def is_done(self):
        raise NotImplementedError

    def current(self):
        raise NotImplementedError


class MyArrayIterator(Iterator):
    def __init__(self, array):
        self._array = array
        self._index = 0

    def first(self):
        self._index = 0

    def next(self):
        self._index += 1

    def is_done(self):
        return self._index >= self._array.size()

    def current(self):
        return self._array.get(self._index)


class MyArray(IterableSequence):
    def __init__(self, capacity):
        self._capacity = capacity
        self._size = 0
        self._array = [None] * capacity

    def add(self, item):
        if self._size == self._capacity:
            raise Exception("Array is full")
        self._array[self._size] = item
        self._size += 1

    def size(self):
        return self._size

    def capacity(self):
        return self._capacity

    def get(self, index):
        if index >= self._size:
            raise Exception("Index out of range")
        return self._array[index]

    def get_iterator(self):
        return MyArrayIterator(self)


class FilterIterator(Iterator):
    def __init__(self, iterator, predicate):
        self._iterator = iterator
        self._predicate = predicate
        self._current = None

    def first(self):
        self._iterator.first()
        self._next()

    def next(self):
        self._iterator.next()
        self._next()

    def is_done(self):
        return self._iterator.is_done()

    def current(self):
        return self._current

    def _next(self):
        while not self._iterator.is_done():
            if self._predicate(self._iterator.current()):
                self._current = self._iterator.current()
                return
            self._iterator.next()
        self._current = None


class ReverseIterator(Iterator):
    def __init__(self, iterator):
        self._iterator = iterator
        self._items = []

    def first(self):
        self._items = []
        self._iterator.first()
        while not self._iterator.is_done():
            self._items.append(self._iterator.current())
            self._iterator.next()
        self._items.reverse()
        self._index = 0

    def next(self):
        self._index += 1

    def is_done(self):
        return self._index >= len(self._items)

    def current(self):
        return self._items[self._index]
