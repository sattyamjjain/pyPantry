import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Creational.AbstractFactory.PyAbstractFactoryPattern import (
    PyAbstractFactoryPattern,
)


class PyAbstractFactoryPatternTestCase(unittest.TestCase):

    def test_windows_ui(self):
        factory = PyAbstractFactoryPattern.WindowsUIFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        self.assertIsInstance(button, PyAbstractFactoryPattern.WindowsButton)
        self.assertIsInstance(checkbox, PyAbstractFactoryPattern.WindowsCheckbox)
        self.assertEqual(button.click(), "Windows Button clicked")
        self.assertEqual(checkbox.toggle(), "Windows Checkbox toggled")

    def test_macos_ui(self):
        factory = PyAbstractFactoryPattern.MacOSUIFactory()
        button = factory.create_button()
        checkbox = factory.create_checkbox()
        self.assertIsInstance(button, PyAbstractFactoryPattern.MacOSButton)
        self.assertIsInstance(checkbox, PyAbstractFactoryPattern.MacOSCheckbox)
        self.assertEqual(button.click(), "MacOS Button clicked")
        self.assertEqual(checkbox.toggle(), "MacOS Checkbox toggled")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyAbstractFactoryPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertEqual(output[0], "Windows Button clicked")
            self.assertEqual(output[1], "Windows Checkbox toggled")
            self.assertEqual(output[2], "MacOS Button clicked")
            self.assertEqual(output[3], "MacOS Checkbox toggled")


if __name__ == "__main__":
    unittest.main()
