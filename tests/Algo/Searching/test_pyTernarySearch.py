import unittest

from pyPantry.Algo.Searching.PyTernarySearch import PyTernarySearch


class PyTernarySearchTestCase(unittest.TestCase):

    def test_search_found(self):
        arr = [-9, 2, 10, 12, 34, 56, 85, 80, 70, 50, 30]
        searcher = PyTernarySearch(arr)
        self.assertEqual(searcher.search(10), 2)

    def test_search_not_found(self):
        arr = [-9, 2, 10, 12, 34, 56, 85, 80, 70, 50, 30]
        searcher = PyTernarySearch(arr)
        self.assertEqual(searcher.search(100), -1)

    def test_search_empty_array(self):
        arr = []
        searcher = PyTernarySearch(arr)
        self.assertEqual(searcher.search(5), -1)

    def test_search_last_element(self):
        arr = [-9, 2, 10, 12, 30, 34, 50, 56, 70, 80, 85]
        searcher = PyTernarySearch(arr)
        self.assertEqual(searcher.search(30), 4)


if __name__ == "__main__":
    unittest.main()
