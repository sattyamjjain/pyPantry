from pyPantry.Algo import PyAlgo


class PyCycleSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    def sort(self):
        writes = 0
        n = len(self.arr)

        for cycleStart in range(0, n - 1):
            item = self.arr[cycleStart]

            pos = cycleStart
            for i in range(cycleStart + 1, n):
                if self.arr[i] < item:
                    pos += 1

            if pos == cycleStart:
                continue

            while item == self.arr[pos]:
                pos += 1
            self.arr[pos], item = item, self.arr[pos]
            writes += 1

            while pos != cycleStart:
                pos = cycleStart
                for i in range(cycleStart + 1, n):
                    if self.arr[i] < item:
                        pos += 1
                while item == self.arr[pos]:
                    pos += 1
                self.arr[pos], item = item, self.arr[pos]
                writes += 1

        return self.arr
