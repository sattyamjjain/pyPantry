from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyVisitorPattern(PyDesignPatterns):
    # Visitor Interface
    class Visitor(ABC):
        @abstractmethod
        def visit_text(self, text: "PyVisitorPattern.TextElement") -> None:
            pass

        @abstractmethod
        def visit_image(self, image: "PyVisitorPattern.ImageElement") -> None:
            pass

        @abstractmethod
        def visit_table(self, table: "PyVisitorPattern.TableElement") -> None:
            pass

    # Element Interface
    class Element(ABC):
        @abstractmethod
        def accept(self, visitor: "PyVisitorPattern.Visitor") -> None:
            pass

    # Concrete Elements
    class TextElement(Element):
        def __init__(self, text: str):
            self.text = text

        def accept(self, visitor: "PyVisitorPattern.Visitor") -> None:
            visitor.visit_text(self)

    class ImageElement(Element):
        def __init__(self, image_url: str):
            self.image_url = image_url

        def accept(self, visitor: "PyVisitorPattern.Visitor") -> None:
            visitor.visit_image(self)

    class TableElement(Element):
        def __init__(self, rows: int, columns: int):
            self.rows = rows
            self.columns = columns

        def accept(self, visitor: "PyVisitorPattern.Visitor") -> None:
            visitor.visit_table(self)

    # Concrete Visitor
    class RenderVisitor(Visitor):
        def visit_text(self, text: "PyVisitorPattern.TextElement") -> None:
            print(f"Rendering text: {text.text}")

        def visit_image(self, image: "PyVisitorPattern.ImageElement") -> None:
            print(f"Rendering image from URL: {image.image_url}")

        def visit_table(self, table: "PyVisitorPattern.TableElement") -> None:
            print(f"Rendering table with {table.rows} rows and {table.columns} columns")

    def example(self):
        elements: List["PyVisitorPattern.Element"] = [
            PyVisitorPattern.TextElement("Hello, World!"),
            PyVisitorPattern.ImageElement("http://example.com/image.jpg"),
            PyVisitorPattern.TableElement(3, 5),
        ]

        visitor = PyVisitorPattern.RenderVisitor()

        for element in elements:
            element.accept(visitor)
