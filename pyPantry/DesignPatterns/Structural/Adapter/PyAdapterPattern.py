from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyAdapterPattern(PyDesignPatterns):
    # Target Interface
    class Shape(ABC):
        @abstractmethod
        def draw(self) -> str:
            pass

    # Adaptee
    class LegacyRectangle:
        @staticmethod
        def draw_rectangle() -> str:
            return "Drawing a rectangle using LegacyRectangle"

    # Adapter
    class RectangleAdapter(Shape):
        def __init__(self, adaptee: "PyAdapterPattern.LegacyRectangle"):
            self.adaptee = adaptee

        def draw(self) -> str:
            return self.adaptee.draw_rectangle()

    def example(self):
        legacy_rectangle = PyAdapterPattern.LegacyRectangle()
        adapter = PyAdapterPattern.RectangleAdapter(legacy_rectangle)
        print(adapter.draw())
