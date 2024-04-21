import unittest

from pyPantry.DS.LinkedList.PyDoublyLinkedList import PyDoublyLinkedList


class PyDoublyLinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.empty_dll = PyDoublyLinkedList()
        self.filled_dll = PyDoublyLinkedList()
        self.filled_dll.append(1)
        self.filled_dll.append(2)
        self.filled_dll.append(3)

    def test_append(self):
        self.empty_dll.append(1)
        self.empty_dll.append(2)
        self.assertEqual(self.empty_dll.head.data, 1)
        self.assertEqual(self.empty_dll.head.next.data, 2)
        self.assertEqual(self.empty_dll.head.next.prev.data, 1)

    def test_prepend(self):
        self.empty_dll.prepend(2)
        self.empty_dll.prepend(1)
        self.assertEqual(self.empty_dll.head.data, 1)
        self.assertEqual(self.empty_dll.head.next.data, 2)
        self.assertEqual(self.empty_dll.head.next.prev.data, 1)

    def test_delete(self):
        self.filled_dll.delete(2)
        self.assertEqual(self.filled_dll.head.next.data, 3)
        self.assertEqual(self.filled_dll.head.next.prev.data, 1)

    def test_display(self):
        with self.assertLogs() as logs:
            self.empty_dll.display()
        self.assertEqual(
            logs.output, ["INFO:pyPantry.DS.LinkedList.PyDoublyLinkedList:None"]
        )

        with self.assertLogs() as logs:
            self.filled_dll.display()
        self.assertEqual(
            logs.output,
            [
                "INFO:pyPantry.DS.LinkedList.PyDoublyLinkedList:1",
                "INFO:pyPantry.DS.LinkedList.PyDoublyLinkedList:2",
                "INFO:pyPantry.DS.LinkedList.PyDoublyLinkedList:3",
                "INFO:pyPantry.DS.LinkedList.PyDoublyLinkedList:None",
            ],
        )


if __name__ == "__main__":
    unittest.main()
