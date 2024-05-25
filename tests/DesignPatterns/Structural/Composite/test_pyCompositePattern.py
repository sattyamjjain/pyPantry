import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Composite.PyCompositePattern import (
    PyCompositePattern,
)


class PyCompositePatternTestCase(unittest.TestCase):

    def test_draw_leaf(self):
        circle = PyCompositePattern.Circle()
        square = PyCompositePattern.Square()
        self.assertEqual(circle.draw(), "Drawing a Circle")
        self.assertEqual(square.draw(), "Drawing a Square")

    def test_draw_composite(self):
        composite = PyCompositePattern.CompositeGraphic()
        circle = PyCompositePattern.Circle()
        square = PyCompositePattern.Square()
        composite.add(circle)
        composite.add(square)
        result = composite.draw()
        expected = "Drawing a Circle\nDrawing a Square"
        self.assertEqual(result, expected)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyCompositePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Drawing a Circle", output)
            self.assertIn("Drawing a Square", output)
            self.assertIn("---", output)


if __name__ == "__main__":
    unittest.main()
