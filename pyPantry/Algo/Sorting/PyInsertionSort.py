from pyPantry.Algo import PyAlgo


class PyInsertionSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and key < self.arr[j]:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
        return self.arr
