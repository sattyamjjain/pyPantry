import threading

from pyPantry.DesignPatterns import PyDesignPatterns


class PySingletonPattern(PyDesignPatterns):
    class SingletonMeta(type):
        _instances = {}
        _lock: threading.Lock = threading.Lock()

        def __call__(cls, *args, **kwargs):
            with cls._lock:
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
            return cls._instances[cls]

    class Logger(metaclass=SingletonMeta):
        def __init__(self):
            self.log_file = "app.log"

        def log(self, message: str) -> None:
            with open(self.log_file, "a") as file:
                file.write(message + "\n")

        def clear_log(self) -> None:
            open(self.log_file, "w").close()

    def example(self):
        logger1 = self.Logger()
        logger2 = self.Logger()

        logger1.log("This is the first log message.")
        logger2.log("This is the second log message.")

        print(f"Logger1 is Logger2: {logger1 is logger2}")

        with open("app.log", "r") as file:
            print(file.read())
