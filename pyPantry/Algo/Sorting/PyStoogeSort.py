from pyPantry.Algo import PyAlgo


class PyStoogeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort_recursive(self, l, h):
        if l >= h:
            return

        if self.arr[l] > self.arr[h]:
            self.arr[l], self.arr[h] = self.arr[h], self.arr[l]

        if h - l + 1 > 2:
            t = (h - l + 1) // 3
            self.sort_recursive(l, h - t)
            self.sort_recursive(l + t, h)
            self.sort_recursive(l, h - t)

    def sort(self):
        self.sort_recursive(0, len(self.arr) - 1)
        return self.arr
