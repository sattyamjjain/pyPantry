import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Structural.Flyweight.PyFlyweightPattern import (
    PyFlyweightPattern,
)


class PyFlyweightPatternTestCase(unittest.TestCase):

    def test_character_factory(self):
        factory = PyFlyweightPattern.CharacterFactory()
        char_a1 = factory.get_character("A")
        char_a2 = factory.get_character("A")
        char_b = factory.get_character("B")

        self.assertIs(char_a1, char_a2)
        self.assertIsNot(char_a1, char_b)

    def test_character_display(self):
        factory = PyFlyweightPattern.CharacterFactory()
        char_a = factory.get_character("A")
        result = char_a.display("Arial", 12)
        self.assertEqual(result, "Character: A, Font: Arial, Size: 12")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyFlyweightPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Character: A, Font: Arial, Size: 12", output)
            self.assertIn("Character: A, Font: Times New Roman, Size: 14", output)
            self.assertIn("Character: B, Font: Verdana, Size: 16", output)
            self.assertIn("char_a1 is char_a2: True", output)


if __name__ == "__main__":
    unittest.main()
