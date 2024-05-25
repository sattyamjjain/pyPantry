import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Adapter.PyAdapterPattern import PyAdapterPattern


class PyAdapterPatternTestCase(unittest.TestCase):

    def test_adapter(self):
        legacy_rectangle = PyAdapterPattern.LegacyRectangle()
        adapter = PyAdapterPattern.RectangleAdapter(legacy_rectangle)
        result = adapter.draw()
        self.assertEqual(result, "Drawing a rectangle using LegacyRectangle")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyAdapterPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Drawing a rectangle using LegacyRectangle", output)


if __name__ == "__main__":
    unittest.main()
