import unittest

from pyPantry.DS.LinkedList.PyLinkedList import PyLinkedList


class PyLinkedListTestCase(unittest.TestCase):
    def test_empty_linked_list(self):
        linked_list = PyLinkedList()
        self.assertTrue(linked_list.is_empty())

    def test_insertion_and_deletion(self):
        linked_list = PyLinkedList()
        linked_list.insert_at_beginning(10)
        linked_list.insert_at_end(20)
        linked_list.insert_at_end(30)
        self.assertFalse(linked_list.is_empty())

        linked_list.delete(20)
        self.assertEqual(linked_list.head.data, 10)
        self.assertEqual(linked_list.head.next.data, 30)

        linked_list.delete(10)
        self.assertEqual(linked_list.head.data, 30)

        linked_list.delete(30)
        self.assertTrue(linked_list.is_empty())


if __name__ == "__main__":
    unittest.main()
