from pyPantry.DS import PyDS


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class PyCircularLinkedList(PyDS):
    def __init__(self):
        super().__init__()
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        current = self.head
        while current.next != self.head:
            current = current.next
        current.next = new_node
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data and self.head.next == self.head:
            self.head = None
            return

        current = self.head
        prev = None
        while current.data != data:
            if current.next == self.head:
                return
            prev = current
            current = current.next

        if current == self.head:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head
        else:
            prev.next = current.next

    def display(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("Head")
