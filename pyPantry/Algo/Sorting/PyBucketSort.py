from pyPantry.Algo import PyAlgo


class PyBucketSort(PyAlgo):
    def __init__(self, arr, num_buckets):
        super().__init__()
        self.arr = arr
        self.num_buckets = num_buckets

    def sort(self):
        if len(self.arr) == 0:
            return []
        if len(self.arr) == 1:
            return self.arr

        buckets = [[] for _ in range(self.num_buckets)]

        max_val, min_val = max(self.arr), min(self.arr)
        for num in self.arr:
            index = int(self.num_buckets * (num - min_val) / (max_val - min_val))
            index = max(0, min(index, self.num_buckets - 1))
            buckets[index].append(num)

        for bucket in buckets:
            bucket.sort()

        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)

        return sorted_arr
