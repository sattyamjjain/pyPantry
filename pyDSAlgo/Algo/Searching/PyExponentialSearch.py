from pyDSAlgo.Algo import PyAlgo


class PyExponentialSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def binary_search(self, l, r, target):
        while l <= r:
            mid = (l + r) // 2

            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

    def search(self, target):
        if len(self.arr) == 0:
            return -1

        if self.arr[0] == target:
            return 0

        i = 1
        while i < len(self.arr) and self.arr[i] <= target:
            i *= 2

        return self.binary_search(i // 2, min(i, len(self.arr) - 1), target)
