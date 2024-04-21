import threading
import time
from pyPantry.Algo import PyAlgo


class PySleepSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr
        self.result = []

    def _sleep_and_append(self, val):
        time.sleep(val)
        self.result.append(val)

    def sort(self):
        threads = []
        for val in self.arr:
            thread = threading.Thread(target=self._sleep_and_append, args=(val,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        return self.result
