from pyPantry.Algo import PyAlgo


class PySentinelLinearSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        if not self.arr:
            return -1

        last_element = self.arr[-1]
        self.arr[-1] = target

        i = 0
        while self.arr[i] != target:
            i += 1

        self.arr[-1] = last_element

        if i == len(self.arr) - 1 and last_element != target:
            return -1

        return i
