from pyPantry.DS import PyDS


class PyQueue(PyDS):
    def __init__(self):
        super().__init__()
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot pop item.")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot front item.")
        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue = []
