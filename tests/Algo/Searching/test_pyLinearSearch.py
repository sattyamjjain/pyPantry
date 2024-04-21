import unittest

from pyPantry.Algo.Searching.PyLinearSearch import PyLinearSearch


class PyLinearSearchTestCase(unittest.TestCase):

    def test_search_found(self):
        arr = [4, 2, 7, 1, 9, 3]
        searcher = PyLinearSearch(arr)
        self.assertEqual(searcher.search(7), 2)

    def test_search_not_found(self):
        arr = [4, 2, 7, 1, 9, 3]
        searcher = PyLinearSearch(arr)
        self.assertEqual(searcher.search(10), -1)

    def test_search_empty_array(self):
        arr = []
        searcher = PyLinearSearch(arr)
        self.assertEqual(searcher.search(7), -1)


if __name__ == "__main__":
    unittest.main()
