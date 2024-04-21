from pyPantry.Algo import PyAlgo


class PyFibonacciSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        n = len(self.arr)
        fib_m2, fib_m1 = 0, 1
        fib_m = fib_m2 + fib_m1

        while fib_m < n:
            fib_m2 = fib_m1
            fib_m1 = fib_m
            fib_m = fib_m2 + fib_m1

        offset = -1

        while fib_m > 1:
            i = min(offset + fib_m2, n - 1)

            if self.arr[i] < target:
                fib_m = fib_m1
                fib_m1 = fib_m2
                fib_m2 = fib_m - fib_m1
                offset = i

            elif self.arr[i] > target:
                fib_m = fib_m2
                fib_m1 = fib_m1 - fib_m2
                fib_m2 = fib_m - fib_m1

            else:
                return i

        if fib_m1 and self.arr[offset + 1] == target:
            return offset + 1

        return -1
