import unittest

from pyPantry.Algo.Sorting.PyCountingSort import PyCountingSort


class PyCountingSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [64, 25, 12, 22, 11]
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [11, 12, 22, 25, 64])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [5])

    def test_sort_negative_elements(self):
        arr = [-5, -1, -3, -2, -4]
        sorter = PyCountingSort(arr)
        self.assertEqual(sorter.sort(), [-5, -4, -3, -2, -1])


if __name__ == "__main__":
    unittest.main()
