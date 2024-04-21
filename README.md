
# pyPantry: Your One-Stop Solution for Data Structures and Algorithms in Python

`pyPantry` is a comprehensive Python library offering robust implementations of numerous data structures and algorithms. It serves as a reliable tool for educators, students, developers, and anyone keen on mastering or utilizing these foundational computer science concepts.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## 🌟 Features

### Data Structures:

- **Graph**: Traverse complex networks. 
  - `PyGraph.py`
  - `PyLinkedGraph.py`
  
- **Heap**: Efficient data management.
  - `PyMaxHeap.py`
  - `PyMinHeap.py`
  
- **LinkedList**: Flexible data storage.
  - `PyCircularLinkedList.py`
  - `PyDoublyCircularLinkedList.py`
  - `PyDoublyLinkedList.py`
  - `PyHeaderLinkedList.py`
  - `PyLinkedList.py`
  - `PySkipLinkedList.py`
  
- **Queue**: FIFO data handling.
  - `PyCircularQueue.py`
  - `PyDeque.py`
  - `PyPriorityQueue.py`
  - `PyQueue.py`
  
- **Stack**: LIFO data access.
  - `PyStack.py`
  - `pyLinkedStack.py`
  
- **Tree**: Hierarchical data modeling.
  - `PyAVLTree.py`
  - `PyBTree.py`
  - `PyBinarySearchTree.py`
  - `PyBinaryTree.py`
  - `PyGenericTree.py`
  
- **Trie**: Rapid text retrieval.
  - `PyTrie.py`

### Algorithms:

#### Searching:

- **Binary Search**: `PyBinarySearch.py`
- **Jump Search**: `PyJumpSearch.py`
- **Linear Search**: `PyLinearSearch.py`
- **Fibonacci Search**: `PyFibonacciSearch.py`
- **Exponential Search**: `PyExponentialSearch.py`
- **Ternary Search**: `PyTernarySearch.py`
- **Meta Binary Search**: `PyMetaBinarySearch.py`
- **Sentinel Linear Search**: `PySentinelLinearSearch.py`
- **Interpolation Search**: `PyInterpolationSearch.py`

#### Sorting:

- **BogoSort**: `PyBogoSort.py`
- **Odd-Even Sort**: `PyOddEvenSort.py`
- **Sleep Sort**: `PySleepSort.py`
- **Insertion Sort**: `PyInsertionSort.py`
- **Tree Sort**: `PyTreeSort.py`
- **Pigeonhole Sort**: `PyPigeonholeSort.py`
- **3-Way Merge Sort**: `Py3WayMergeSort.py`
- **Cycle Sort**: `PyCycleSort.py`
- **Stooge Sort**: `PyStoogeSort.py`
- **Merge Sort**: `PyMergeSort.py`
- **Comb Sort**: `PyCombSort.py`
- **Tag Sort**: `PyTagSort.py`
- **Cocktail Sort**: `PyCocktailSort.py`
- **Radix Sort**: `PyRadixSort.py`
- **Bubble Sort**: `PyBubbleSort.py`
- **Selection Sort**: `PySelectionSort.py`
- **Bingo Sort**: `PyBingoSort.py`
- **QuickSort**: `PyQuickSort.py`
- **Counting Sort**: `PyCountingSort.py`
- **Bucket Sort**: `PyBucketSort.py`
- **Gnome Sort**: `PyGnomeSort.py`
- **HeapSort**: `PyHeapSort.py`
- **Bitonic Sort**: `PyBitonicSort.py`
- **Strand Sort**: `PyStrandSort.py`
- **Shell Sort**: `PyShellSort.py`
- **TimSort**: `PyTimSort.py`
- **Pancake Sort**: `PyPancakeSort.py`

## 🔧 Installation

```bash
pip install pyPantry
```

## 🚀 Usage

### Data Structures:

```python
from pyPantry.DS.Stack.PyStack import PyStack

# Create a new stack
stack = PyStack()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Pop an element from the stack
print(stack.pop())  # Output: 3
```

### Algorithms:

```python
from pyPantry.Algo.Sorting.PyBubbleSort import PyBubbleSort

# Sample list to be sorted
sample_list = [64, 34, 25, 12, 22, 11, 90]

# Apply bubble sort
sorted_list = PyBubbleSort(arr=sample_list).sort()
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

## 🧪 Testing

All implementations come with corresponding test files located in the `tests` directory, ensuring reliability and correctness.

## 🤝 Contributing

We welcome and value contributions from the open-source community. Your input, whether it's a bug fix, feature addition, or documentation improvement, helps enhance `pyPantry`.

## 👏 Credits

Crafted with ❤️ by [Sattyam Jain](https://www.linkedin.com/in/sattyamjain/).

## 📜 License

Licensed under the [MIT License](https://github.com/sattyamjjain/pyPantry/blob/main/LICENSE).

## 📞 Contact

For feedback or queries, [contact us](https://www.linkedin.com/in/sattyamjain/). We're always eager to connect!
