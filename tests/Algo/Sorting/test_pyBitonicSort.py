import unittest

from pyPantry.Algo.Sorting.PyBitonicSort import PyBitonicSort


class PyBitonicSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [3, 7, 4, 8, 6, 2, 1, 5]
        sorter = PyBitonicSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyBitonicSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8]
        sorter = PyBitonicSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sort_reverse_sorted(self):
        arr = [8, 7, 6, 5, 4, 3, 2, 1]
        sorter = PyBitonicSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyBitonicSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
