from pyPantry.DS import PyDS


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class PyBinaryTree(PyDS):
    def __init__(self):
        super().__init__()
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current, key):
        if key < current.key:
            if current.left:
                self._insert_recursive(current.left, key)
            else:
                current.left = Node(key)
        else:
            if current.right:
                self._insert_recursive(current.right, key)
            else:
                current.right = Node(key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current, key):
        if not current:
            return None
        if current.key == key:
            return current
        elif key < current.key:
            return self._search_recursive(current.left, key)
        else:
            return self._search_recursive(current.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal_recursive(self.root, result)
        return result

    def _inorder_traversal_recursive(self, current, result):
        if current:
            self._inorder_traversal_recursive(current.left, result)
            result.append(current.key)
            self._inorder_traversal_recursive(current.right, result)
