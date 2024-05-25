import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.NullObject.PyNullObjectPattern import (
    PyNullObjectPattern,
)


class PyNullObjectPatternTestCase(unittest.TestCase):

    def test_console_logger(self):
        logger = PyNullObjectPattern.ConsoleLogger()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            logger.log("Test message")
            output = fake_out.getvalue().strip()
            self.assertIn("Logging to console: Test message", output)

    def test_null_logger(self):
        logger = PyNullObjectPattern.NullLogger()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            logger.log("Test message")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_application_with_logging(self):
        logger = PyNullObjectPattern.ConsoleLogger()
        app = PyNullObjectPattern.Application(logger)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.do_something()
            output = fake_out.getvalue().strip()
            self.assertIn("Logging to console: Doing something", output)

    def test_application_without_logging(self):
        logger = PyNullObjectPattern.NullLogger()
        app = PyNullObjectPattern.Application(logger)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            app.do_something()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyNullObjectPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Application with logging:", output)
            self.assertIn("Logging to console: Doing something", output)
            self.assertIn("Application without logging:", output)


if __name__ == "__main__":
    unittest.main()
