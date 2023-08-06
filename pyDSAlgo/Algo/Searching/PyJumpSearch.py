from pyDSAlgo.Algo import PyAlgo
import math


class PyJumpSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        n = len(self.arr)

        if n == 0:
            return -1

        step = int(math.sqrt(n))
        prev = 0

        while step < n and self.arr[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1

        for i in range(prev, min(step, n)):
            if self.arr[i] == target:
                return i

        return -1
