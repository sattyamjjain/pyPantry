import unittest

from pyPantry.DS.LinkedList.PyDoublyCircularLinkedLIst import PyDoublyCircularLinkedList


class PyDoublyCircularLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.dcll = PyDoublyCircularLinkedList()
        self.dcll.append(1)
        self.dcll.append(2)
        self.dcll.append(3)

    def test_append(self):
        self.assertEqual(self.dcll.head.data, 1)
        self.assertEqual(self.dcll.head.next.data, 2)
        self.assertEqual(self.dcll.head.next.next.data, 3)
        self.assertEqual(self.dcll.head.next.next.next.data, 1)
        self.assertEqual(self.dcll.head.prev.data, 3)

    def test_prepend(self):
        self.dcll.prepend(0)
        self.assertEqual(self.dcll.head.data, 0)
        self.assertEqual(self.dcll.head.next.data, 1)
        self.assertEqual(self.dcll.head.next.next.data, 2)
        self.assertEqual(self.dcll.head.next.next.next.data, 3)
        self.assertEqual(self.dcll.head.next.next.next.next.data, 0)
        self.assertEqual(self.dcll.head.prev.data, 3)

    def test_delete(self):
        self.dcll.delete(2)
        self.assertEqual(self.dcll.head.data, 1)
        self.assertEqual(self.dcll.head.next.data, 3)
        self.assertEqual(self.dcll.head.next.next.data, 1)
        self.assertEqual(self.dcll.head.prev.data, 3)

    def test_delete_head(self):
        self.dcll.delete(1)
        self.assertEqual(self.dcll.head.data, 2)
        self.assertEqual(self.dcll.head.next.data, 3)
        self.assertEqual(self.dcll.head.next.next.data, 2)
        self.assertEqual(self.dcll.head.prev.data, 3)

    def test_delete_single_element(self):
        dcll = PyDoublyCircularLinkedList()
        dcll.append(1)
        dcll.delete(1)
        self.assertIsNone(dcll.head)

    def test_delete_nonexistent_element(self):
        self.dcll.delete(4)
        self.assertEqual(self.dcll.head.data, 1)
        self.assertEqual(self.dcll.head.next.data, 2)
        self.assertEqual(self.dcll.head.next.next.data, 3)
        self.assertEqual(self.dcll.head.next.next.next.data, 1)
        self.assertEqual(self.dcll.head.prev.data, 3)


if __name__ == "__main__":
    unittest.main()
