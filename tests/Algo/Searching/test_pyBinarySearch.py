import unittest

from pyPantry.Algo.Searching.PyBinarySearch import PyBinarySearch


class PyBinarySearchTestCase(unittest.TestCase):

    def test_search_found(self):
        arr = [1, 2, 3, 4, 7, 9]
        searcher = PyBinarySearch(arr)
        self.assertEqual(searcher.search(7), 4)

    def test_search_not_found(self):
        arr = [1, 2, 3, 4, 7, 9]
        searcher = PyBinarySearch(arr)
        self.assertEqual(searcher.search(10), -1)

    def test_search_empty_array(self):
        arr = []
        searcher = PyBinarySearch(arr)
        self.assertEqual(searcher.search(7), -1)

    def test_search_single_element_found(self):
        arr = [5]
        searcher = PyBinarySearch(arr)
        self.assertEqual(searcher.search(5), 0)

    def test_search_single_element_not_found(self):
        arr = [5]
        searcher = PyBinarySearch(arr)
        self.assertEqual(searcher.search(7), -1)


if __name__ == "__main__":
    unittest.main()
