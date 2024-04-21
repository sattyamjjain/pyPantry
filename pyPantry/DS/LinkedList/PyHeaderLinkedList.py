import logging

from pyPantry.DS import PyDS


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class PyHeaderLinkedList(PyDS):
    def __init__(self):
        super().__init__()
        self.header = Node()
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        current = self.header
        while current.next:
            current = current.next
        current.next = new_node
        self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.header.next
        self.header.next = new_node
        self.length += 1

    def delete(self, data):
        current = self.header
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                self.length -= 1
                return
            current = current.next

    def display(self):
        logger = logging.getLogger(__name__)
        current = self.header.next
        display_str = ""
        while current:
            display_str += str(current.data) + " -> "
            current = current.next
        display_str += "None"
        logger.info(display_str)
