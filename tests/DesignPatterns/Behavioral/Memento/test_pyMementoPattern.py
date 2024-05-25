import unittest
from io import StringIO
from unittest.mock import patch

from pyPantry.DesignPatterns.Behavioral.Memento.PyMementoPattern import PyMementoPattern


class PyMementoPatternTestCase(unittest.TestCase):

    def test_text_editor_save_restore(self):
        editor = PyMementoPattern.TextEditor()
        history = PyMementoPattern.History()

        editor.type("Hello")
        history.save(editor.save())

        editor.type(", World!")
        history.save(editor.save())

        editor.type(" This is an example of Memento pattern.")
        self.assertEqual(
            editor.get_text(), "Hello, World! This is an example of Memento pattern."
        )

        editor.restore(history.restore())
        self.assertEqual(editor.get_text(), "Hello, World!")

        editor.restore(history.restore())
        self.assertEqual(editor.get_text(), "Hello")

    def test_example(self):
        with patch("sys.stdout", new=StringIO()) as fake_out:
            pattern = PyMementoPattern()
            pattern.example()
            output = fake_out.getvalue().strip().split("\n")
            self.assertIn(
                "Current text: Hello, World! This is an example of Memento pattern.",
                output,
            )
            self.assertIn("Restored text: Hello, World!", output)
            self.assertIn("Restored text: Hello", output)


if __name__ == "__main__":
    unittest.main()
