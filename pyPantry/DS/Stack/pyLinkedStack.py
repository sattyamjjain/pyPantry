from pyPantry.DS import PyDS


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PyLinkedStack(PyDS):
    def __init__(self):
        super().__init__()
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop item.")
        item = self.top.data
        self.top = self.top.next
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek item.")
        return self.top.data

    def get_size(self):
        return self.size
