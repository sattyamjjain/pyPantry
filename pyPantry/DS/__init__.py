import inspect
from typing import Optional


class PyDS:
    def __init__(self):
        pass

    def get_time_complexity(self):
        pass

    def get_space_complexity(self):
        pass

    def get_sourcing_code(self, ds: str) -> Optional[str]:
        subclasses = [self.__class__] + self.__class__.__subclasses__()
        for subclass in subclasses:
            if ds == subclass.__name__:
                return inspect.getsource(subclass)
        return None
