# Give a Resume "Concepts, Techniques, and Models of Computer Programming"

## Lets start by disecting

**Concept**: Is a mental representation of some elements that may/not exists in reality.

**Technique**: A way of carrying out a particular task.

**Computation Model**:  Formal System that models a  **Computer Device**, what language it accepts, and how the sentences of the language are executed.
- What is the meaning of every sentence, what is their effect.

**Programming Model**: A set of techniques and design principles used to write programs in the language of the **computation model**. A **Programming model** is always build on top of a **computation model**.
- Abstractions, Concepts, Techniques, Design Principles to build programs to describe comptuations in a given "Computation Model".
- A program model helps in the organization of computations, by a given "Computation Model".

**Program**: A description of a computation that will be perform by a "computer device". Created using a "Model of Programming".
- General Computer Device + Program = Specific Computer Device (Useful)

**Computation**:
- Execution of a program by a computer device, 
- The process of solving problem,
- The process of doing a task,
- Execute SQL Queries (Declarative).

 ![Problem, Programer, Model of Programming, Program, Model of Computation, Device, Computation, Computation Result](https://gitlab.com/dbremont/resources/-/raw/main/images/models.jpg)


**What is a resonable computation model?**:
Is a model that can be used to solve many problems, that has straighforward an practical reasoning techniques, and that can be implemeneted efficiently. 

|Model of Computation|Programming Model|
|--|---|
|Declarative Model (ch 2 & 3, Mercury , Prolog)||
|Stateful Model (ch 6 & 7, Scheme, Pasca)|
|Lazy declarative model (Haskell)|
|Lazy stateful model|
|Eager concurrent model (ch 4, dataflow)|
|Stateful concurrent model (ch 5 & 8, Erlang, Java)|
|Lazy concurrent model (ch 4, demand-driven dataflow)| 
|Steful concurent model with laziness (Oz)|






###  Concepts

 Is a mental representation of some elements that may/not exists in reality

 ![Concept](https://upload.wikimedia.org/wikipedia/commons/f/fd/Generalization_process_using_trees.svg)

Examples:

- concurrency,
- exceptions,
- lazy execution,
- security,
- explicit state,
- and nondeterministic choice,
- Sequential, concurrent, and distributed abstractions,
- abstract vs concrete,
- Locks, reentrant locks, monitors and transactions,
- Active objects,
- Active objects with mailboxes,
- Coroutines (non-preemtive threads),
- Loops abstraction like the **foor loop**,
- Stream objects and declarative concurrency,
- Ports (communication channels) and port objects



###  Techniques

A way of carrying out a particular task.

**Declarative Model of Comptuation**

- Recursion
- Higher-Order Programming
- Object Oriented Programming Techniques

###  Models of Computer Programming 
A Model of Computation ("A Model of Programming"), provides a set of tools that help to describe/organize computations that will be be done in a "abstract machine". 

![Programming Paradigms](https://miro.medium.com/max/1200/1*wS8DsmEejvsswkQjNA-BoQ.png)

### How to practice

- Haskell for lazy functional programming
- Erlang: for message-passing concurrency
- Sql for transactioal programing
- Esterel for synchonous programing
- oz for declarative concurrency adn constraint programming
