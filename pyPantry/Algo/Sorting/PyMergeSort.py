from pyPantry.Algo import PyAlgo


class PyMergeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    @staticmethod
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr

        mid = len(self.arr) // 2
        left_half = self.arr[:mid]
        right_half = self.arr[mid:]

        left_sorted = PyMergeSort(left_half).sort()
        right_sorted = PyMergeSort(right_half).sort()

        return self.merge(left_sorted, right_sorted)
