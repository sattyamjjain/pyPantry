import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Creational.Prototype.PyPrototypePattern import (
    PyPrototypePattern,
)


class PyPrototypePatternTestCase(unittest.TestCase):

    def test_clone_character(self):
        original_character = PyPrototypePattern.Character(
            name="Knight", health=100, mana=50
        )
        cloned_character = original_character.clone()
        self.assertNotEqual(id(original_character), id(cloned_character))
        self.assertEqual(original_character.name, cloned_character.name)
        self.assertEqual(original_character.health, cloned_character.health)
        self.assertEqual(original_character.mana, cloned_character.mana)

    def test_clone_character_modification(self):
        original_character = PyPrototypePattern.Character(
            name="Knight", health=100, mana=50
        )
        cloned_character = original_character.clone()
        cloned_character.name = "Mage"
        cloned_character.health = 80
        cloned_character.mana = 120
        self.assertNotEqual(original_character.name, cloned_character.name)
        self.assertNotEqual(original_character.health, cloned_character.health)
        self.assertNotEqual(original_character.mana, cloned_character.mana)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyPrototypePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn(
                "Original: Character(Name: Knight, Health: 100, Mana: 50)", output
            )
            self.assertIn(
                "Cloned: Character(Name: Mage, Health: 80, Mana: 120)", output
            )
            self.assertIn(
                "Unchanged Original: Character(Name: Knight, Health: 100, Mana: 50)",
                output,
            )


if __name__ == "__main__":
    unittest.main()
