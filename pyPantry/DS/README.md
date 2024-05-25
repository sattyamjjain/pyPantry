
# pyPantry: Data Structures

This section of the `pyPantry` library offers robust implementations of various data structures. These data structures are essential building blocks in computer science and are widely used in algorithm design and optimization.

## 📋 Table of Contents

- [Features](#features)
- [Data Structures](#data-structures)
  - [Graph](#graph)
  - [Heap](#heap)
  - [LinkedList](#linkedlist)
  - [Queue](#queue)
  - [Stack](#stack)
  - [Tree](#tree)
  - [Trie](#trie)
- [Usage](#usage)
- [Testing](#testing)

## 🌟 Features

This module includes the following data structures:

### Graph

Graphs are data structures used to represent pairwise relationships between objects. A graph consists of vertices (also called nodes) and edges connecting these vertices.

- `PyGraph.py`: Basic graph implementation.
- `PyLinkedGraph.py`: Graph implementation using linked lists.

### Heap

Heaps are specialized tree-based data structures that satisfy the heap property. They are commonly used to implement priority queues.

- `PyMaxHeap.py`: Max-heap implementation where the parent node is always greater than or equal to the child nodes.
- `PyMinHeap.py`: Min-heap implementation where the parent node is always less than or equal to the child nodes.

### LinkedList

Linked lists are linear data structures where each element is a separate object. Each element (or node) contains a reference to the next node in the sequence.

- `PyCircularLinkedList.py`: Circular linked list implementation.
- `PyDoublyCircularLinkedList.py`: Doubly circular linked list implementation.
- `PyDoublyLinkedList.py`: Doubly linked list implementation.
- `PyHeaderLinkedList.py`: Linked list with a header node.
- `PyLinkedList.py`: Singly linked list implementation.
- `PySkipLinkedList.py`: Skip list implementation, which allows for faster search within an ordered sequence of elements.

### Queue

Queues are abstract data types that follow the FIFO (First In, First Out) principle. They are used in various scenarios like scheduling processes, handling requests, etc.

- `PyCircularQueue.py`: Circular queue implementation.
- `PyDeque.py`: Double-ended queue implementation.
- `PyPriorityQueue.py`: Priority queue implementation.
- `PyQueue.py`: Basic queue implementation.

### Stack

Stacks are abstract data types that follow the LIFO (Last In, First Out) principle. They are used in scenarios like function call management, parsing expressions, etc.

- `PyStack.py`: Basic stack implementation.
- `pyLinkedStack.py`: Linked stack implementation.

### Tree

Trees are hierarchical data structures with a root value and subtrees of children represented as a set of linked nodes.

- `PyAVLTree.py`: AVL tree implementation, a self-balancing binary search tree.
- `PyBTree.py`: B-tree implementation, a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions.
- `PyBinarySearchTree.py`: Binary search tree implementation.
- `PyBinaryTree.py`: Basic binary tree implementation.
- `PyGenericTree.py`: Generic tree implementation.

### Trie

Tries are a type of search tree used to store associative data structures. A common application of a trie is storing a predictive text or autocomplete dictionary.

- `PyTrie.py`: Trie implementation.

## 🚀 Usage

### Graph Example

```python
from pyPantry.DS.Graph.PyGraph import Graph

# Create a new graph
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print(graph)  # Output the graph structure
```

### Heap Example

```python
from pyPantry.DS.Heap.PyMaxHeap import MaxHeap

# Create a max heap
max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(4)
max_heap.insert(9)
max_heap.insert(1)
max_heap.insert(7)
max_heap.insert(5)
max_heap.insert(3)

print(max_heap.extract_max())  # Output: 10
```

### LinkedList Example

```python
from pyPantry.DS.LinkedList.PyLinkedList import LinkedList

# Create a new linked list
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

print(linked_list)  # Output the linked list
```

## 🧪 Testing

All implementations come with corresponding test files located in the `tests` directory, ensuring reliability and correctness.

To run tests, use:
```bash
python -m unittest discover tests/DS
```