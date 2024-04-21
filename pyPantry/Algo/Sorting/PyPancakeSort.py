from pyPantry.Algo import PyAlgo


class PyPancakeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def flip(self, k):
        left = 0
        while left < k:
            self.arr[left], self.arr[k] = self.arr[k], self.arr[left]
            left += 1
            k -= 1

    def max_index(self, n):
        mi = 0
        for i in range(n + 1):
            if self.arr[i] > self.arr[mi]:
                mi = i
        return mi

    def sort(self):
        n = len(self.arr)
        while n > 1:
            mi = self.max_index(n - 1)
            if mi != n - 1:
                self.flip(mi)
                self.flip(n - 1)
            n -= 1
        return self.arr
