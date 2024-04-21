import unittest

from pyPantry.Algo.Sorting.PyBIngoSort import PyBingoSort


class PyBingoSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [5, 3, 2, 4, 3, 1]
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 3, 4, 5])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [5])

    def test_sort_all_same_elements(self):
        arr = [5, 5, 5, 5, 5]
        sorter = PyBingoSort(arr)
        self.assertEqual(sorter.sort(), [5, 5, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()
