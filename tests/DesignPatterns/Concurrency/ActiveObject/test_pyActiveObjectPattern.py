import time
import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Concurrency.ActiveObject.PyActiveObjectPattern import (
    PyActiveObjectPattern,
)


class PyActiveObjectPatternTestCase(unittest.TestCase):

    def test_print_command(self):
        command = PyActiveObjectPattern.PrintCommand("Test Message")
        with patch("sys.stdout", new=StringIO()) as fake_out:
            command.execute()
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "Test Message")

    def test_scheduler(self):
        scheduler = PyActiveObjectPattern.Scheduler()
        scheduler.start()

        with patch("sys.stdout", new=StringIO()) as fake_out:
            scheduler.enqueue(PyActiveObjectPattern.PrintCommand("Test 1"))
            scheduler.enqueue(PyActiveObjectPattern.PrintCommand("Test 2"))
            time.sleep(1)
            scheduler.stop()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Test 1", output)
            self.assertIn("Test 2", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyActiveObjectPattern()
            pattern.example()
            time.sleep(1)
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Hello", output)
            self.assertIn("World", output)
            self.assertIn("Active Object Pattern", output)


if __name__ == "__main__":
    unittest.main()
