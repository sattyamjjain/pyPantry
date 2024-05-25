from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyChainOfResponsibilityPattern(PyDesignPatterns):
    # Handler Interface
    class Handler(ABC):
        def __init__(self, successor: "PyChainOfResponsibilityPattern.Handler" = None):
            self._successor = successor

        @abstractmethod
        def handle_request(self, request: str) -> None:
            pass

    # Concrete Handlers
    class LevelOneSupport(Handler):
        def handle_request(self, request: str) -> None:
            if request == "Level 1":
                print(f"Level 1 support handling the request: {request}")
            elif self._successor:
                self._successor.handle_request(request)

    class LevelTwoSupport(Handler):
        def handle_request(self, request: str) -> None:
            if request == "Level 2":
                print(f"Level 2 support handling the request: {request}")
            elif self._successor:
                self._successor.handle_request(request)

    class LevelThreeSupport(Handler):
        def handle_request(self, request: str) -> None:
            if request == "Level 3":
                print(f"Level 3 support handling the request: {request}")
            elif self._successor:
                self._successor.handle_request(request)

    def example(self):
        # Create the chain of responsibility
        level3 = PyChainOfResponsibilityPattern.LevelThreeSupport()
        level2 = PyChainOfResponsibilityPattern.LevelTwoSupport(level3)
        level1 = PyChainOfResponsibilityPattern.LevelOneSupport(level2)

        # Send requests to the chain
        requests = ["Level 1", "Level 2", "Level 3", "Unknown"]
        for request in requests:
            print(f"Request: {request}")
            level1.handle_request(request)
            print("---")
