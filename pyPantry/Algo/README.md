
# pyPantry: Algorithms

This section of the `pyPantry` library provides robust implementations of various algorithms. These algorithms are essential for solving a wide range of computational problems efficiently.

## 📋 Table of Contents

- [Features](#features)
- [Algorithms](#algorithms)
  - [Searching](#searching)
  - [Sorting](#sorting)
- [Testing](#testing)

## 🌟 Features

This module includes the following algorithms:

### Searching

Searching algorithms are designed to retrieve information stored within some data structure. The algorithms implemented in this module include:

- **Binary Search**: `PyBinarySearch.py`
  - Finds the position of a target value within a sorted array.
- **Jump Search**: `PyJumpSearch.py`
  - Searches for an element in a sorted array by jumping ahead by fixed steps and then performing a linear search.
- **Linear Search**: `PyLinearSearch.py`
  - Checks each element of a list sequentially until the desired element is found or the list ends.
- **Fibonacci Search**: `PyFibonacciSearch.py`
  - Searches for an element in a sorted array using Fibonacci numbers to divide the array into smaller parts.
- **Exponential Search**: `PyExponentialSearch.py`
  - Searches for an element in a sorted array by first finding the range where the element is likely to be and then performing a binary search within that range.
- **Ternary Search**: `PyTernarySearch.py`
  - Similar to binary search but divides the array into three parts instead of two.
- **Meta Binary Search**: `PyMetaBinarySearch.py`
  - A variant of binary search that uses bit manipulation to perform the search.
- **Sentinel Linear Search**: `PySentinelLinearSearch.py`
  - An optimized version of linear search that reduces the number of comparisons.
- **Interpolation Search**: `PyInterpolationSearch.py`
  - An improved variant of binary search for uniformly distributed data.

### Sorting

Sorting algorithms are designed to arrange elements in a particular order (typically ascending or descending). The algorithms implemented in this module include:

- **BogoSort**: `PyBogoSort.py`
  - A highly ineffective sorting algorithm based on generating permutations of its input until it is sorted.
- **Odd-Even Sort**: `PyOddEvenSort.py`
  - A parallel version of bubble sort.
- **Sleep Sort**: `PySleepSort.py`
  - A novelty sorting algorithm that works by spawning processes that "sleep" for a time proportional to their value.
- **Cocktail Sort**: `PyCocktailSort.py`
  - A variation of bubble sort that sorts in both directions on each pass through the list.
- **Radix Sort**: `PyRadixSort.py`
  - A non-comparative sorting algorithm that sorts integers by processing individual digits.
- **Bubble Sort**: `PyBubbleSort.py`
  - A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Selection Sort**: `PySelectionSort.py`
  - A simple in-place comparison sorting algorithm that divides the input list into two parts: the sorted part and the unsorted part, and repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part.
- **Bingo Sort**: `PyBingoSort.py`
  - A variation of selection sort that repeatedly selects the smallest element and moves it to the front.
- **QuickSort**: `PyQuickSort.py`
  - An efficient sorting algorithm that uses divide-and-conquer to sort elements.
- **Counting Sort**: `PyCountingSort.py`
  - A non-comparative sorting algorithm that sorts integers by counting the number of occurrences of each unique element.
- **Bucket Sort**: `PyBucketSort.py`
  - A sorting algorithm that works by distributing elements into a number of buckets, each of which is then sorted individually.
- **Gnome Sort**: `PyGnomeSort.py`
  - A simple sorting algorithm that is similar to insertion sort but with a different approach to moving elements.
- **HeapSort**: `PyHeapSort.py`
  - A comparison-based sorting algorithm that uses a binary heap data structure.
- **Bitonic Sort**: `PyBitonicSort.py`
  - A parallel algorithm that sorts bitonic sequences (sequences that first increase then decrease).
- **Strand Sort**: `PyStrandSort.py`
  - A recursive sorting algorithm that sorts elements by extracting sorted sublists and merging them.
- **Shell Sort**: `PyShellSort.py`
  - An optimization of insertion sort that allows the exchange of items that are far apart.
- **TimSort**: `PyTimSort.py`
  - A hybrid sorting algorithm derived from merge sort and insertion sort.
- **Pancake Sort**: `PyPancakeSort.py`
  - A sorting algorithm that sorts a list by flipping sublists like pancakes.

## 🧪 Testing

All implementations come with corresponding test files located in the `tests` directory, ensuring reliability and correctness.

To run tests, use:
```bash
python -m unittest discover tests/Algo
```