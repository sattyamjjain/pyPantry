import unittest

from pyPantry.Algo.Searching.PyExponentialSearch import PyExponentialSearch


class PyExponentialSearchTestCase(unittest.TestCase):

    def test_search_found(self):
        arr = [-9, 2, 10, 12, 34, 56, 85]
        searcher = PyExponentialSearch(arr)
        self.assertEqual(searcher.search(10), 2)

    def test_search_not_found(self):
        arr = [-9, 2, 10, 12, 34, 56, 85]
        searcher = PyExponentialSearch(arr)
        self.assertEqual(searcher.search(100), -1)

    def test_search_empty_array(self):
        arr = []
        searcher = PyExponentialSearch(arr)
        self.assertEqual(searcher.search(5), -1)

    def test_search_last_element(self):
        arr = [-9, 2, 10, 12, 34, 56, 85]
        searcher = PyExponentialSearch(arr)
        self.assertEqual(searcher.search(85), 6)


if __name__ == "__main__":
    unittest.main()
