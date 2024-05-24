from pyPantry.Algo import PyAlgo


class Py3WayMergeSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def merge(self, low, mid1, mid2, high):
        temp = [0] * (high - low + 1)
        i, j, k, l = low, mid1, mid2, 0

        # Merge the three parts into temp array
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

        # Merge remaining elements of the first part
        while i < mid1 and j < mid2:
            if self.arr[i] < self.arr[j]:
                temp[l] = self.arr[i]
                l += 1
                i += 1
            else:
                temp[l] = self.arr[j]
                l += 1
                j += 1

        while j < mid2 and k <= high:
            if self.arr[j] < self.arr[k]:
                temp[l] = self.arr[j]
                l += 1
                j += 1
            else:
                temp[l] = self.arr[k]
                l += 1
                k += 1

        while k <= high and i < mid1:
            if self.arr[k] < self.arr[i]:
                temp[l] = self.arr[k]
                l += 1
                k += 1
            else:
                temp[l] = self.arr[i]
                l += 1
                i += 1

        # Merge remaining elements of the first part
        while i < mid1:
            temp[l] = self.arr[i]
            l += 1
            i += 1

        # Merge remaining elements of the second part
        while j < mid2:
            temp[l] = self.arr[j]
            l += 1
            j += 1

        # Merge remaining elements of the third part
        while k <= high:
            temp[l] = self.arr[k]
            l += 1
            k += 1

        # Copy the merged elements back into the original array
        for i in range(low, high + 1):
            self.arr[i] = temp[i - low]

    def sort_recursive(self, low, high):
        if low >= high:
            return

        # Divide the array into three parts
        third = (high - low + 1) // 3
        mid1 = low + third
        mid2 = low + 2 * third + 1

        # Sort the first third
        self.sort_recursive(low, mid1 - 1)
        # Sort the second third
        self.sort_recursive(mid1, mid2 - 1)
        # Sort the third part
        self.sort_recursive(mid2, high)

        # Merge the three sorted parts
        self.merge(low, mid1, mid2, high)

    def sort(self):
        self.sort_recursive(0, len(self.arr) - 1)
        return self.arr
