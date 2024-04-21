from pyPantry.Algo import PyAlgo


class PyShellSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.arr[i]
                j = i
                while j >= gap and self.arr[j - gap] > temp:
                    self.arr[j] = self.arr[j - gap]
                    j -= gap
                self.arr[j] = temp
            gap //= 2
        return self.arr
