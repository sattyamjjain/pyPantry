from pyPantry.Algo import PyAlgo


class PyRadixSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def counting_sort(self, exp):
        n = len(self.arr)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = (self.arr[i] // exp) % 10
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (self.arr[i] // exp) % 10
            output[count[index] - 1] = self.arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            self.arr[i] = output[i]

    def sort(self):
        if len(self.arr) == 0:
            return []

        max_val = max(self.arr)

        exp = 1
        while max_val // exp > 0:
            self.counting_sort(exp)
            exp *= 10

        return self.arr
