import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Iterator.PyIteratorPattern import (
    PyIteratorPattern,
)


class PyIteratorPatternTestCase(unittest.TestCase):

    def test_book_iterator(self):
        collection = PyIteratorPattern.BookCollection()
        collection.add_book("Book 1")
        collection.add_book("Book 2")
        collection.add_book("Book 3")

        iterator = collection.get_iterator()
        books = []
        while iterator.has_next():
            books.append(iterator.next())

        self.assertEqual(books, ["Book 1", "Book 2", "Book 3"])

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyIteratorPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn("Book 1", output)
            self.assertIn("Book 2", output)
            self.assertIn("Book 3", output)


if __name__ == "__main__":
    unittest.main()
