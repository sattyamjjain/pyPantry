import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Interpreter.PyInterpreterPattern import (
    PyInterpreterPattern,
)


class PyInterpreterPatternTestCase(unittest.TestCase):

    def test_number_expression(self):
        number = PyInterpreterPattern.Number(10)
        context = {}
        self.assertEqual(number.interpret(context), 10)

    def test_plus_expression(self):
        left = PyInterpreterPattern.Number(5)
        right = PyInterpreterPattern.Number(10)
        plus = PyInterpreterPattern.Plus(left, right)
        context = {}
        self.assertEqual(plus.interpret(context), 15)

    def test_minus_expression(self):
        left = PyInterpreterPattern.Number(10)
        right = PyInterpreterPattern.Number(5)
        minus = PyInterpreterPattern.Minus(left, right)
        context = {}
        self.assertEqual(minus.interpret(context), 5)

    def test_complex_expression(self):
        expression = PyInterpreterPattern.Minus(
            PyInterpreterPattern.Plus(
                PyInterpreterPattern.Number(5), PyInterpreterPattern.Number(10)
            ),
            PyInterpreterPattern.Plus(
                PyInterpreterPattern.Number(2), PyInterpreterPattern.Number(3)
            ),
        )
        context = {}
        self.assertEqual(expression.interpret(context), 10)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyInterpreterPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("The result of the expression is: 10", output)


if __name__ == "__main__":
    unittest.main()
