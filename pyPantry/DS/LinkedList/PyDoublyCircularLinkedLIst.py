from pyPantry.DS import PyDS


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class PyDoublyCircularLinkedList(PyDS):
    def __init__(self):
        super().__init__()
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = self.head
            self.head.prev = new_node

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        if not self.head:
            return

        current = self.head
        while True:
            if current.data == data:
                if current.next == current:
                    self.head = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                    if current == self.head:
                        self.head = current.next
                return

            current = current.next
            if current == self.head:
                break

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" <-> ")
            current = current.next
            if current == self.head:
                break
        print("Head")
