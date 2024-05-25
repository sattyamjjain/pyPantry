import unittest

from pyPantry.Algo.Sorting.PyBucketSort import PyBucketSort


class PyBucketSortTestCase(unittest.TestCase):

    def test_sort_basic(self):
        arr = [0.79, 0.13, 0.16, 0.64, 0.39, 0.20, 0.89, 0.53, 0.71, 0.42]
        num_buckets = 5
        sorter = PyBucketSort(arr, num_buckets)
        self.assertEqual(
            sorter.sort(), [0.13, 0.16, 0.20, 0.39, 0.42, 0.53, 0.64, 0.71, 0.79, 0.89]
        )

    def test_sort_empty_array(self):
        arr = []
        num_buckets = 5
        sorter = PyBucketSort(arr, num_buckets)
        self.assertEqual(sorter.sort(), [])

    def test_sort_already_sorted(self):
        arr = [0.1, 0.2, 0.3, 0.4, 0.5]
        num_buckets = 5
        sorter = PyBucketSort(arr, num_buckets)
        self.assertEqual(sorter.sort(), [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_sort_reverse_sorted(self):
        arr = [0.5, 0.4, 0.3, 0.2, 0.1]
        num_buckets = 5
        sorter = PyBucketSort(arr, num_buckets)
        self.assertEqual(sorter.sort(), [0.1, 0.2, 0.3, 0.4, 0.5])

    def test_sort_single_element(self):
        arr = [0.5]
        num_buckets = 1
        sorter = PyBucketSort(arr, num_buckets)
        self.assertEqual(sorter.sort(), [0.5])


if __name__ == "__main__":
    unittest.main()
