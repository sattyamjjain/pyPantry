from pyPantry.DS import PyDS


class CircularQueue(PyDS):
    def __init__(self, k):
        super().__init__()
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def enqueue(self, item):
        if self.is_full():
            raise IndexError("Queue is full. Cannot enqueue item.")
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue item.")
        item = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return item

    def is_empty(self):
        return self.front == -1 and self.rear == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def get_front(self):
        if self.is_empty():
            raise IndexError("Queue is empty. No front item.")
        return self.queue[self.front]

    def get_rear(self):
        if self.is_empty():
            raise IndexError("Queue is empty. No rear item.")
        return self.queue[self.rear]
