
# pyPantry: Your One-Stop Solution for  DSA, Design Patterns and etc. in Python

`pyPantry` is a comprehensive Python library offering robust implementations of numerous data structures and algorithms. It serves as a reliable tool for educators, students, developers, and anyone keen on mastering or utilizing these foundational computer science concepts.

## 📋 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Data Structures](#data-structures)
  - [Algorithms](#algorithms)
  - [Design Patterns](#design-patterns)
- [Testing](#testing)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## 🌟 Features

### Data Structures

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

### Algorithms

#### Searching

- **Binary Search**: `PyBinarySearch.py`
- **Jump Search**: `PyJumpSearch.py`
- **Linear Search**: `PyLinearSearch.py`
- **Fibonacci Search**: `PyFibonacciSearch.py`
- **Exponential Search**: `PyExponentialSearch.py`
- **Ternary Search**: `PyTernarySearch.py`
- **Meta Binary Search**: `PyMetaBinarySearch.py`
- **Sentinel Linear Search**: `PySentinelLinearSearch.py`
- **Interpolation Search**: `PyInterpolationSearch.py`

#### Sorting

- **BogoSort**: `PyBogoSort.py`
- **Odd-Even Sort**: `PyOddEvenSort.py`
- **Sleep Sort**: `PySleepSort.py`
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

### Design Patterns

#### Architectural Patterns

- **Event-Driven Architecture**: `PyEventDrivenArchitecturePattern.py`
- **Microservices**: `PyMicroservicesPattern.py`
- **Model-View-Controller (MVC)**: `PyModelViewControllerPattern.py`
- **Model-View-ViewModel (MVVM)**: `PyModelViewViewModelPattern.py`
- **Service-Oriented Architecture (SOA)**: `PyServiceOrientedArchitecturePattern.py`

#### Behavioral Patterns

- **Chain of Responsibility**: `PyChainOfResponsibilityPattern.py`
- **Command**: `PyCommandPattern.py`
- **Interpreter**: `PyInterpreterPattern.py`
- **Iterator**: `PyIteratorPattern.py`
- **Mediator**: `PyMediatorPattern.py`
- **Memento**: `PyMementoPattern.py`
- **Null Object**: `PyNullObjectPattern.py`
- **Observer**: `PyObserverPattern.py`
- **Specification**: `PySpecificationPattern.py`
- **State**: `PyStatePattern.py`
- **Strategy**: `PyStrategyPattern.py`
- **Template**: `PyTemplatePattern.py`
- **Visitor**: `PyVisitorPattern.py`

#### Concurrency Patterns

- **Active Object**: `PyActiveObjectPattern.py`
- **Half-Sync/Half-Async**: `PyHalfSyncOrHalfAsyncPattern.py`
- **Leader-Follower**: `PyLeaderOrFollowerPattern.py`
- **Reactor**: `PyReactorPattern.py`
- **Thread Pool**: `PyThreadPoolPattern.py`

#### Creational Patterns

- **Abstract Factory**: `PyAbstractFactoryPattern.py`
- **Builder**: `PyBuilderPattern.py`
- **Factory Method**: `PyFactoryPattern.py`
- **Object Pool**: `PyObjectPoolPattern.py`
- **Prototype**: `PyPrototypePattern.py`
- **Singleton**: `PySingletonPattern.py`

#### Structural Patterns

- **Adapter**: `PyAdapterPattern.py`
- **Bridge**: `PyBridgePattern.py`
- **Composite**: `PyCompositePattern.py`
- **Decorator**: `PyDecoratorPattern.py`
- **Facade**: `PyFacadePattern.py`
- **Flyweight**: `PyFlyweightPattern.py`
- **Private Class Data**: `PyPrivateClassDataPattern.py`
- **Proxy**: `PyProxyPattern.py`

## 🔧 Installation

```bash
pip install python-Pantry 
```

## 🚀 Usage

### Data Structures

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

### Algorithms

```python
from pyPantry.Algo.Sorting.PyBubbleSort import PyBubbleSort

# Sample list to be sorted
sample_list = [64, 34, 25, 12, 22, 11, 90]

# Apply bubble sort
sorted_list = PyBubbleSort(arr=sample_list).sort()
print(sorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### Design Patterns

#### Strategy Pattern

```python
from pyPantry.DesignPatterns.Behavioral.Strategy.PyStrategyPattern import PyStrategyPattern

class CreditCardPayment(PyStrategyPattern.PaymentStrategy):
    def pay(self, amount):
        return f"Paid {amount} using Credit Card"

payment_method = CreditCardPayment()
print(payment_method.pay(100))  # Output: Paid 100 using Credit Card
```

## 🧪 Testing

All implementations come with corresponding test files located in the `tests` directory, ensuring reliability and correctness.

To run tests, use:
```bash
python -m unittest discover tests
```

## 🤝 Contributing

We welcome and value contributions from the open-source community. Your input, whether it's a bug fix, feature addition, or documentation improvement, helps enhance `pyPantry`.

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## 👏 Credits

Crafted with ❤️ by [Sattyam Jain](https://www.linkedin.com/in/sattyamjain/).

## 📜 License

Licensed under the [MIT License](LICENSE).

## 📞 Contact

For feedback or queries, [contact us](https://www.linkedin.com/in/sattyamjain/). We're always eager to connect!
