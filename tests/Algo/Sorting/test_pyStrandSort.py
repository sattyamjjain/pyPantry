import unittest

from pyPantry.Algo.Sorting.PyStrandSort import PyStrandSort


class PyStrandSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [10, 2, 3, 1, 6, 5, 7, 4, 9, 8]
        sorter = PyStrandSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyStrandSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyStrandSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyStrandSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyStrandSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
