from abc import ABC, abstractmethod

from pyPantry.DesignPatterns import PyDesignPatterns


class PyAbstractFactoryPattern(PyDesignPatterns):
    # Abstract Products
    class Button(ABC):
        @abstractmethod
        def click(self) -> str:
            pass

    class Checkbox(ABC):
        @abstractmethod
        def toggle(self) -> str:
            pass

    # Concrete Products for Windows
    class WindowsButton(Button):
        def click(self) -> str:
            return "Windows Button clicked"

    class WindowsCheckbox(Checkbox):
        def toggle(self) -> str:
            return "Windows Checkbox toggled"

    # Concrete Products for MacOS
    class MacOSButton(Button):
        def click(self) -> str:
            return "MacOS Button clicked"

    class MacOSCheckbox(Checkbox):
        def toggle(self) -> str:
            return "MacOS Checkbox toggled"

    # Abstract Factory
    class UIFactory(ABC):
        @abstractmethod
        def create_button(self) -> "PyAbstractFactoryPattern.Button":
            pass

        @abstractmethod
        def create_checkbox(self) -> "PyAbstractFactoryPattern.Checkbox":
            pass

    # Concrete Factories
    class WindowsUIFactory(UIFactory):
        def create_button(self) -> "PyAbstractFactoryPattern.Button":
            return PyAbstractFactoryPattern.WindowsButton()

        def create_checkbox(self) -> "PyAbstractFactoryPattern.Checkbox":
            return PyAbstractFactoryPattern.WindowsCheckbox()

    class MacOSUIFactory(UIFactory):
        def create_button(self) -> "PyAbstractFactoryPattern.Button":
            return PyAbstractFactoryPattern.MacOSButton()

        def create_checkbox(self) -> "PyAbstractFactoryPattern.Checkbox":
            return PyAbstractFactoryPattern.MacOSCheckbox()

    def example(self):
        def create_ui(factory: PyAbstractFactoryPattern.UIFactory):
            button = factory.create_button()
            checkbox = factory.create_checkbox()
            print(button.click())
            print(checkbox.toggle())

        # Create Windows UI
        windows_factory = PyAbstractFactoryPattern.WindowsUIFactory()
        create_ui(windows_factory)

        # Create MacOS UI
        macos_factory = PyAbstractFactoryPattern.MacOSUIFactory()
        create_ui(macos_factory)
