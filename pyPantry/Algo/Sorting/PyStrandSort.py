from pyPantry.Algo import PyAlgo


class PyStrandSort(PyAlgo):
    def __init__(self, arr):
        super().__init__()
        self.arr = arr

    @staticmethod
    def merge(a, b):
        result = []
        while (len(a) > 0) and (len(b) > 0):
            if a[0] < b[0]:
                result.append(a[0])
                a.pop(0)
            else:
                result.append(b[0])
                b.pop(0)
        if len(a) == 0:
            result += b
        else:
            result += a
        return result

    def sort(self):
        if len(self.arr) <= 1:
            return self.arr

        result = []
        while len(self.arr) > 0:
            sublist = [self.arr.pop(0)]
            i = 0
            while i < len(self.arr):
                if self.arr[i] > sublist[-1]:
                    sublist.append(self.arr.pop(i))
                else:
                    i += 1
            result = self.merge(result, sublist)

        return result
