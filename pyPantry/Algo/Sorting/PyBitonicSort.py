from pyPantry.Algo import PyAlgo


class PyBitonicSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def compare_and_swap(self, i, j, direction):
        if (direction == 1 and self.arr[i] > self.arr[j]) or (direction == 0 and self.arr[i] < self.arr[j]):
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def bitonic_merge(self, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            for i in range(low, low + k):
                self.compare_and_swap(i, i + k, direction)
            self.bitonic_merge(low, k, direction)
            self.bitonic_merge(low + k, k, direction)

    def bitonic_sort_recursive(self, low, cnt, direction):
        if cnt > 1:
            k = cnt // 2
            self.bitonic_sort_recursive(low, k, 1)
            self.bitonic_sort_recursive(low + k, k, 0)
            self.bitonic_merge(low, cnt, direction)

    def sort(self):
        self.bitonic_sort_recursive(0, len(self.arr), 1)
        return self.arr
