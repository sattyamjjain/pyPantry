from pyPantry.Algo import PyAlgo


class PyQuickSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def partition(self, low, high):
        pivot = self.arr[high]
        i = low - 1
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def _quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self._quick_sort(low, pi - 1)
            self._quick_sort(pi + 1, high)

    def sort(self):
        self._quick_sort(0, len(self.arr) - 1)
        return self.arr
