import threading
from queue import Queue
from abc import ABC, abstractmethod
import time

from pyPantry.DesignPatterns import PyDesignPatterns


class PyActiveObjectPattern(PyDesignPatterns):
    # Command Interface
    class Command(ABC):
        @abstractmethod
        def execute(self) -> None:
            pass

    # Concrete Command
    class PrintCommand(Command):
        def __init__(self, message: str):
            self.message = message

        def execute(self) -> None:
            print(self.message)

    # Scheduler
    class Scheduler(threading.Thread):
        def __init__(self):
            super().__init__()
            self._queue = Queue()
            self._stop_event = threading.Event()

        def enqueue(self, command: "PyActiveObjectPattern.Command") -> None:
            self._queue.put(command)

        def run(self) -> None:
            while not self._stop_event.is_set():
                if not self._queue.empty():
                    command = self._queue.get()
                    command.execute()
                time.sleep(0.1)

        def stop(self) -> None:
            self._stop_event.set()

    def example(self):
        scheduler = PyActiveObjectPattern.Scheduler()
        scheduler.start()

        scheduler.enqueue(PyActiveObjectPattern.PrintCommand("Hello"))
        scheduler.enqueue(PyActiveObjectPattern.PrintCommand("World"))
        scheduler.enqueue(PyActiveObjectPattern.PrintCommand("Active Object Pattern"))

        time.sleep(1)
        scheduler.stop()
