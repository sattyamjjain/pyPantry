import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Observer.PyObserverPattern import (
    PyObserverPattern,
)


class PyObserverPatternTestCase(unittest.TestCase):

    def test_observer_notification(self):
        channel = PyObserverPattern.ConcreteNewsChannel()

        subscriber1 = PyObserverPattern.Subscriber("Alice")
        subscriber2 = PyObserverPattern.Subscriber("Bob")

        channel.register_observer(subscriber1)
        channel.register_observer(subscriber2)

        with patch("sys.stdout", new=StringIO()) as fake_out:
            channel.add_news("Breaking News: Observer Pattern in Action!")
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn(
                "Alice received news: Breaking News: Observer Pattern in Action!",
                output,
            )
            self.assertIn(
                "Bob received news: Breaking News: Observer Pattern in Action!", output
            )

        with patch("sys.stdout", new=StringIO()) as fake_out:
            channel.add_news("Update: More news to follow.")
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Alice received news: Update: More news to follow.", output)
            self.assertIn("Bob received news: Update: More news to follow.", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyObserverPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn(
                "Alice received news: Breaking News: Observer Pattern in Action!",
                output,
            )
            self.assertIn(
                "Bob received news: Breaking News: Observer Pattern in Action!", output
            )
            self.assertIn("Alice received news: Update: More news to follow.", output)
            self.assertIn("Bob received news: Update: More news to follow.", output)


if __name__ == "__main__":
    unittest.main()
