from pyPantry.Algo import PyAlgo


class PySelectionSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        for i in range(n):
            smallest_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[smallest_index]:
                    smallest_index = j
            self.arr[i], self.arr[smallest_index] = self.arr[smallest_index], self.arr[i]
        return self.arr
