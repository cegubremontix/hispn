# Give a Resume "Software Design for Flexibility"

This book is a master class on the design of flexible and adaptable software systems.

This book is a master class in specific program organization strategies that mnaintain flexibilty.

## Goals

It's hard to build systems that have acceptable behavior over a large class of situations than was anticipated by their designers. The best systems are evolvable: they can be adapted to new situations with only minor modification.

Design Evolvable/Adaptable Systems.

Explore Addictive Programming: Our goal in this book is to investigate how to construct **computational systems** so that they can be easily adapted to changing requirements. One should not have to midify a workig program. One should be able to add to it to implement new functionality or to ajust old functions for new requirements.

Explore the evaluator as a common building block "for engineering system". An evaluator takes a description of some computation to be performed, and some inputs. It produces the outputs or deseriable behavior.


## Fundamentals Ideas in Building Adaptable and Evolvable Systems

**Generic dispatch**, Is a way to extend the aplicability of a procedure by adding additional handlers (methods) based on the detail of the arguments pass to the procedure. By requireing the handlers to disjoint sets of arguments, we can avoid breaking an existing program when a new handler is added. We explore **Generic dispatch** in a global context without **object orientation**.

**Layers**, Is the idea to annotate procedure and data with **metadata**  that can be process alongside with the data, and  procedures respectively. As an example one can annotate numeric data with `units metadata`. We will explore how to add new functionality processing this `metadata`.

**Redundancy**,  Having more capacity to the job then really need it. Having multple ways to do the same thing.

**Degeneracy**,  Having multiple ways to compute something, which can be combined or modulated as needed. There are many valuables uses for degeneracy, including error detection, performace management, and instruction detection. 

**Exploratory Behavior**, The idea that the desired outcome is prouded by a generate-and-test mechanism. In generate-and-test mechanism the **generate componente** generate actions that are test by the **test mechanism**. That accepts/reject the proposal.

## Concrete Techniques

**Domain-Specific Languages**: Provide an abstraction in which the nouns and verbs of the language are directly related to the problem domain.

**Generic Procedures**, Is a way to extend the aplicability of a procedure by adding additional handlers (methods) based on the detail of the arguments pass to the procedure. By requireing the handlers to disjoint sets of arguments, we can avoid breaking an existing program when a new handler is added. We explore **Generic dispatch** in a global context without **object orientation**. 

**Layering**, Is the idea to annotate procedure and data with **metadata**  that can be process alongside with the data, and  procedures respectively. As an example one can annotate numeric data with `units metadata`. We will explore how to add new functionality processing this `metadata`.

**Propagator**, Is a **Model of Computation** in which the basic computational elements are **propagators**, autonomous independent machines interconnected  by shared cells through which they communicate. Each propagator machine contiuously examines the cells it is connected to, and adds information to some cells based on computations it can make from information it  can get from others cells.
- Cells accumulate information and propagators produce information.
