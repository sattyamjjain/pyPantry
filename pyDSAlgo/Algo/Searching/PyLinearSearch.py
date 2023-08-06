from pyDSAlgo.Algo import PyAlgo


class PyLinearSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        for i, value in enumerate(self.arr):
            if value == target:
                return i
        return -1
