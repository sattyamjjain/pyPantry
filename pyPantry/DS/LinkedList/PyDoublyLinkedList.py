import logging

from pyPantry.DS import PyDS


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class PyDoublyLinkedList(PyDS):
    def __init__(self):
        super().__init__()
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def display(self):
        logger = logging.getLogger(__name__)
        current = self.head
        while current:
            logger.info(current.data)
            current = current.next
        logger.info("None")
