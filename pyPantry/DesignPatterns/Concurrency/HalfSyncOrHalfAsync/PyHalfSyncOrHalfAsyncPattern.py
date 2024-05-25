import threading
import queue
import time

from pyPantry.DesignPatterns import PyDesignPatterns


class PyHalfSyncOrHalfAsyncPattern(PyDesignPatterns):
    # Asynchronous Layer
    class AsyncLayer(threading.Thread):
        def __init__(self, task_queue: queue.Queue):
            super().__init__()
            self.task_queue = task_queue
            self.stop_event = threading.Event()

        def run(self) -> None:
            while not self.stop_event.is_set():
                try:
                    task = self.task_queue.get(timeout=1)
                    task()
                except queue.Empty:
                    continue

        def stop(self) -> None:
            self.stop_event.set()

    # Synchronous Layer
    class SyncLayer:
        def __init__(self, task_queue: queue.Queue):
            self.task_queue = task_queue

        def process_request(self, request: str) -> None:
            print(f"Processing request: {request}")
            self.task_queue.put(lambda: self.handle_request(request))

        @staticmethod
        def handle_request(request: str) -> None:
            time.sleep(2)  # Simulate a long-running task
            print(f"Handled request: {request}")

    def example(self):
        task_queue = queue.Queue()
        async_layer = PyHalfSyncOrHalfAsyncPattern.AsyncLayer(task_queue)
        sync_layer = PyHalfSyncOrHalfAsyncPattern.SyncLayer(task_queue)

        async_layer.start()

        sync_layer.process_request("Request 1")
        sync_layer.process_request("Request 2")

        time.sleep(5)  # Allow some time for processing
        async_layer.stop()
        async_layer.join()
