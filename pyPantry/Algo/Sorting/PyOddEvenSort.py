from pyPantry.Algo import PyAlgo


class PyOddEvenSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        is_sorted = False

        while not is_sorted:
            is_sorted = True

            for i in range(1, n - 1, 2):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    is_sorted = False

            for i in range(0, n - 1, 2):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    is_sorted = False

        return self.arr
