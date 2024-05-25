import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Visitor.PyVisitorPattern import PyVisitorPattern


class PyVisitorPatternTestCase(unittest.TestCase):

    def test_render_visitor(self):
        elements = [
            PyVisitorPattern.TextElement("Hello, World!"),
            PyVisitorPattern.ImageElement("http://example.com/image.jpg"),
            PyVisitorPattern.TableElement(3, 5),
        ]
        visitor = PyVisitorPattern.RenderVisitor()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            for element in elements:
                element.accept(visitor)
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Rendering text: Hello, World!", output)
            self.assertIn(
                "Rendering image from URL: http://example.com/image.jpg", output
            )
            self.assertIn("Rendering table with 3 rows and 5 columns", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyVisitorPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Rendering text: Hello, World!", output)
            self.assertIn(
                "Rendering image from URL: http://example.com/image.jpg", output
            )
            self.assertIn("Rendering table with 3 rows and 5 columns", output)


if __name__ == "__main__":
    unittest.main()
