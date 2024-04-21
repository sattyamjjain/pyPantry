from pyPantry.Algo import PyAlgo


class PyGnomeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        idx = 0
        while idx < len(self.arr):
            if idx == 0 or self.arr[idx] >= self.arr[idx - 1]:
                idx += 1
            else:
                self.arr[idx], self.arr[idx - 1] = self.arr[idx - 1], self.arr[idx]
                idx -= 1
        return self.arr
