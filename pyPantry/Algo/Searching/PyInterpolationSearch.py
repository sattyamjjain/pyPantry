from pyPantry.Algo import PyAlgo


class PyInterpolationSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        low = 0
        high = len(self.arr) - 1

        while low <= high and self.arr[low] <= target <= self.arr[high]:
            position = low + int(((target - self.arr[low]) * (high - low)) / (self.arr[high] - self.arr[low]))
            if self.arr[position] == target:
                return position
            if self.arr[position] < target:
                low = position + 1
            else:
                high = position - 1
        return -1
