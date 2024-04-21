import unittest

from pyPantry.Algo.Sorting.PyPancakeSort import PyPancakeSort


class PyPancakeSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [23, 10, 20, 11, 12, 6, 7]
        sorter = PyPancakeSort(arr)
        self.assertEqual(sorter.sort(), [6, 7, 10, 11, 12, 20, 23])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyPancakeSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyPancakeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyPancakeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyPancakeSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
