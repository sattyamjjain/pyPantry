import unittest

from pyPantry.DS.Queue.PyCircularQueue import CircularQueue


class CircularQueueTestCase(unittest.TestCase):
    def test_enqueue_dequeue(self):
        cq = CircularQueue(5)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        self.assertEqual(cq.dequeue(), 1)
        self.assertEqual(cq.dequeue(), 2)
        cq.enqueue(4)
        cq.enqueue(5)
        self.assertEqual(cq.dequeue(), 3)
        cq.enqueue(6)
        self.assertEqual(cq.dequeue(), 4)
        self.assertEqual(cq.dequeue(), 5)
        self.assertEqual(cq.dequeue(), 6)
        self.assertRaises(IndexError, cq.dequeue)
        self.assertRaises(IndexError, cq.get_front)
        self.assertRaises(IndexError, cq.get_rear)

    def test_is_empty(self):
        cq = CircularQueue(3)
        self.assertTrue(cq.is_empty())
        cq.enqueue(1)
        self.assertFalse(cq.is_empty())
        cq.dequeue()
        self.assertTrue(cq.is_empty())

    def test_is_full(self):
        cq = CircularQueue(3)
        self.assertFalse(cq.is_full())
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        self.assertTrue(cq.is_full())
        cq.dequeue()
        self.assertFalse(cq.is_full())
        cq.enqueue(4)
        self.assertTrue(cq.is_full())

    def test_get_front_rear(self):
        cq = CircularQueue(4)
        cq.enqueue(1)
        cq.enqueue(2)
        cq.enqueue(3)
        cq.enqueue(4)
        self.assertEqual(cq.get_front(), 1)
        self.assertEqual(cq.get_rear(), 4)
        cq.dequeue()
        self.assertEqual(cq.get_front(), 2)
        self.assertEqual(cq.get_rear(), 4)
        cq.dequeue()
        cq.dequeue()
        self.assertEqual(cq.get_front(), 4)
        self.assertEqual(cq.get_rear(), 4)
        cq.dequeue()
        self.assertRaises(IndexError, cq.get_front)
        self.assertRaises(IndexError, cq.get_rear)


if __name__ == "__main__":
    unittest.main()
