import inspect
from abc import ABC, abstractmethod
from typing import Optional


class PyDesignPatterns(ABC):
    @abstractmethod
    def example(self):
        pass

    def get_time_complexity(self):
        pass

    def get_space_complexity(self):
        pass

    def get_sourcing_code(self, pattern_name: str) -> Optional[str]:
        subclasses = [self.__class__] + self.__class__.__subclasses__()
        for subclass in subclasses:
            if pattern_name == subclass.__name__:
                return inspect.getsource(subclass)
        return None
