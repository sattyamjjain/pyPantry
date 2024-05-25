from typing import Dict

from pyPantry.DesignPatterns import PyDesignPatterns


class PyFlyweightPattern(PyDesignPatterns):
    # Flyweight
    class Character:
        def __init__(self, char: str):
            self.char = char

        def display(self, font: str, size: int) -> str:
            return f"Character: {self.char}, Font: {font}, Size: {size}"

    # Flyweight Factory
    class CharacterFactory:
        _characters: Dict[str, "PyFlyweightPattern.Character"] = {}

        @classmethod
        def get_character(cls, char: str) -> "PyFlyweightPattern.Character":
            if char not in cls._characters:
                cls._characters[char] = PyFlyweightPattern.Character(char)
            return cls._characters[char]

    def example(self):
        factory = PyFlyweightPattern.CharacterFactory()

        # Create characters
        char_a1 = factory.get_character("A")
        char_a2 = factory.get_character("A")
        char_b = factory.get_character("B")

        # Display characters
        print(char_a1.display("Arial", 12))
        print(char_a2.display("Times New Roman", 14))
        print(char_b.display("Verdana", 16))

        # Verify that the same object is used for 'A'
        print(f"char_a1 is char_a2: {char_a1 is char_a2}")
