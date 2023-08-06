from pyDSAlgo.Algo import PyAlgo


class PyTernarySearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        l, r = 0, len(self.arr) - 1
        while l <= r:
            mid1 = l + (r - l) // 3
            mid2 = r - (r - l) // 3

            if self.arr[mid1] == target:
                return mid1
            if self.arr[mid2] == target:
                return mid2

            if target < self.arr[mid1]:
                r = mid1 - 1
            elif target > self.arr[mid2]:
                l = mid2 + 1
            else:
                l = mid1 + 1
                r = mid2 - 1

        return -1
