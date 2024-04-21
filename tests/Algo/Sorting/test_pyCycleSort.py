import unittest

from pyPantry.Algo.Sorting.PyCycleSort import PyCycleSort


class PyCycleSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [5, 2, 9, 1, 5, 6]
        sorter = PyCycleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 5, 5, 6, 9])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyCycleSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyCycleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyCycleSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyCycleSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
