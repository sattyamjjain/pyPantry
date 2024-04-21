from pyPantry.Algo import PyAlgo


class PyPigeonholeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        if len(self.arr) == 0:
            return []

        n = len(self.arr)
        min_val = min(self.arr)
        max_val = max(self.arr)

        range_val = max_val - min_val + 1

        pigeonholes = [0] * range_val

        for i in self.arr:
            pigeonholes[i - min_val] += 1

        index = 0
        for count in range(range_val):
            while pigeonholes[count] > 0:
                pigeonholes[count] -= 1
                self.arr[index] = count + min_val
                index += 1

        return self.arr
