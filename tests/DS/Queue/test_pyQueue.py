import unittest

from pyPantry.DS.Queue.PyQueue import PyQueue


class PyQueueTestCase(unittest.TestCase):
    def test_empty_queue(self):
        queue = PyQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(queue.size(), 0)
        self.assertRaises(IndexError, queue.dequeue)
        self.assertRaises(IndexError, queue.front)

    def test_enqueue_dequeue(self):
        queue = PyQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertFalse(queue.is_empty())
        self.assertEqual(queue.size(), 3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.front(), 3)
        self.assertEqual(queue.size(), 1)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())
        self.assertRaises(IndexError, queue.dequeue)
        self.assertRaises(IndexError, queue.front)


if __name__ == "__main__":
    unittest.main()
