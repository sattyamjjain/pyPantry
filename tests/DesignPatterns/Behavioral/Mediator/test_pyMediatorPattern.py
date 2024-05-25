import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Mediator.PyMediatorPattern import (
    PyMediatorPattern,
)


class PyMediatorPatternTestCase(unittest.TestCase):

    def test_chat_room_mediator(self):
        chat_room = PyMediatorPattern.ChatRoom()
        user1 = PyMediatorPattern.User("Alice", chat_room)
        user2 = PyMediatorPattern.User("Bob", chat_room)

        with patch("sys.stdout", new=StringIO()) as fake_out:
            user1.send_message("Hi Bob!")
            user2.send_message("Hello Alice!")
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("[Alice]: Hi Bob!", output)
            self.assertIn("[Bob]: Hello Alice!", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyMediatorPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("[Alice]: Hi Bob!", output)
            self.assertIn("[Bob]: Hello Alice!", output)


if __name__ == "__main__":
    unittest.main()
