import unittest

from pyPantry.DS.Queue.PyPriorityQueue import PyPriorityQueue


class PriorityQueueTestCase(unittest.TestCase):
    def test_enqueue_dequeue(self):
        pq = PyPriorityQueue()
        pq.enqueue("Task 1", 3)
        pq.enqueue("Task 2", 1)
        pq.enqueue("Task 3", 2)
        self.assertEqual(pq.dequeue(), "Task 2")
        self.assertEqual(pq.dequeue(), "Task 3")
        pq.enqueue("Task 4", 1)
        self.assertEqual(pq.dequeue(), "Task 4")
        self.assertEqual(pq.dequeue(), "Task 1")
        self.assertRaises(IndexError, pq.dequeue)
        self.assertRaises(IndexError, pq.peek)

    def test_is_empty(self):
        pq = PyPriorityQueue()
        self.assertTrue(pq.is_empty())
        pq.enqueue("Task 1", 3)
        self.assertFalse(pq.is_empty())
        pq.dequeue()
        self.assertTrue(pq.is_empty())

    def test_peek(self):
        pq = PyPriorityQueue()
        pq.enqueue("Task 1", 3)
        pq.enqueue("Task 2", 1)
        pq.enqueue("Task 3", 2)
        self.assertEqual(pq.peek(), "Task 2")
        pq.dequeue()
        self.assertEqual(pq.peek(), "Task 3")
        pq.dequeue()
        pq.dequeue()
        self.assertRaises(IndexError, pq.peek)

    def test_size(self):
        pq = PyPriorityQueue()
        self.assertEqual(pq.size(), 0)
        pq.enqueue("Task 1", 3)
        self.assertEqual(pq.size(), 1)
        pq.enqueue("Task 2", 1)
        pq.enqueue("Task 3", 2)
        self.assertEqual(pq.size(), 3)
        pq.dequeue()
        pq.dequeue()
        self.assertEqual(pq.size(), 1)
        pq.dequeue()
        self.assertEqual(pq.size(), 0)


if __name__ == "__main__":
    unittest.main()
