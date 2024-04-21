from pyPantry.Algo import PyAlgo


class Py3WayMergeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def merge(self, low, mid1, mid2, high):
        temp = [0] * (high - low + 1)
        i, j, k, l = low, mid1, mid2, 0

        while i < mid1 and j < mid2 and k <= high:
            if self.arr[i] < self.arr[j]:
                if self.arr[i] < self.arr[k]:
                    temp[l] = self.arr[i]
                    l += 1
                    i += 1
                else:
                    temp[l] = self.arr[k]
                    l += 1
                    k += 1
            else:
                if self.arr[j] < self.arr[k]:
                    temp[l] = self.arr[j]
                    l += 1
                    j += 1
                else:
                    temp[l] = self.arr[k]
                    l += 1
                    k += 1

        while i < mid1:
            temp[l] = self.arr[i]
            l += 1
            i += 1

        while j < mid2:
            temp[l] = self.arr[j]
            l += 1
            j += 1

        while k <= high:
            temp[l] = self.arr[k]
            l += 1
            k += 1

        for i in range(low, high + 1):
            self.arr[i] = temp[i - low]

    def sort_recursive(self, low, high):
        if high <= low:
            return

        mid1 = low + (high - low) // 3
        mid2 = low + 2 * (high - low) // 3 + 1

        print("low:", low, "mid1:", mid1, "mid2:", mid2, "high:", high)

        self.sort_recursive(low, mid1)
        self.sort_recursive(mid1, mid2)
        self.sort_recursive(mid2, high)

        self.merge(low, mid1, mid2, high)

    def sort(self):
        self.sort_recursive(0, len(self.arr) - 1)
        return self.arr
