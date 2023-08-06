from pyDSAlgo.Algo import PyAlgo


class PyMetaBinarySearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        low, high = 0, 1
        while high < len(self.arr) and self.arr[high] <= target:
            low = high
            high *= 2

        high = min(high, len(self.arr) - 1)

        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
