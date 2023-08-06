import unittest

from pyDSAlgo.DS.LinkedList.PyHeaderLinkedList import PyHeaderLinkedList


class PyHeaderLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.hll = PyHeaderLinkedList()
        self.hll.append(1)
        self.hll.append(2)
        self.hll.append(3)

    def test_append(self):
        self.assertEqual(self.hll.length, 3)
        self.assertEqual(self.hll.header.next.data, 1)
        self.assertEqual(self.hll.header.next.next.data, 2)
        self.assertEqual(self.hll.header.next.next.next.data, 3)

    def test_prepend(self):
        self.hll.prepend(0)
        self.assertEqual(self.hll.length, 4)
        self.assertEqual(self.hll.header.next.data, 0)
        self.assertEqual(self.hll.header.next.next.data, 1)
        self.assertEqual(self.hll.header.next.next.next.data, 2)
        self.assertEqual(self.hll.header.next.next.next.next.data, 3)

    def test_delete(self):
        self.hll.delete(2)
        self.assertEqual(self.hll.length, 2)
        self.assertEqual(self.hll.header.next.data, 1)
        self.assertEqual(self.hll.header.next.next.data, 3)

    def test_delete_nonexistent_element(self):
        self.hll.delete(4)
        self.assertEqual(self.hll.length, 3)
        self.assertEqual(self.hll.header.next.data, 1)
        self.assertEqual(self.hll.header.next.next.data, 2)
        self.assertEqual(self.hll.header.next.next.next.data, 3)

    def test_display(self):
        with self.assertLogs() as logs:
            self.hll.display()
        self.assertEqual(
            logs.output,
            ["INFO:pyDSAlgo.DS.LinkedList.PyHeaderLinkedList:1 -> 2 -> 3 -> None"],
        )

    def test_empty_list(self):
        empty_hll = PyHeaderLinkedList()
        self.assertEqual(empty_hll.length, 0)
        self.assertIsNone(empty_hll.header.next)


if __name__ == "__main__":
    unittest.main()
