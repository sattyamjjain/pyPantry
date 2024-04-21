import unittest

from pyPantry.DS.LinkedList.PySkipLinkedList import PySkipLinkedList


class SkipLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.sl = PySkipLinkedList()

    def test_insert_and_search(self):
        self.sl.insert(1)
        self.sl.insert(3)
        self.sl.insert(2)
        self.assertEqual(self.sl.search(1).key, 1)
        self.assertEqual(self.sl.search(2).key, 2)
        self.assertEqual(self.sl.search(3).key, 3)
        self.assertIsNone(self.sl.search(0))
        self.assertIsNone(self.sl.search(4))

    def test_insert_duplicates(self):
        self.sl.insert(1)
        self.sl.insert(1)
        self.sl.insert(1)
        self.assertEqual(self.sl.search(1).key, 1)
        self.assertIsNone(self.sl.search(2))

    def test_random_level(self):
        levels = set()
        for _ in range(100):
            levels.add(self.sl.random_level())
        self.assertTrue(len(levels) > 1)


if __name__ == "__main__":
    unittest.main()
