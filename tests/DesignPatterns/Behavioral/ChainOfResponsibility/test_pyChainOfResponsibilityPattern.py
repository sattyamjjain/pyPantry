import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.ChainOfResponsibility.PyChainOfResponsibilityPattern import (
    PyChainOfResponsibilityPattern,
)


class PyChainOfResponsibilityPatternTestCase(unittest.TestCase):

    def test_level_one_support(self):
        level3 = PyChainOfResponsibilityPattern.LevelThreeSupport()
        level2 = PyChainOfResponsibilityPattern.LevelTwoSupport(level3)
        level1 = PyChainOfResponsibilityPattern.LevelOneSupport(level2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            level1.handle_request("Level 1")
            output = fake_out.getvalue().strip()
            self.assertIn("Level 1 support handling the request: Level 1", output)

    def test_level_two_support(self):
        level3 = PyChainOfResponsibilityPattern.LevelThreeSupport()
        level2 = PyChainOfResponsibilityPattern.LevelTwoSupport(level3)
        level1 = PyChainOfResponsibilityPattern.LevelOneSupport(level2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            level1.handle_request("Level 2")
            output = fake_out.getvalue().strip()
            self.assertIn("Level 2 support handling the request: Level 2", output)

    def test_level_three_support(self):
        level3 = PyChainOfResponsibilityPattern.LevelThreeSupport()
        level2 = PyChainOfResponsibilityPattern.LevelTwoSupport(level3)
        level1 = PyChainOfResponsibilityPattern.LevelOneSupport(level2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            level1.handle_request("Level 3")
            output = fake_out.getvalue().strip()
            self.assertIn("Level 3 support handling the request: Level 3", output)

    def test_unknown_request(self):
        level3 = PyChainOfResponsibilityPattern.LevelThreeSupport()
        level2 = PyChainOfResponsibilityPattern.LevelTwoSupport(level3)
        level1 = PyChainOfResponsibilityPattern.LevelOneSupport(level2)
        with patch("sys.stdout", new=StringIO()) as fake_out:
            level1.handle_request("Unknown")
            output = fake_out.getvalue().strip()
            self.assertEqual(output, "")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyChainOfResponsibilityPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Request: Level 1", output)
            self.assertIn("Level 1 support handling the request: Level 1", output)
            self.assertIn("Request: Level 2", output)
            self.assertIn("Level 2 support handling the request: Level 2", output)
            self.assertIn("Request: Level 3", output)
            self.assertIn("Level 3 support handling the request: Level 3", output)
            self.assertIn("Request: Unknown", output)
            self.assertIn("---", output)


if __name__ == "__main__":
    unittest.main()
