from pyPantry.DS import PyDS


class PyPriorityQueue(PyDS):
    def __init__(self):
        super().__init__()
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item, priority):
        element = (priority, item)
        if self.is_empty():
            self.queue.append(element)
        else:
            inserted = False
            for i in range(len(self.queue)):
                if self.queue[i][0] > priority:
                    self.queue.insert(i, element)
                    inserted = True
                    break
            if not inserted:
                self.queue.append(element)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue item.")
        (_, item) = self.queue.pop(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot peek item.")
        return self.queue[0][1]

    def size(self):
        return len(self.queue)
