from pyPantry.Algo import PyAlgo


class PyTreeSort(PyAlgo):
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def insert(self, root, key):
        if root is None:
            return self.Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def inorder_traversal(self, root, res):
        if root:
            self.inorder_traversal(root.left, res)
            res.append(root.val)
            self.inorder_traversal(root.right, res)

    def sort(self):
        root = None
        for key in self.arr:
            root = self.insert(root, key)

        res = []
        self.inorder_traversal(root, res)
        return res
