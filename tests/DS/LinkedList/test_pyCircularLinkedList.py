import unittest

from pyPantry.DS.LinkedList.PyCircularLinkedList import PyCircularLinkedList


class PyCircularLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.cll = PyCircularLinkedList()
        self.cll.append(1)
        self.cll.append(2)
        self.cll.append(3)

    def test_append(self):
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 2)
        self.assertEqual(self.cll.head.next.next.data, 3)
        self.assertEqual(self.cll.head.next.next.next.data, 1)

    def test_prepend(self):
        self.cll.prepend(0)
        self.assertEqual(self.cll.head.data, 0)
        self.assertEqual(self.cll.head.next.data, 1)
        self.assertEqual(self.cll.head.next.next.data, 2)
        self.assertEqual(self.cll.head.next.next.next.data, 3)
        self.assertEqual(self.cll.head.next.next.next.next.data, 0)

    def test_delete(self):
        self.cll.delete(2)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 3)
        self.assertEqual(self.cll.head.next.next.data, 1)

    def test_delete_head(self):
        self.cll.delete(1)
        self.assertEqual(self.cll.head.data, 2)
        self.assertEqual(self.cll.head.next.data, 3)
        self.assertEqual(self.cll.head.next.next.data, 2)

    def test_delete_single_element(self):
        cll = PyCircularLinkedList()
        cll.append(1)
        cll.delete(1)
        self.assertIsNone(cll.head)

    def test_delete_nonexistent_element(self):
        self.cll.delete(4)
        self.assertEqual(self.cll.head.data, 1)
        self.assertEqual(self.cll.head.next.data, 2)
        self.assertEqual(self.cll.head.next.next.data, 3)
        self.assertEqual(self.cll.head.next.next.next.data, 1)


if __name__ == "__main__":
    unittest.main()
