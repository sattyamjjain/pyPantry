from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyMediatorPattern(PyDesignPatterns):
    # Mediator Interface
    class ChatRoomMediator(ABC):
        @abstractmethod
        def show_message(self, user: "PyMediatorPattern.User", message: str) -> None:
            pass

    # Concrete Mediator
    class ChatRoom(ChatRoomMediator):
        def show_message(self, user: "PyMediatorPattern.User", message: str) -> None:
            print(f"[{user.get_name()}]: {message}")

    # Colleague
    class User:
        def __init__(self, name: str, mediator: "PyMediatorPattern.ChatRoomMediator"):
            self._name = name
            self._mediator = mediator

        def get_name(self) -> str:
            return self._name

        def send_message(self, message: str) -> None:
            self._mediator.show_message(self, message)

    def example(self):
        chat_room = PyMediatorPattern.ChatRoom()

        user1 = PyMediatorPattern.User("Alice", chat_room)
        user2 = PyMediatorPattern.User("Bob", chat_room)

        user1.send_message("Hi Bob!")
        user2.send_message("Hello Alice!")
