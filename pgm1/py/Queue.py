class Queue:
    def __init__(self, impl) -> None:
        # clearing the impl before it added to the queue
        # prevents items that dont follow the FIFO order
        # from being added to the queue.
        self.impl = impl.clear() 

    def add(self, item):
        '''Add an item to the end of the queue.'''
        self.impl.add(item)

    def get(self):
        '''Get the first item of queue. (No Removal)'''
        return self.impl.get()

    def remove(self):
        '''Remove the first item of queue.'''
        return self.impl.remove()

    def size(self):
        '''Get the size of the queue.'''
        self.impl.size()

    def clear(self):
        '''Clear the queue (FIFO).'''
        self.impl.clear()

    def change_impl(self, new_impl):
        '''Change the implementation of the queue.'''
        new_impl.clear()
        for item in self.impl:
            new_impl.add(item)
        self.impl = new_impl

    def print_queue(self):
        '''Print all items in the queue.'''
        for item in self.impl:
            print(item)
