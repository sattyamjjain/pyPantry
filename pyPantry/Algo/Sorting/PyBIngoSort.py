from pyPantry.Algo import PyAlgo


class PyBingoSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        while n > 1:
            max_index = 0
            for i in range(n):
                if self.arr[i] > self.arr[max_index]:
                    max_index = i

            if max_index != n - 1:
                self.arr[max_index], self.arr[n - 1] = self.arr[n - 1], self.arr[max_index]

            max_val = self.arr[n - 1]
            i = 0
            while i < n - 1:
                if self.arr[i] == max_val:
                    self.arr[i], self.arr[n - 2] = self.arr[n - 2], self.arr[i]
                    n -= 1
                else:
                    i += 1

            n -= 1

        return self.arr
