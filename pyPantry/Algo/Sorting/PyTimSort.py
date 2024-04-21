from pyPantry.Algo import PyAlgo

MIN_MERGE = 32


def calc_min_run(n):
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r


class PyTimSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def insertion_sort(self, left=0, right=None):
        if right is None:
            right = len(self.arr) - 1

        for i in range(left + 1, right + 1):
            key = self.arr[i]
            j = i - 1
            while j >= left and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    def merge(self, l, m, r):
        len1, len2 = m - l + 1, r - m
        left, right = [], []
        for i in range(0, len1):
            left.append(self.arr[l + i])
        for i in range(0, len2):
            right.append(self.arr[m + 1 + i])

        i, j, k = 0, 0, l

        while i < len1 and j < len2:
            if left[i] <= right[j]:
                self.arr[k] = left[i]
                i += 1
            else:
                self.arr[k] = right[j]
                j += 1
            k += 1

        while i < len1:
            self.arr[k] = left[i]
            k += 1
            i += 1

        while j < len2:
            self.arr[k] = right[j]
            k += 1
            j += 1

    def sort(self):
        n = len(self.arr)
        min_run = calc_min_run(n)

        min_run = max(1, min_run)

        for start in range(0, n, min_run):
            end = min(start + min_run - 1, n - 1)
            self.insertion_sort(start, end)

        size = min_run
        while size < n:
            for left in range(0, n, 2 * size):
                mid = min(n - 1, left + size - 1)
                right = min((left + 2 * size - 1), (n - 1))
                self.merge(left, mid, right)
            size *= 2

        return self.arr