from pyPantry.DS import PyDS


class PyDeque(PyDS):
    def __init__(self):
        super().__init__()
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove item from front.")
        return self.items.pop()

    def remove_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty. Cannot remove item from rear.")
        return self.items.pop(0)

    def peek_front(self):
        if self.is_empty():
            raise IndexError("Deque is empty. No item at front.")
        return self.items[-1]

    def peek_rear(self):
        if self.is_empty():
            raise IndexError("Deque is empty. No item at rear.")
        return self.items[0]

    def size(self):
        return len(self.items)
