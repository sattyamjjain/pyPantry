import unittest

from pyPantry.Algo.Sorting.PyCombSort import PyCombSort


class PyCombSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [64, 34, 25, 12, 22, 11, 90]
        sorter = PyCombSort(arr)
        self.assertEqual(sorter.sort(), [11, 12, 22, 25, 34, 64, 90])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyCombSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyCombSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyCombSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyCombSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
