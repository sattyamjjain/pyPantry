import unittest

from pyDSAlgo.DS.Heap.PyMinHeap import PyMinHeap


class MinHeapTestCase(unittest.TestCase):
    def setUp(self):
        self.min_heap = PyMinHeap()

    def test_insert(self):
        self.min_heap.insert(5)
        self.assertEqual(self.min_heap.get_min(), 5)

        self.min_heap.insert(3)
        self.assertEqual(self.min_heap.get_min(), 3)

        self.min_heap.insert(7)
        self.assertEqual(self.min_heap.get_min(), 3)

        self.min_heap.insert(2)
        self.assertEqual(self.min_heap.get_min(), 2)

        self.min_heap.insert(4)
        self.assertEqual(self.min_heap.get_min(), 2)

        self.min_heap.insert(6)
        self.assertEqual(self.min_heap.get_min(), 2)

    def test_extract_min(self):
        self.min_heap.insert(5)
        self.min_heap.insert(3)
        self.min_heap.insert(7)
        self.min_heap.insert(2)
        self.min_heap.insert(4)
        self.min_heap.insert(6)

        self.assertEqual(self.min_heap.extract_min(), 2)
        self.assertEqual(self.min_heap.extract_min(), 3)
        self.assertEqual(self.min_heap.extract_min(), 4)
        self.assertEqual(self.min_heap.extract_min(), 5)
        self.assertEqual(self.min_heap.extract_min(), 6)
        self.assertEqual(self.min_heap.extract_min(), 7)
        self.assertIsNone(self.min_heap.extract_min())

    def test_get_min(self):
        self.assertIsNone(self.min_heap.get_min())

        self.min_heap.insert(5)
        self.assertEqual(self.min_heap.get_min(), 5)

        self.min_heap.insert(3)
        self.assertEqual(self.min_heap.get_min(), 3)

    def test_is_empty(self):
        self.assertTrue(self.min_heap.is_empty())

        self.min_heap.insert(5)
        self.assertFalse(self.min_heap.is_empty())

        self.min_heap.extract_min()
        self.assertTrue(self.min_heap.is_empty())


if __name__ == "__main__":
    unittest.main()
