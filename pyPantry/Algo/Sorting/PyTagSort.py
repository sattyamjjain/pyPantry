from pyPantry.Algo import PyAlgo


class PyTagSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        ranks = [0] * n
        for i in range(n):
            for j in range(n):
                if self.arr[i] > self.arr[j] or (self.arr[i] == self.arr[j] and i < j):
                    ranks[i] += 1

        output = [0] * n
        for i in range(n):
            output[ranks[i]] = self.arr[i]

        return output
