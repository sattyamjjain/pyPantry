import queue
import time
import unittest
from unittest.mock import patch, call

from pyPantry.DesignPatterns.Concurrency.HalfSyncOrHalfAsync.PyHalfSyncOrHalfAsyncPattern import (
    PyHalfSyncOrHalfAsyncPattern,
)


class PyHalfSyncOrHalfAsyncPatternTestCase(unittest.TestCase):

    def test_sync_layer_process_request(self):
        task_queue = queue.Queue()
        sync_layer = PyHalfSyncOrHalfAsyncPattern.SyncLayer(task_queue)

        with patch("builtins.print") as mocked_print:
            sync_layer.process_request("Test Request")
            self.assertIn(
                call("Processing request: Test Request"), mocked_print.mock_calls
            )
            task = task_queue.get(timeout=1)
            task()
            self.assertIn(
                call("Handled request: Test Request"), mocked_print.mock_calls
            )

    def test_async_layer_run(self):
        task_queue = queue.Queue()
        async_layer = PyHalfSyncOrHalfAsyncPattern.AsyncLayer(task_queue)
        sync_layer = PyHalfSyncOrHalfAsyncPattern.SyncLayer(task_queue)

        async_layer.start()

        with patch("builtins.print") as mocked_print:
            sync_layer.process_request("Test Request 1")
            sync_layer.process_request("Test Request 2")
            time.sleep(3)  # Allow some time for processing
            async_layer.stop()
            async_layer.join()

            self.assertIn(
                call("Processing request: Test Request 1"), mocked_print.mock_calls
            )
            self.assertIn(
                call("Processing request: Test Request 2"), mocked_print.mock_calls
            )
            self.assertIn(
                call("Handled request: Test Request 1"), mocked_print.mock_calls
            )
            self.assertIn(
                call("Handled request: Test Request 2"), mocked_print.mock_calls
            )

    def test_example(self):
        with patch("builtins.print") as mocked_print:
            pattern = PyHalfSyncOrHalfAsyncPattern()
            pattern.example()
            output = mocked_print.mock_calls
            self.assertIn(call("Processing request: Request 1"), output)
            self.assertIn(call("Processing request: Request 2"), output)
            self.assertIn(call("Handled request: Request 1"), output)
            self.assertIn(call("Handled request: Request 2"), output)


if __name__ == "__main__":
    unittest.main()
