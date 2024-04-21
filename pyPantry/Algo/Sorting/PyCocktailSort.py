from pyPantry.Algo import PyAlgo


class PyCocktailSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        n = len(self.arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False

            for i in range(start, end):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False

            end -= 1

            for i in range(end - 1, start - 1, -1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True

            start += 1
        return self.arr
