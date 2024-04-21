import unittest

from pyPantry.Algo.Sorting.PyBogoSort import PyBogoSort


class PyBogoSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [3, 2, 1]
        sorter = PyBogoSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyBogoSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3]
        sorter = PyBogoSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyBogoSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
