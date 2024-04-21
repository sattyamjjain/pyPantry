import unittest

from pyPantry.DS.Queue.PyDeque import PyDeque


class DequeTestCase(unittest.TestCase):
    def test_add_remove_front(self):
        d = PyDeque()
        d.add_front(1)
        d.add_front(2)
        self.assertEqual(d.remove_front(), 2)
        self.assertEqual(d.remove_front(), 1)
        self.assertRaises(IndexError, d.remove_front)

    def test_add_remove_rear(self):
        d = PyDeque()
        d.add_rear(1)
        d.add_rear(2)
        self.assertEqual(d.remove_rear(), 2)
        self.assertEqual(d.remove_rear(), 1)
        self.assertRaises(IndexError, d.remove_rear)

    def test_peek_front(self):
        d = PyDeque()
        d.add_front(1)
        d.add_front(2)
        self.assertEqual(d.peek_front(), 2)
        d.remove_front()
        self.assertEqual(d.peek_front(), 1)
        d.remove_front()
        self.assertRaises(IndexError, d.peek_front)

    def test_peek_rear(self):
        d = PyDeque()
        d.add_rear(1)
        d.add_rear(2)
        self.assertEqual(d.peek_rear(), 2)
        d.remove_rear()
        self.assertEqual(d.peek_rear(), 1)
        d.remove_rear()
        self.assertRaises(IndexError, d.peek_rear)

    def test_is_empty(self):
        d = PyDeque()
        self.assertTrue(d.is_empty())
        d.add_front(1)
        self.assertFalse(d.is_empty())
        d.remove_front()
        self.assertTrue(d.is_empty())

    def test_size(self):
        d = PyDeque()
        self.assertEqual(d.size(), 0)
        d.add_front(1)
        self.assertEqual(d.size(), 1)
        d.add_rear(2)
        self.assertEqual(d.size(), 2)
        d.remove_front()
        self.assertEqual(d.size(), 1)
        d.remove_rear()
        self.assertEqual(d.size(), 0)


if __name__ == "__main__":
    unittest.main()
