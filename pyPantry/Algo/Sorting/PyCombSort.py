from pyPantry.Algo import PyAlgo


class PyCombSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        gap = n
        swapped = True

        while gap != 1 or swapped:
            gap = int(gap / 1.3)
            if gap < 1:
                gap = 1
            swapped = False

            for i in range(0, n - gap):
                if self.arr[i] > self.arr[i + gap]:
                    self.arr[i], self.arr[i + gap] = self.arr[i + gap], self.arr[i]
                    swapped = True

        return self.arr
