# What are "Reactive Systems"?

Are "Systems" that react to changes in the environment nearly real-time. In other terms are very responsive systems. Has similarity with real-time processing and stream processing.

You recieved a message and react to it.

## Features

- **Responsive**: The system responds in a timely manner to requests(Changes in the environment).
- **Resilient**: Tolerant to **failure**.
- **Elastic**:   Stay responsive under varying workload.
- **Message Driven**:  The components mus tuse asynchonous message-driven to stablish a boundary and ensure loose coupling.

### Message Driven

A message is an item of data that is sent to a specific destination. An event is a signal emitted by a component upon reaching a given state. In a message-driven system addressable recipients await the arrival of messages and react to them, otherwise lying dormant. In an event-driven system notification listeners are attached to the sources of events such that they are invoked when the event is emitted. This means that an event-driven system focuses on addressable event sources while a message-driven system concentrates on addressable recipients. A message can contain an encoded event as its payload.

Resilience is more difficult to achieve in an event-driven system due to the short-lived nature of event consumption chains: when processing is set in motion and listeners are attached in order to react to and transform the result, these listeners typically handle success or failure directly and in the sense of reporting back to the original client. Responding to the failure of a component in order to restore its proper function, on the other hand, requires a treatment of these failures that is not tied to ephemeral client requests, but that responds to the overall component health state.


## Actor Model Vs Reactor Model

[Can I still write my traditional actor programs?](http://reactors.io/faq/)

[Actor Model](https://en.wikipedia.org/wiki/Actor_model)

[ACTORS: A Model of Concurrent Computation in Distributed Systems](https://dspace.mit.edu/handle/1721.1/6952)

[Reactors: A Case for Predictable, Virtualized Actor Database Systems](https://arxiv.org/pdf/1701.05397.pdf)

The Reactor Model is a generalization of the actor model.

Reactors are software components that borrow concepts from actors, dataflow
models, synchronous-reactive models, discrete event systems, object-oriented
programming, and reactive programming.

## Tools for Building Java Applications

- [Eclipse Vertx. Reactive applications on the JVM](https://vertx.io/)
- [Akka Build powerful reactive, concurrent, and distributed applications more easily](https://akka.io/)
  - [Akka HTTP](https://doc.akka.io/docs/akka-http/current/index.html?language=java)
  - [Akka Streams](https://doc.akka.io/docs/akka/current/stream/index.html?language=java)
  - [Akka Actors](https://doc.akka.io/docs/akka/current/typed/index.html)


## Formal Model

## Resources

[Reactors: A Deterministic Model for Composable Reactive Systems](https://people.eecs.berkeley.edu/~marten/pdf/Lohstroh_etAl_CyPhy19.pdf)

A formal representation is given in https://web.stanford.edu/class/cs256/slides/l01_win09-2x1.pdf

[Dataflow](https://en.wikipedia.org/wiki/Dataflow)
