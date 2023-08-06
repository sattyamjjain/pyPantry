import unittest

from pyDSAlgo.DS.Tree.PyAVLTree import PyAVLTree


class AVLTreeTestCase(unittest.TestCase):
    def setUp(self):
        self.avl = PyAVLTree()

    def test_insert_and_search(self):
        self.avl.insert(5)
        self.avl.insert(3)
        self.avl.insert(7)
        self.avl.insert(2)
        self.avl.insert(4)
        self.avl.insert(6)
        self.avl.insert(8)

        self.assertEqual(self.avl.search(5).key, 5)
        self.assertEqual(self.avl.search(2).key, 2)
        self.assertEqual(self.avl.search(8).key, 8)
        self.assertIsNone(self.avl.search(9))

    def test_inorder_traversal(self):
        self.avl.insert(5)
        self.avl.insert(3)
        self.avl.insert(7)
        self.avl.insert(2)
        self.avl.insert(4)
        self.avl.insert(6)
        self.avl.insert(8)

        self.assertEqual(self.avl.inorder_traversal(), [2, 3, 4, 5, 6, 7, 8])

    def test_insert_duplicates(self):
        self.avl.insert(5)
        self.avl.insert(5)
        self.avl.insert(5)
        self.assertEqual(self.avl.inorder_traversal(), [5])

    def test_empty_tree(self):
        self.assertIsNone(self.avl.search(5))
        self.assertEqual(self.avl.inorder_traversal(), [])


if __name__ == "__main__":
    unittest.main()
