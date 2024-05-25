import copy
from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyPrototypePattern(PyDesignPatterns):
    # Prototype Interface
    class GameCharacter(ABC):
        @abstractmethod
        def clone(self):
            pass

    # Concrete Prototype
    class Character(GameCharacter):
        def __init__(self, name: str, health: int, mana: int):
            self.name = name
            self.health = health
            self.mana = mana

        def clone(self):
            return copy.deepcopy(self)

        def __str__(self):
            return f"Character(Name: {self.name}, Health: {self.health}, Mana: {self.mana})"

    def example(self):
        # Original character
        original_character = PyPrototypePattern.Character(
            name="Knight", health=100, mana=50
        )
        print(f"Original: {original_character}")

        # Cloning the character
        cloned_character = original_character.clone()
        cloned_character.name = "Mage"
        cloned_character.health = 80
        cloned_character.mana = 120
        print(f"Cloned: {cloned_character}")

        # Showing that original character is unchanged
        print(f"Unchanged Original: {original_character}")
