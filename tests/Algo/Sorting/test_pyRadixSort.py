import unittest

from pyPantry.Algo.Sorting.PyRadixSort import PyRadixSort


class PyRadixSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        sorter = PyRadixSort(arr)
        self.assertEqual(sorter.sort(), [2, 24, 45, 66, 75, 90, 170, 802])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyRadixSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyRadixSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyRadixSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyRadixSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
