import unittest

from pyPantry.Algo.Sorting.Py3WayMergeSort import Py3WayMergeSort


class Py3WayMergeSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [34, 2, 10, -9, 56, 85, 12, 3, 0, 11]
        sorter = Py3WayMergeSort(arr)
        self.assertEqual(sorter.sort(), [-9, 0, 2, 3, 10, 11, 12, 34, 56, 85])

    def test_sort_empty_array(self):
        arr = []
        sorter = Py3WayMergeSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = Py3WayMergeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = Py3WayMergeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = Py3WayMergeSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
