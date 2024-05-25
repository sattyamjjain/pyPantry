from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyNullObjectPattern(PyDesignPatterns):
    # Abstract Class
    class Logger(ABC):
        @abstractmethod
        def log(self, message: str) -> None:
            pass

    # Real Object
    class ConsoleLogger(Logger):
        def log(self, message: str) -> None:
            print(f"Logging to console: {message}")

    # Null Object
    class NullLogger(Logger):
        def log(self, message: str) -> None:
            pass

    # Client Code
    class Application:
        def __init__(self, logger: "PyNullObjectPattern.Logger"):
            self._logger = logger

        def do_something(self) -> None:
            self._logger.log("Doing something")

    def example(self):
        console_logger = PyNullObjectPattern.ConsoleLogger()
        null_logger = PyNullObjectPattern.NullLogger()

        app_with_logging = PyNullObjectPattern.Application(console_logger)
        app_with_no_logging = PyNullObjectPattern.Application(null_logger)

        print("Application with logging:")
        app_with_logging.do_something()

        print("\nApplication without logging:")
        app_with_no_logging.do_something()
