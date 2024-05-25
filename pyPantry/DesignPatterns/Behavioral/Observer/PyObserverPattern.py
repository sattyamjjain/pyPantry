from abc import ABC, abstractmethod
from typing import List

from pyPantry.DesignPatterns import PyDesignPatterns


class PyObserverPattern(PyDesignPatterns):
    # Subject Interface
    class NewsChannel(ABC):
        @abstractmethod
        def register_observer(self, observer: "PyObserverPattern.Observer") -> None:
            pass

        @abstractmethod
        def remove_observer(self, observer: "PyObserverPattern.Observer") -> None:
            pass

        @abstractmethod
        def notify_observers(self) -> None:
            pass

    # Concrete Subject
    class ConcreteNewsChannel(NewsChannel):
        def __init__(self):
            self._observers: List["PyObserverPattern.Observer"] = []
            self._latest_news: str = ""

        def register_observer(self, observer: "PyObserverPattern.Observer") -> None:
            self._observers.append(observer)

        def remove_observer(self, observer: "PyObserverPattern.Observer") -> None:
            self._observers.remove(observer)

        def notify_observers(self) -> None:
            for observer in self._observers:
                observer.update(self._latest_news)

        def add_news(self, news: str) -> None:
            self._latest_news = news
            self.notify_observers()

    # Observer Interface
    class Observer(ABC):
        @abstractmethod
        def update(self, news: str) -> None:
            pass

    # Concrete Observer
    class Subscriber(Observer):
        def __init__(self, name: str):
            self._name = name

        def update(self, news: str) -> None:
            print(f"{self._name} received news: {news}")

    def example(self):
        channel = PyObserverPattern.ConcreteNewsChannel()

        subscriber1 = PyObserverPattern.Subscriber("Alice")
        subscriber2 = PyObserverPattern.Subscriber("Bob")

        channel.register_observer(subscriber1)
        channel.register_observer(subscriber2)

        channel.add_news("Breaking News: Observer Pattern in Action!")
        channel.add_news("Update: More news to follow.")
