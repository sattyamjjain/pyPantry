import random
from pyPantry.Algo import PyAlgo


class PyBogoSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def is_sorted(self):
        for i in range(1, len(self.arr)):
            if self.arr[i - 1] > self.arr[i]:
                return False
        return True

    def sort(self):
        while not self.is_sorted():
            random.shuffle(self.arr)
        return self.arr
