import unittest

from pyDSAlgo.DS.Stack.PyStack import PyStack


class PyStackTestCase(unittest.TestCase):
    def test_empty_stack(self):
        stack = PyStack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(stack.size(), 0)
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)

    def test_push_pop(self):
        stack = PyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertFalse(stack.is_empty())
        self.assertEqual(stack.size(), 3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.peek(), 1)
        self.assertEqual(stack.size(), 1)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())
        self.assertRaises(IndexError, stack.pop)
        self.assertRaises(IndexError, stack.peek)


if __name__ == "__main__":
    unittest.main()
