import unittest
from unittest.mock import patch, call

from pyPantry.DesignPatterns.Architectural.ModelViewViewModel.PyModelViewViewModelPattern import (
    PyModelViewViewModelPattern,
)


class PyModelViewViewModelPatternTestCase(unittest.TestCase):

    def test_task_model(self):
        model = PyModelViewViewModelPattern.TaskModel()

        model.add_task("Task 1")
        self.assertIn("Task 1", model.get_tasks())

        model.remove_task("Task 1")
        self.assertNotIn("Task 1", model.get_tasks())

    def test_task_view(self):
        view = PyModelViewViewModelPattern.TaskView()
        tasks = ["Task 1", "Task 2"]

        with patch("builtins.print") as mocked_print:
            view.display_tasks(tasks)
            mocked_print.assert_has_calls(
                [
                    call("Task List:"),
                    call("- Task 1"),
                    call("- Task 2"),
                ]
            )

    def test_task_viewmodel(self):
        model = PyModelViewViewModelPattern.TaskModel()
        viewmodel = PyModelViewViewModelPattern.TaskViewModel(model)

        viewmodel.add_task("Task 1")
        self.assertIn("Task 1", viewmodel.get_tasks())

        viewmodel.add_task("Task 2")
        self.assertIn("Task 2", viewmodel.get_tasks())

        viewmodel.remove_task("Task 1")
        self.assertNotIn("Task 1", viewmodel.get_tasks())

    def test_example(self):
        with patch("builtins.print") as mocked_print:
            pattern = PyModelViewViewModelPattern()
            pattern.example()
            output = mocked_print.mock_calls
            self.assertIn(call("Task List:"), output)
            self.assertIn(call("- Task 2"), output)


if __name__ == "__main__":
    unittest.main()
