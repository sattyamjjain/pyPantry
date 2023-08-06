from pyDSAlgo.Algo import PyAlgo


class PyBinarySearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = sorted(arr)

    def search(self, target):
        left, right = 0, len(self.arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.arr[mid] == target:
                return mid
            elif self.arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
