from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyDecoratorPattern(PyDesignPatterns):
    # Component
    class Text(ABC):
        @abstractmethod
        def render(self) -> str:
            pass

    # Concrete Component
    class PlainText(Text):
        def __init__(self, text: str):
            self.text = text

        def render(self) -> str:
            return self.text

    # Decorator
    class TextDecorator(Text):
        def __init__(self, decorated_text: "PyDecoratorPattern.Text"):
            self.decorated_text = decorated_text

        @abstractmethod
        def render(self) -> str:
            pass

    # Concrete Decorators
    class BoldDecorator(TextDecorator):
        def render(self) -> str:
            return f"<b>{self.decorated_text.render()}</b>"

    class ItalicDecorator(TextDecorator):
        def render(self) -> str:
            return f"<i>{self.decorated_text.render()}</i>"

    class UnderlineDecorator(TextDecorator):
        def render(self) -> str:
            return f"<u>{self.decorated_text.render()}</u>"

    def example(self):
        simple_text = PyDecoratorPattern.PlainText("Hello, World!")
        bold_text = PyDecoratorPattern.BoldDecorator(simple_text)
        italic_bold_text = PyDecoratorPattern.ItalicDecorator(bold_text)
        underlined_italic_bold_text = PyDecoratorPattern.UnderlineDecorator(
            italic_bold_text
        )

        print("Plain Text:", simple_text.render())
        print("Bold Text:", bold_text.render())
        print("Italic Bold Text:", italic_bold_text.render())
        print("Underlined Italic Bold Text:", underlined_italic_bold_text.render())
