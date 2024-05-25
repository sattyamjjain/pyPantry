from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyCompositePattern(PyDesignPatterns):
    # Component
    class Graphic(ABC):
        @abstractmethod
        def draw(self) -> str:
            pass

    # Leaf
    class Circle(Graphic):
        def draw(self) -> str:
            return "Drawing a Circle"

    class Square(Graphic):
        def draw(self) -> str:
            return "Drawing a Square"

    # Composite
    class CompositeGraphic(Graphic):
        def __init__(self):
            self.children: List["PyCompositePattern.Graphic"] = []

        def add(self, graphic: "PyCompositePattern.Graphic") -> None:
            self.children.append(graphic)

        def remove(self, graphic: "PyCompositePattern.Graphic") -> None:
            self.children.remove(graphic)

        def draw(self) -> str:
            results = [child.draw() for child in self.children]
            return "\n".join(results)

    def example(self):
        # Creating simple graphics
        circle = PyCompositePattern.Circle()
        square = PyCompositePattern.Square()

        # Creating composite graphic
        composite = PyCompositePattern.CompositeGraphic()
        composite.add(circle)
        composite.add(square)

        # Creating another composite graphic
        another_composite = PyCompositePattern.CompositeGraphic()
        another_composite.add(composite)
        another_composite.add(circle)

        print(composite.draw())
        print("---")
        print(another_composite.draw())
