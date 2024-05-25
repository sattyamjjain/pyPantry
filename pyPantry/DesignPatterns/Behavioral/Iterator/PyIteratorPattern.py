from abc import ABC, abstractmethod
from typing import List, Iterator as TypingIterator

from pyPantry.DesignPatterns import PyDesignPatterns


class PyIteratorPattern(PyDesignPatterns):
    # Iterator Interface
    class Iterator(ABC):
        @abstractmethod
        def next(self) -> object:
            pass

        @abstractmethod
        def has_next(self) -> bool:
            pass

    # Concrete Iterator
    class BookIterator(Iterator):
        def __init__(self, books: List[str]):
            self._books = books
            self._position = 0

        def next(self) -> str:
            book = self._books[self._position]
            self._position += 1
            return book

        def has_next(self) -> bool:
            return self._position < len(self._books)

    # Aggregate Interface
    class BookCollection:
        def __init__(self):
            self._books: List[str] = []

        def add_book(self, book: str) -> None:
            self._books.append(book)

        def get_iterator(self) -> "PyIteratorPattern.BookIterator":
            return PyIteratorPattern.BookIterator(self._books)

    def example(self):
        collection = PyIteratorPattern.BookCollection()
        collection.add_book("Book 1")
        collection.add_book("Book 2")
        collection.add_book("Book 3")

        iterator = collection.get_iterator()
        while iterator.has_next():
            book = iterator.next()
            print(book)
