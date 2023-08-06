import unittest

from pyDSAlgo.DS.Tree.PyBinarySearchTree import PyBinarySearchTree


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self):
        self.bst = PyBinarySearchTree()

    def test_insert(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        expected = [20, 30, 40, 50, 60, 70, 80]
        result = self._inorder_traversal_values()
        self.assertEqual(result, expected)

    def test_search(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        self.assertIsNotNone(self.bst.search(40))
        self.assertIsNone(self.bst.search(100))

    def test_delete(self):
        self.bst.insert(50)
        self.bst.insert(30)
        self.bst.insert(70)
        self.bst.insert(20)
        self.bst.insert(40)
        self.bst.insert(60)
        self.bst.insert(80)

        self.bst.delete(30)
        self.bst.delete(80)

        expected = [20, 40, 50, 60, 70]
        result = self._inorder_traversal_values()
        self.assertEqual(result, expected)

    def _inorder_traversal_values(self):
        result = []

        def inorder_helper(node):
            if node is not None:
                inorder_helper(node.left)
                result.append(node.key)
                inorder_helper(node.right)

        inorder_helper(self.bst.root)
        return result


if __name__ == "__main__":
    unittest.main()
