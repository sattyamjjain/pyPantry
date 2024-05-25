from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyProxyPattern(PyDesignPatterns):
    # Subject Interface
    class Image(ABC):
        @abstractmethod
        def display(self) -> None:
            pass

    # RealSubject
    class RealImage(Image):
        def __init__(self, filename: str):
            self.filename = filename
            self.load_from_disk()

        def load_from_disk(self) -> None:
            print(f"Loading {self.filename} from disk...")

        def display(self) -> None:
            print(f"Displaying {self.filename}")

    # Proxy
    class ProxyImage(Image):
        def __init__(self, filename: str):
            self.filename = filename
            self.real_image = None

        def display(self) -> None:
            if self.real_image is None:
                self.real_image = PyProxyPattern.RealImage(self.filename)
            self.real_image.display()

    def example(self):
        image1 = PyProxyPattern.ProxyImage("image1.jpg")
        image2 = PyProxyPattern.ProxyImage("image2.jpg")

        # Image will be loaded from disk
        image1.display()

        # Image will not be loaded from disk again
        image1.display()

        # Image will be loaded from disk
        image2.display()
