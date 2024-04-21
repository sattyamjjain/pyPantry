import unittest

from pyPantry.DS.Tree.PyBTree import PyBTree


class TestBTree(unittest.TestCase):
    def setUp(self):
        self.bt = PyBTree(t=2)

    def test_insert_and_search(self):
        self.bt.insert(5)
        self.bt.insert(3)
        self.bt.insert(7)
        self.bt.insert(2)
        self.bt.insert(4)
        self.bt.insert(6)
        self.bt.insert(8)

        self.assertEqual(self.bt.search(5).keys[0], (5, None))
        self.assertEqual(self.bt.search(2).keys[0], (2, None))
        self.assertEqual(self.bt.search(8).keys[0], (6, None))
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

    def test_delete(self):
        self.bt.insert(5)
        self.bt.insert(3)
        self.bt.insert(7)
        self.bt.insert(2)
        self.bt.insert(4)
        self.bt.insert(6)
        self.bt.insert(8)

        self.bt.delete(5)
        self.bt.delete(2)

        self.assertEqual(self.bt.inorder_traversal(), [3, 4, 6, 7, 8])

    def test_delete_nonexistent_key(self):
        self.bt.insert(5)
        self.bt.insert(3)
        self.bt.insert(7)

        self.bt.delete(6)

        self.assertEqual(self.bt.inorder_traversal(), [3, 5, 7])

    def test_empty_tree(self):
        self.assertIsNone(self.bt.search(5))
        self.assertEqual(self.bt.inorder_traversal(), [])


if __name__ == "__main__":
    unittest.main()
