import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Decorator.PyDecoratorPattern import (
    PyDecoratorPattern,
)


class PyDecoratorPatternTestCase(unittest.TestCase):

    def test_plain_text(self):
        text = PyDecoratorPattern.PlainText("Hello, World!")
        self.assertEqual(text.render(), "Hello, World!")

    def test_bold_decorator(self):
        text = PyDecoratorPattern.PlainText("Hello, World!")
        bold_text = PyDecoratorPattern.BoldDecorator(text)
        self.assertEqual(bold_text.render(), "<b>Hello, World!</b>")

    def test_italic_decorator(self):
        text = PyDecoratorPattern.PlainText("Hello, World!")
        italic_text = PyDecoratorPattern.ItalicDecorator(text)
        self.assertEqual(italic_text.render(), "<i>Hello, World!</i>")

    def test_underline_decorator(self):
        text = PyDecoratorPattern.PlainText("Hello, World!")
        underlined_text = PyDecoratorPattern.UnderlineDecorator(text)
        self.assertEqual(underlined_text.render(), "<u>Hello, World!</u>")

    def test_combined_decorators(self):
        text = PyDecoratorPattern.PlainText("Hello, World!")
        decorated_text = PyDecoratorPattern.UnderlineDecorator(
            PyDecoratorPattern.ItalicDecorator(PyDecoratorPattern.BoldDecorator(text))
        )
        self.assertEqual(decorated_text.render(), "<u><i><b>Hello, World!</b></i></u>")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyDecoratorPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Plain Text: Hello, World!", output)
            self.assertIn("Bold Text: <b>Hello, World!</b>", output)
            self.assertIn("Italic Bold Text: <i><b>Hello, World!</b></i>", output)
            self.assertIn(
                "Underlined Italic Bold Text: <u><i><b>Hello, World!</b></i></u>",
                output,
            )


if __name__ == "__main__":
    unittest.main()
