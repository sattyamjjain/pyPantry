import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Template.PyTemplatePattern import (
    PyTemplatePattern,
)


class PyTemplatePatternTestCase(unittest.TestCase):

    def test_csv_data_processor(self):
        processor = PyTemplatePattern.CSVDataProcessor()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            processor.process()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Reading data from CSV file", output)
            self.assertIn("Processing data", output)
            self.assertIn("Saving data to CSV file", output)

    def test_json_data_processor(self):
        processor = PyTemplatePattern.JSONDataProcessor()
        with patch("sys.stdout", new=StringIO()) as fake_out:
            processor.process()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Reading data from JSON file", output)
            self.assertIn("Processing data", output)
            self.assertIn("Saving data to JSON file", output)

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyTemplatePattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("CSV Data Processing:", output)
            self.assertIn("Reading data from CSV file", output)
            self.assertIn("Processing data", output)
            self.assertIn("Saving data to CSV file", output)
            self.assertIn("JSON Data Processing:", output)
            self.assertIn("Reading data from JSON file", output)
            self.assertIn("Processing data", output)
            self.assertIn("Saving data to JSON file", output)


if __name__ == "__main__":
    unittest.main()
