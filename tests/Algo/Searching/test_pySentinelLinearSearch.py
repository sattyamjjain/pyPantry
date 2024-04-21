import unittest

from pyPantry.Algo.Searching.PySentinelLinearSearch import PySentinelLinearSearch


class PySentinelLinearSearchTestCase(unittest.TestCase):

    def test_search_found(self):
        arr = [34, 2, 10, -9, 56, 85, 12]
        searcher = PySentinelLinearSearch(arr)
        self.assertEqual(searcher.search(10), 2)

    def test_search_not_found(self):
        arr = [34, 2, 10, -9, 56, 85, 12]
        searcher = PySentinelLinearSearch(arr)
        self.assertEqual(searcher.search(100), -1)

    def test_search_empty_array(self):
        arr = []
        searcher = PySentinelLinearSearch(arr)
        self.assertEqual(searcher.search(5), -1)

    def test_search_last_element(self):
        arr = [34, 2, 10, -9, 56, 85, 12]
        searcher = PySentinelLinearSearch(arr)
        self.assertEqual(searcher.search(12), 6)


if __name__ == "__main__":
    unittest.main()
