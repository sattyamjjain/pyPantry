from abc import ABC, abstractmethod
from typing import Dict, List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyInterpreterPattern(PyDesignPatterns):
    # Abstract Expression
    class Expression(ABC):
        @abstractmethod
        def interpret(self, context: Dict[str, int]) -> int:
            pass

    # Terminal Expression
    class Number(Expression):
        def __init__(self, number: int):
            self.number = number

        def interpret(self, context: Dict[str, int]) -> int:
            return self.number

    # Non-terminal Expression
    class Plus(Expression):
        def __init__(
            self,
            left: "PyInterpreterPattern.Expression",
            right: "PyInterpreterPattern.Expression",
        ):
            self.left = left
            self.right = right

        def interpret(self, context: Dict[str, int]) -> int:
            return self.left.interpret(context) + self.right.interpret(context)

    class Minus(Expression):
        def __init__(
            self,
            left: "PyInterpreterPattern.Expression",
            right: "PyInterpreterPattern.Expression",
        ):
            self.left = left
            self.right = right

        def interpret(self, context: Dict[str, int]) -> int:
            return self.left.interpret(context) - self.right.interpret(context)

    def example(self):
        context = {}

        # Building the expression (5 + 10) - (2 + 3)
        expression = PyInterpreterPattern.Minus(
            PyInterpreterPattern.Plus(
                PyInterpreterPattern.Number(5), PyInterpreterPattern.Number(10)
            ),
            PyInterpreterPattern.Plus(
                PyInterpreterPattern.Number(2), PyInterpreterPattern.Number(3)
            ),
        )

        result = expression.interpret(context)
        print(f"The result of the expression is: {result}")
