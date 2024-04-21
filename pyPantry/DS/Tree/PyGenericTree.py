from pyPantry.DS import PyDS


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


class PyGenericTree(PyDS):
    def __init__(self):
        super().__init__()
        self.root = None

    def is_empty(self):
        return self.root is None

    def add_root(self, data):
        if self.is_empty():
            self.root = TreeNode(data)
        else:
            raise ValueError("Root already exists.")

    def add_child(self, parent, data):
        if parent is None:
            raise ValueError("Invalid parent node.")
        if self.is_empty():
            raise ValueError("Tree is empty. Cannot add child.")
        node = TreeNode(data)
        parent.children.append(node)

    def get_root(self):
        if self.is_empty():
            raise ValueError("Tree is empty. No root node.")
        return self.root

    @staticmethod
    def get_children(parent):
        if parent is None:
            raise ValueError("Invalid parent node.")
        return parent.children

    def traverse_pre_order(self, node):
        if node is None:
            return []
        captured_output = [node.data]
        for child in node.children:
            captured_output.extend(self.traverse_pre_order(child))
        return captured_output

    def traverse_post_order(self, node):
        if node is None:
            return []
        captured_output = []
        for child in node.children:
            captured_output.extend(self.traverse_post_order(child))
        captured_output.append(node.data)
        return captured_output

    def traverse_level_order(self):
        if self.is_empty():
            return []
        queue = [self.root]
        captured_output = []
        while queue:
            node = queue.pop(0)
            captured_output.append(node.data)
            queue.extend(node.children)
        return captured_output
