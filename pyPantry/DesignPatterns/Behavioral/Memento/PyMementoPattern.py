from pyPantry.DesignPatterns import PyDesignPatterns


class PyMementoPattern(PyDesignPatterns):
    # Memento
    class Memento:
        def __init__(self, state: str):
            self._state = state

        def get_state(self) -> str:
            return self._state

    # Originator
    class TextEditor:
        def __init__(self):
            self._state = ""

        def type(self, text: str) -> None:
            self._state += text

        def save(self) -> "PyMementoPattern.Memento":
            return PyMementoPattern.Memento(self._state)

        def restore(self, memento: "PyMementoPattern.Memento") -> None:
            self._state = memento.get_state()

        def get_text(self) -> str:
            return self._state

    # Caretaker
    class History:
        def __init__(self):
            self._mementos = []

        def save(self, memento: "PyMementoPattern.Memento") -> None:
            self._mementos.append(memento)

        def restore(self) -> "PyMementoPattern.Memento":
            return self._mementos.pop() if self._mementos else None

    def example(self):
        editor = PyMementoPattern.TextEditor()
        history = PyMementoPattern.History()

        editor.type("Hello")
        history.save(editor.save())

        editor.type(", World!")
        history.save(editor.save())

        editor.type(" This is an example of Memento pattern.")
        print("Current text:", editor.get_text())

        editor.restore(history.restore())
        print("Restored text:", editor.get_text())

        editor.restore(history.restore())
        print("Restored text:", editor.get_text())
