from pyPantry.DS import PyDS


class PyStack(PyDS):
    def __init__(self):
        super().__init__()
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item: any):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop item.")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot peek item.")
        return self.stack[-1]

    def size(self):
        return len(self.stack)
