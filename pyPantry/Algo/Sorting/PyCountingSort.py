from pyPantry.Algo import PyAlgo


class PyCountingSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        if not self.arr:
            return []
        min_val = min(self.arr)
        max_val = max(self.arr)
        count = [0] * (max_val - min_val + 1)
        for num in self.arr:
            count[num - min_val] += 1
        sorted_arr = []
        for i, freq in enumerate(count):
            sorted_arr.extend([i + min_val] * freq)
        return sorted_arr
