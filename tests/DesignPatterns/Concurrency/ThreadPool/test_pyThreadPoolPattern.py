import time
import unittest
from unittest.mock import patch, call

from pyPantry.DesignPatterns.Concurrency.ThreadPool.PyThreadPoolPattern import (
    PyThreadPoolPattern,
)


class PyThreadPoolPatternTestCase(unittest.TestCase):

    def test_thread_pool(self):
        pool = PyThreadPoolPattern.ThreadPool(2)

        with patch("builtins.print") as mocked_print, patch(
            "time.sleep", return_value=None
        ):
            pool.add_task(mocked_print, "Task 1 running")
            pool.add_task(mocked_print, "Task 2 running")
            pool.add_task(mocked_print, "Task 3 running")

            time.sleep(1)  # Allow some time for tasks to be picked up

            pool.shutdown()

            self.assertIn(call("Task 1 running"), mocked_print.mock_calls)
            self.assertIn(call("Task 2 running"), mocked_print.mock_calls)
            self.assertIn(call("Task 3 running"), mocked_print.mock_calls)

    def test_example(self):
        with patch("builtins.print") as mocked_print, patch(
            "time.sleep", return_value=None
        ):
            pattern = PyThreadPoolPattern()
            pattern.example()
            output = mocked_print.mock_calls
            self.assertIn(call("Task running for 2 seconds"), output)
            self.assertIn(call("Task running for 3 seconds"), output)
            self.assertIn(call("Task running for 1 seconds"), output)
            self.assertIn(call("Task completed in 2 seconds"), output)
            self.assertIn(call("Task completed in 3 seconds"), output)
            self.assertIn(call("Task completed in 1 seconds"), output)


if __name__ == "__main__":
    unittest.main()
