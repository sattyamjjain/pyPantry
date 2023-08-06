import unittest

from pyDSAlgo.DS.Stack.pyLinkedStack import PyLinkedStack


class LinkedStackTestCase(unittest.TestCase):
    def test_push_pop(self):
        stack = PyLinkedStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertRaises(IndexError, stack.pop)

    def test_peek(self):
        stack = PyLinkedStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)
        stack.pop()
        self.assertRaises(IndexError, stack.peek)

    def test_is_empty(self):
        stack = PyLinkedStack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_get_size(self):
        stack = PyLinkedStack()
        self.assertEqual(stack.get_size(), 0)
        stack.push(1)
        self.assertEqual(stack.get_size(), 1)
        stack.push(2)
        self.assertEqual(stack.get_size(), 2)
        stack.pop()
        self.assertEqual(stack.get_size(), 1)
        stack.pop()
        self.assertEqual(stack.get_size(), 0)


if __name__ == "__main__":
    unittest.main()
