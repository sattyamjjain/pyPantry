import unittest

from pyDSAlgo.DS.Heap.PyMaxHeap import PyMaxHeap


class MaxHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.max_heap = PyMaxHeap()

    def test_insert(self):
        self.max_heap.insert(5)
        self.assertEqual(self.max_heap.get_max(), 5)

        self.max_heap.insert(3)
        self.assertEqual(self.max_heap.get_max(), 5)

        self.max_heap.insert(7)
        self.assertEqual(self.max_heap.get_max(), 7)

        self.max_heap.insert(2)
        self.assertEqual(self.max_heap.get_max(), 7)

        self.max_heap.insert(4)
        self.assertEqual(self.max_heap.get_max(), 7)

        self.max_heap.insert(6)
        self.assertEqual(self.max_heap.get_max(), 7)

    def test_extract_max(self):
        self.max_heap.insert(5)
        self.max_heap.insert(3)
        self.max_heap.insert(7)
        self.max_heap.insert(2)
        self.max_heap.insert(4)
        self.max_heap.insert(6)

        self.assertEqual(self.max_heap.extract_max(), 7)
        self.assertEqual(self.max_heap.extract_max(), 6)
        self.assertEqual(self.max_heap.extract_max(), 5)
        self.assertEqual(self.max_heap.extract_max(), 4)
        self.assertEqual(self.max_heap.extract_max(), 3)
        self.assertEqual(self.max_heap.extract_max(), 2)
        self.assertIsNone(self.max_heap.extract_max())

    def test_get_max(self):
        self.assertIsNone(self.max_heap.get_max())

        self.max_heap.insert(5)
        self.assertEqual(self.max_heap.get_max(), 5)

        self.max_heap.insert(3)
        self.assertEqual(self.max_heap.get_max(), 5)

    def test_is_empty(self):
        self.assertTrue(self.max_heap.is_empty())

        self.max_heap.insert(5)
        self.assertFalse(self.max_heap.is_empty())

        self.max_heap.extract_max()
        self.assertTrue(self.max_heap.is_empty())


if __name__ == "__main__":
    unittest.main()
