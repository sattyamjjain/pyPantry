import unittest
from unittest.mock import patch, call, MagicMock

from pyPantry.DesignPatterns.Architectural.ModelViewController.PyModelViewControllerPattern import (
    PyModelViewControllerPattern,
)


class PyModelViewControllerPatternTestCase(unittest.TestCase):

    def test_task_model(self):
        model = PyModelViewControllerPattern.TaskModel()
        observer = MagicMock()
        model.add_observer(observer)

        model.add_task("Task 1")
        self.assertIn("Task 1", model.get_tasks())
        observer.update.assert_called_once()

        model.remove_task("Task 1")
        self.assertNotIn("Task 1", model.get_tasks())
        self.assertEqual(observer.update.call_count, 2)

    def test_task_view(self):
        view = PyModelViewControllerPattern.TaskView()
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

    def test_task_controller(self):
        model = PyModelViewControllerPattern.TaskModel()
        view = PyModelViewControllerPattern.TaskView()
        controller = PyModelViewControllerPattern.TaskController(model, view)

        with patch.object(view, "display_tasks") as mocked_display:
            controller.add_task("Task 1")
            mocked_display.assert_called_once_with(["Task 1"])

            controller.add_task("Task 2")
            mocked_display.assert_called_with(["Task 1", "Task 2"])

            controller.remove_task("Task 1")
            mocked_display.assert_called_with(["Task 2"])

    def test_example(self):
        with patch("builtins.print") as mocked_print:
            pattern = PyModelViewControllerPattern()
            pattern.example()
            output = mocked_print.mock_calls
            self.assertIn(call("Task List:"), output)
            self.assertIn(call("- Task 1"), output)
            self.assertIn(call("- Task 2"), output)
            self.assertIn(call("Task List:"), output)
            self.assertIn(call("- Task 2"), output)


if __name__ == "__main__":
    unittest.main()
