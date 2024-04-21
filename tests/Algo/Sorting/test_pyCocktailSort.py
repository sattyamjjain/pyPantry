import unittest

from pyPantry.Algo.Sorting.PyCocktailSort import PyCocktailSort


class PyCocktailSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [5, 1, 4, 2, 8, 0, 2]
        sorter = PyCocktailSort(arr)
        self.assertEqual(sorter.sort(), [0, 1, 2, 2, 4, 5, 8])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyCocktailSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyCocktailSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyCocktailSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyCocktailSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
