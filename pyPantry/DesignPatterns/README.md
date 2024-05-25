
# pyPantry: Design Patterns

This section of the `pyPantry` library provides robust implementations of various design patterns. These design patterns are essential for creating scalable, maintainable, and efficient software systems.

## 📋 Table of Contents

- [Features](#features)
- [Design Patterns](#design-patterns)
  - [Creational Patterns](#creational-patterns)
  - [Structural Patterns](#structural-patterns)
  - [Behavioral Patterns](#behavioral-patterns)
  - [Concurrency Patterns](#concurrency-patterns)
  - [Architectural Patterns](#architectural-patterns)
- [Testing](#testing)

## 🌟 Features

This module includes the following design patterns:

### Creational Patterns

Creational patterns are design patterns that deal with object creation mechanisms, trying to create objects in a manner suitable to the situation.

- **Singleton**: Ensures a class has only one instance and provides a global point of access to it. (`PySingletonPattern.py`)
- **Factory Method**: Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created. (`PyFactoryPattern.py`)
- **Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes. (`PyAbstractFactoryPattern.py`)
- **Builder**: Separates the construction of a complex object from its representation, allowing the same construction process to create different representations. (`PyBuilderPattern.py`)
- **Prototype**: Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype. (`PyPrototypePattern.py`)
- **Object Pool**: Manages a pool of reusable objects to minimize the cost of object creation and garbage collection. (`PyObjectPoolPattern.py`)

### Structural Patterns

Structural patterns are design patterns that ease the design by identifying a simple way to realize relationships between entities.

- **Adapter**: Converts the interface of a class into another interface that clients expect. Allows classes to work together that couldn't otherwise because of incompatible interfaces. (`PyAdapterPattern.py`)
- **Composite**: Composes objects into tree structures to represent part-whole hierarchies. Lets clients treat individual objects and compositions of objects uniformly. (`PyCompositePattern.py`)
- **Proxy**: Provides a surrogate or placeholder for another object to control access to it. (`PyProxyPattern.py`)
- **Flyweight**: Uses sharing to support large numbers of fine-grained objects efficiently. (`PyFlyweightPattern.py`)
- **Facade**: Provides a unified interface to a set of interfaces in a subsystem. Defines a higher-level interface that makes the subsystem easier to use. (`PyFacadePattern.py`)
- **Bridge**: Decouples an abstraction from its implementation so that the two can vary independently. (`PyBridgePattern.py`)
- **Decorator**: Attaches additional responsibilities to an object dynamically. Provides a flexible alternative to subclassing for extending functionality. (`PyDecoratorPattern.py`)
- **Private Class Data**: Restricts accessor/mutator access and provides more control over the data. (`PyPrivateClassDataPattern.py`)

### Behavioral Patterns

Behavioral patterns are design patterns that identify common communication patterns between objects and realize these patterns.

- **Observer**: Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically. (`PyObserverPattern.py`)
- **Strategy**: Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Lets the algorithm vary independently from clients that use it. (`PyStrategyPattern.py`)
- **Command**: Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations. (`PyCommandPattern.py`)
- **Chain of Responsibility**: Lets more than one object handle a request without coupling the sender class to the concrete classes of the receivers. The request is passed along a chain of handlers. (`PyChainOfResponsibilityPattern.py`)
- **State**: Allows an object to alter its behavior when its internal state changes. The object will appear to change its class. (`PyStatePattern.py`)
- **Visitor**: Represents an operation to be performed on elements of an object structure. Lets you define a new operation without changing the classes of the elements on which it operates. (`PyVisitorPattern.py`)
- **Interpreter**: Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language. (`PyInterpreterPattern.py`)
- **Iterator**: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. (`PyIteratorPattern.py`)
- **Mediator**: Defines an object that encapsulates how a set of objects interact. Promotes loose coupling by keeping objects from referring to each other explicitly. (`PyMediatorPattern.py`)
- **Memento**: Without violating encapsulation, captures and externalizes an object's internal state so that the object can be restored to this state later. (`PyMementoPattern.py`)
- **Template Method**: Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure. (`PyTemplatePattern.py`)
- **Null Object**: Provides an object as a surrogate for the absence of an object and implements default behavior to avoid null references. (`PyNullObjectPattern.py`)
- **Specification**: Combines business rules to be recombined by chaining the rules together using boolean logic. (`PySpecificationPattern.py`)

### Concurrency Patterns

Concurrency patterns are design patterns that deal with multi-threaded programming paradigms.

- **Active Object**: Decouples method execution from method invocation to enhance concurrency. (`PyActiveObjectPattern.py`)
- **Reactor**: Handles service requests that are delivered concurrently to an application by one or more clients. (`PyReactorPattern.py`)
- **Half-Sync/Half-Async**: Separates synchronous and asynchronous processing to simplify complex systems. (`PyHalfSyncOrHalfAsyncPattern.py`)
- **Leader-Follower**: Reduces contention and context switching in processing multiple event sources. (`PyLeaderOrFollowerPattern.py`)
- **Thread Pool**: Manages a pool of worker threads to perform tasks concurrently. (`PyThreadPoolPattern.py`)

### Architectural Patterns

Architectural patterns are design patterns that help to define the overall structure of a software system.

- **Model-View-Controller (MVC)**: Separates the application into three interconnected components. (`PyModelViewControllerPattern.py`)
- **Model-View-ViewModel (MVVM)**: A variation of MVC, specifically for use with data-binding. (`PyModelViewViewModelPattern.py`)
- **Microservices**: Structures an application as a collection of loosely coupled, independently deployable services. (`PyMicroservicesPattern.py`)
- **Service-Oriented Architecture (SOA)**: Design principles used to define the integration of services across different systems. (`PyServiceOrientedArchitecturePattern.py`)


## 🧪 Testing

All implementations come with corresponding test files located in the `tests` directory, ensuring reliability and correctness.

To run tests, use:
```bash
python -m unittest discover tests/DesignPatterns
```