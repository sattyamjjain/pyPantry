from pyPantry.Algo import PyAlgo


class PyFibonacciSearch(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def search(self, target):
        n = len(self.arr)

        # Initialize the smallest Fibonacci numbers
        fib_m2, fib_m1 = 0, 1
        fib_m = fib_m2 + fib_m1

        # Find the smallest Fibonacci number greater than or equal to n
        while fib_m < n:
            fib_m2 = fib_m1
            fib_m1 = fib_m
            fib_m = fib_m2 + fib_m1

        offset = -1

        # While there are elements to be inspected
        while fib_m > 1:
            i = min(offset + fib_m2, n - 1)

            # If target is greater than the value at index fib_m2, cut the subarray from offset to i
            if self.arr[i] < target:
                fib_m = fib_m1
                fib_m1 = fib_m2
                fib_m2 = fib_m - fib_m1
                offset = i

            # If target is less than the value at index fib_m2, cut the subarray after i+1
            elif self.arr[i] > target:
                fib_m = fib_m2
                fib_m1 = fib_m1 - fib_m2
                fib_m2 = fib_m - fib_m1

            # Element found
            else:
                return i

        # Comparing the last element with target
        if fib_m1 and offset + 1 < n and self.arr[offset + 1] == target:
            return offset + 1

        # Element not found
        return -1
