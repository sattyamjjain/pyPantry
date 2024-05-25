import threading
import queue
import time

from pyPantry.DesignPatterns import PyDesignPatterns


class PyThreadPoolPattern(PyDesignPatterns):
    class ThreadPool:
        def __init__(self, num_threads):
            self.tasks = queue.Queue()
            self.threads = []
            self.stop_event = threading.Event()

            for _ in range(num_threads):
                thread = threading.Thread(target=self.worker)
                thread.start()
                self.threads.append(thread)

        def worker(self):
            while not self.stop_event.is_set():
                try:
                    task, args, kwargs = self.tasks.get(timeout=1)
                    task(*args, **kwargs)
                    self.tasks.task_done()
                except queue.Empty:
                    continue

        def add_task(self, task, *args, **kwargs):
            self.tasks.put((task, args, kwargs))

        def shutdown(self):
            self.tasks.join()  # Wait for all tasks to be completed
            self.stop_event.set()
            for thread in self.threads:
                thread.join()

    def example(self):
        def example_task(duration):
            print(f"Task running for {duration} seconds")
            time.sleep(duration)
            print(f"Task completed in {duration} seconds")

        pool = PyThreadPoolPattern.ThreadPool(3)

        pool.add_task(example_task, 2)
        pool.add_task(example_task, 3)
        pool.add_task(example_task, 1)

        time.sleep(5)
        pool.shutdown()
