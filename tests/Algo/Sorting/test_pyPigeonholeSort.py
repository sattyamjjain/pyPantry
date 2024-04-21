import unittest

from pyPantry.Algo.Sorting.PyPigeonholeSort import PyPigeonholeSort


class PyPigeonholeSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [8, 3, 2, 7, 4, 6, 8]
        sorter = PyPigeonholeSort(arr)
        self.assertEqual(sorter.sort(), [2, 3, 4, 6, 7, 8, 8])

    def test_sort_empty_array(self):
        arr = []
        sorter = PyPigeonholeSort(arr)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        sorter = PyPigeonholeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        sorter = PyPigeonholeSort(arr)
        self.assertEqual(sorter.sort(), [1, 2, 3, 4, 5])

    def test_sort_single_element(self):
        arr = [5]
        sorter = PyPigeonholeSort(arr)
        self.assertEqual(sorter.sort(), [5])


if __name__ == "__main__":
    unittest.main()
