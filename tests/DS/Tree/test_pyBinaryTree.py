import unittest

from pyDSAlgo.DS.Tree.PyBinaryTree import PyBinaryTree


class BinaryTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.bt = PyBinaryTree()

    def test_insert_and_search(self):
        self.bt.insert(5)
        self.bt.insert(3)
        self.bt.insert(7)
        self.bt.insert(2)
        self.bt.insert(4)
        self.bt.insert(6)
        self.bt.insert(8)

        self.assertEqual(self.bt.search(5).key, 5)
        self.assertEqual(self.bt.search(2).key, 2)
        self.assertEqual(self.bt.search(8).key, 8)
        self.assertIsNone(self.bt.search(9))

    def test_inorder_traversal(self):
        self.bt.insert(5)
        self.bt.insert(3)
        self.bt.insert(7)
        self.bt.insert(2)
        self.bt.insert(4)
        self.bt.insert(6)
        self.bt.insert(8)

        self.assertEqual(self.bt.inorder_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_empty_tree(self):
        self.assertIsNone(self.bt.search(5))
        self.assertEqual(self.bt.inorder_traversal(), [])


if __name__ == "__main__":
    unittest.main()
