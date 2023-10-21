# Systems Performace

> **System performace** is the study of the entire sysetm (software stack + hardware stack) / Anything in the **data path**.

> **Data Path** is the physical and logical component of a computer system responsible for executing instructions and performing data manipulation tasks.

> **Systems performance engineering** is a challenging field for a number of reasons, includ- ing the fact that it is subjective, it is complex, and it often involves multiple issues.

> It is a **capital mistake** to theorize before one has data. Insensibly one begins to twist facts to suit theories, instead of theories to suit facts. Sherlock Holmes in “A Scandal in Bohemia” by Sir Arthur Conan Doyle

> The performance of the system under increasing load is its **scalability**.

> **System performance monitoring** records performance statistics over time (a time series), so that the past can be compared to the present and time-based usage pat-terns can be identified. This is useful for capacity planning, quantifying growth, and showing peak usage. Historic values can also provide context for understand- ing the current value of performance metrics, by showing what the “normal” range and average have been in the past.

## Activities

1. Setting performance objectives and performance modeling
2. Performance characterization of prototype software or hardware
3. Performance analysis of development code, pre-integration
4. Performing non-regression testing of software builds, pre- or post-release
5. Benchmarking/benchmarketing for software releases
6. Proof-of-concept testing in the target environment
7. Configuration optimization for production deployment
8. Monitoring of running production software
9. Performance analysis of issues

## Perspectives

![Analysis perspectives](https://i.imgur.com/5f1qnjO.png)

**Resource Analysis**

Resource analysis begins with analysis of the system resources: CPUs, memory, disks, network interfaces, busses, and interconnects.

Some Metrics:
- IOPS
- Throughput
- Utilization
- Saturation

**Workload Analysis**

Workload Analysis examines the performce  of the application.

![Workload Analysis](https://i.imgur.com/E82Zam5.png)

The targets for workload analysis are:
- **Requests**: the workload applied
- **Latency**: the response time of the application
- **Completion**: looking for errors

## Analytical Modeling

> **Analytical modeling** of a system can be used for various purposes, in particular scalability analysis: studying how performance scales as load or resources scale. Resources may be hardware, such as CPU cores, or software, such as processes or threads.

![scalability](https://i.imgur.com/yAIspW8.png)

**...**

## System Models

> The **system under test** refers to the specific software, hardware, or combination thereof that is being evaluated, tested, or analyzed in a given context or experiment.

![sut](https://i.imgur.com/o48XeP1.png)

Templates:

- System Under Test (SUT)
- Queueing Modele

## Systems

|Layer|Tuning Targets|
|---|--|
Layer|Tuning Targets
Application| database queries performed
Database| database table layout, indexes, buffering
System calls| memory-mapped or read/write, sync or async I/O flags
File system| record size, cache size, file system tunables
Storage| RAID level, number and type of disks, storage tunables

## Metrics

- **Response time**: the time for an operation to complete. This includes any
time spent waiting and time spent being serviced (service time), including the
time to transfer the result.
- **IOPS**: Input/output operations per second is a measure of the rate of data
transfer operations. For disk I/O, IOPS refers to reads and writes per second.
- **Latency**: Latency is a measure of time an operation spends waiting to be
serviced. In some contexts, it can refer to the entire time for an operation,
equivalent to response time. See Section 2.3, Concepts, for examples.
- **Throughput**: the rate of work performed. Especially in communications, the
term is used to refer to the data rate (bytes per second or bits per second). In
some contexts (e.g., databases), throughput can refer to the operation rate
(operations per second or transactions per second).
Ut**ilization**: For resources that service requests, utilization is a measure of
how busy a resource is, based on how much time in a given interval it was
actively performing work. For resources that provide storage, utilization may
refer to the capacity that is consumed (e.g., memory utilization).
- **Saturation**: the degree to which a resource has queued work it cannot
service.
- **Bottleneck**: In system performance, a bottleneck is a resource that limits the
performance of the system. Identifying and removing systemic bottlenecks is
a key activity of systems performance.
- **Workload**: The input to the system or the load applied is the workload. For a
database, the workload consists of the database queries and commands sent
by the clients. 

## Techniques

- Dynamic Tracing
- Profiling

## Methodologies

> **Analysis** tools.

|Methodology|Type|
|---|---|
Streetlight|anti-method observational analysis
Random change anti-method| experimental analysis
Blame-someone-else anti-method| hypothetical analysis
Ad hoc checklist method| observational and experimental analysis
Problem statement| information gathering
Scientific method| observational analysis
Diagnosis cycle| analysis life cycle
Tools method| observational analysis
USE method| observational analysis
Workload characterization| observational analysis, capacity planning
Drill-down analysis| observational analysis
Latency analysis| observational analysis
Method R| observational analysis
Event tracing| observational analysis
Baseline statistics| observational analysis
Performance monitoring| observational analysis, capacity planning
Queueing theory| statistical analysis, capacity planning
Static performance tuning| observational analysis, capacity planning
Cache tuning| observational analysis, tuning
Micro-benchmarking| experimental analysis
Capacity planning| capacity planning, tuning

## Workload Characterization

> **Workload characterization** is a simple and effective method for identifying a class of issues: those due to the load applied.

Workloads can be characterized by answering the following questions:
- **Who** is causing the load? Process ID, user ID, remote IP address?
- **Why** is the load being called? Code path, stack trace?
- **What** are the load characteristics? IOPS, throughput, direction (read/write),
type? Include variance (standard deviation) where appropriate.
- **How** is the load changing over time? Is there a daily pattern?

**...**