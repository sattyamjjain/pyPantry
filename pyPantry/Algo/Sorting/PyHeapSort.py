from pyPantry.Algo import PyAlgo


class PyHeapSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def heapify(self, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.arr[l] > self.arr[largest]:
            largest = l

        if r < n and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(n, largest)

    def sort(self):
        n = len(self.arr)

        for i in range(n // 2, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(i, 0)

        return self.arr
