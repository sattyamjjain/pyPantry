import random

from pyPantry.DS import PyDS


class Node:
    def __init__(self, key, forward=None):
        if forward is None:
            forward = []
        self.key = key
        self.forward = forward


class PySkipLinkedList(PyDS):
    def __init__(self):
        super().__init__()
        self.max_level = 16
        self.head = Node(None, [None] * self.max_level)

    def random_level(self):
        level = 1
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def search(self, target):
        current = self.head
        for level in range(self.max_level - 1, -1, -1):
            while current.forward[level] and current.forward[level].key < target:
                current = current.forward[level]
        current = current.forward[0]
        if current and current.key == target:
            return current
        return None

    def insert(self, key):
        update = [None] * self.max_level
        current = self.head
        for level in range(self.max_level - 1, -1, -1):
            while current.forward[level] and current.forward[level].key < key:
                current = current.forward[level]
            update[level] = current

        level = self.random_level()
        new_node = Node(key, [None] * level)
        for i in range(level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def display(self):
        current = self.head.forward[0]
        while current:
            print(current.key, end=" -> ")
            current = current.forward[0]
        print("None")
