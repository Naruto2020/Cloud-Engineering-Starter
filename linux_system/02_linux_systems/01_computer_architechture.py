
========================================================================

		BLOC 2 — Systems
		Lesson 2.1: Computer Architecture

========================================================================


Part 2 — CPU architecture and execution


We have already covered the basic roles of the CPU, RAM and storage. 
Now let's understand how the CPU actually executes programs.


1. What is a CPU?


The Central Processing Unit (CPU) is the component responsible for
executing instructions.

For example, when your Node.js application executes:


The CPU performs the underlying operations required to calculate the result.

At a simplified level, CPU execution follows three steps:


1 Fetch
Retrieve the next instruction from memory.


2 Decode
Determine what the instruction means and what operation is required.


This is a simplified representation. Modern CPUs use pipelines, caches 
and other optimizations to execute instructions efficiently.



3
Execute Perform the operation, such as arithmetic, comparison or data 
movement. const total = price * quantity;


For example:

Example: 1 physical CPU

Physical CPU

Core 1
Hardware thread 1

Hardware thread 2



Core 2
Hardware thread 3

Hardware thread 4

Illustrative example: 2 physical cores exposing 4 logical CPUs.


An important distinction:
- Hardware threads are provided by the processor.
- Software threads are created and managed by applications and the 
operating system.

They are related, but they are not the same thing.


3. Processes vs software threads

When you launch a program, the operating system creates a process.

A process is a running instance of a program with its own virtual 
memory space and resources.

For example, your Node.js backend running on Linux is a process.


A process can contain several software threads.

A thread is an execution path inside a process.


Why have multiple threads?

Imagine a backend that needs to:
- Process incoming requests.
- Perform calculations.
- Read files.
- Communicate with databases.
Multiple threads can allow several operations to make progress 
independently.


One important Node.js detail: Node.js normally executes JavaScript 
callbacks on a single main event-loop thread. It can still handle many 
concurrent I/O operations, and it also uses worker threads and a 
background thread pool for certain tasks.


4. How does the operating system manage CPU execution?

The operating system has a component called the CPU scheduler.

Its responsibility is to decide which runnable software thread gets 
CPU time.


Consider a computer with one CPU core and three runnable threads:
- Thread A: application backend.
- Thread B: database.
- Thread C: system service.

The scheduler allocates CPU time between them.

This is called CPU scheduling.


Time slice: A period during which a thread is allowed to execute before 
the scheduler may give another thread CPU time.


Preemption: The operating system can interrupt a running thread and 
schedule another runnable thread.


The scheduler does not necessarily use a simple round-robin strategy. 
Modern Linux uses more sophisticated scheduling mechanisms.


5. Context switching
How does the CPU switch from one thread to another?

It uses a mechanism called a context switch.

A context represents the execution state of a thread, including 
information such as:

- CPU registers.
- Program counter (where execution should continue).
- Stack pointer.
- Other scheduling and processor state.
A simplified context switch looks like this:


Thread A is executing

	|

Save Thread A's execution state

	|

Scheduler selects Thread B

	|

Restore Thread B's execution state

	|

Thread B continues executing


Context switching has a cost: saving and restoring execution state
consumes CPU resources.


This is why excessive context switching can hurt performance.


6. Concurrency vs parallelism
These concepts are particularly important in backend and cloud 
engineering.


Concurrency: Multiple tasks make progress over overlapping periods, even 
if they do not execute simultaneously.

Parallelism: Multiple tasks execute at exactly the same time on separate 
processing units.


Concurrency
One CPU core
Task A

Task B

Task C

Tasks take turns executing.


Parallelism
Multiple cores
Core 1 — Task A

Core 2 — Task B

Core 3 — Task C

Tasks execute simultaneously.


This distinction explains why a server can handle many simultaneous
network requests without necessarily needing one CPU core per request.


7. What happens when the CPU is overloaded?



Imagine your EC2 instance has two logical CPUs, but hundreds of computationally intensive threads are ready to execute.

The scheduler cannot execute all of them simultaneously.

They must wait for CPU time.


This can lead to:

Symptom				Explanation
High CPU utilization	Available CPU capacity is heavily used
Increased latency	Tasks wait longer before execution
Reduced responsiveness	Applications take longer to process requests
Growing runnable queue	More threads are waiting for CPU time
Context-switch overhead	Frequent switching consumes resources


One useful Linux metric is load average.

It represents the average number of tasks that are runnable or waiting in
certain uninterruptible states over 1, 5 and 15 minutes. It is not simply
CPU utilization.

For example, on a machine with 2 logical CPUs, a sustained load average 
significantly above 2 can indicate that work is accumulating, although 
I/O waits and workload characteristics also matter.


8. Connecting this to AWS EC2

When you launch an EC2 instance, you select an instance type that 
determines its available compute resources.

For example, an instance with 2 vCPUs exposes two logical CPU execution 
units to the operating system.

A vCPU is a virtual CPU presented to your instance. Depending on the 
underlying processor and instance family, it generally corresponds to a 
hardware thread, not necessarily an entire physical core.


This matters when:
- Choosing an EC2 instance size.
- Deploying Node.js applications.
- Configuring worker processes.
- Troubleshooting high CPU usage.
- Deciding whether to scale vertically (bigger instance) or horizontally
 (more instances).

=========================================================================

		Section 2.1 — Final exercises

=========================================================================


		Exercise 1 — CPU, cores and hardware threads


An EC2 instance has 4 vCPUs.

Explain:
- What is a vCPU?
- Does 4 vCPUs necessarily mean 4 physical CPU cores?
- What is the difference between a CPU core and a hardware thread?

==> - A vCPU is a virtual CPU used on cloud corresponding to an real 
hardware CPU

    - No 4 vCPUs not necessarily mean 4 physical CPU cores there is also
threads

    - ??
==> correction : 

- A vCPU is a virtual processing unit exposed to a virtual machine by the
 cloud provider.

- ok

- CPU core is a physical processing unit use to execute instructions
while hardware thread is a logical execution context using one physical
core to manage multiple instructions.


		Exercise 2 — Processes vs Threads


Imagine an EC2 instance running a Node.js application.

The application starts as a process, and internally it can use multiple 
threads.

Question: What is the difference between a process and a thread? In 
particular, what resources do threads within the same process share, and 
what does each thread have independently?

Answer in your own words.

==> The difference between a process and a thred is that a process is a 
running instance of a programe and a thread is use to manage that 
process. Thhe threads and process share  vCPU core

====> Correction 

1. Process vs thread
Your definition:
A process is a running instance of a program.

Correct
But a thread doesn't simply manage a process. A thread is an execution 
path inside a process. It executes instructions belonging to that process.

Think of it this way:
- Process = the application and its execution environment.
- Thread = a worker executing instructions within that application.


2. What do they share?
The process and its threads don't share a vCPU as a resource.

Threads belonging to the same process share:
- Memory (especially the heap).
- Open files and network connections.
- Other process resources.

Each thread has its own:
- Stack.
- CPU registers.
- Program counter.

Exercise 2 — Final attempt
A Node.js process has three threads.

Complete these two statements in your own words:

1. The three threads share Memory, Open files and network connections
and other process resources.

2. Each thread has its own Stack , CPU register and program counter.



Exercise 3 — CPU Scheduling
The concept
A computer may have many runnable threads but only a limited number of CPU cores.

The CPU scheduler is the operating system component responsible for deciding which runnable thread gets CPU time and when.

For example, imagine:
- Your EC2 instance has 2 vCPUs.
- Your application has 5 runnable threads.
Only two threads can execute simultaneously on those two logical CPUs. The scheduler decides which threads run and switches between them.

Two important concepts:
- Runnable: A thread is ready to execute but may be waiting for CPU time.
- Blocked: A thread cannot continue until an event occurs, such as a network response or disk operation.

Your exercise:

An EC2 instance has 2 vCPUs and 6 runnable threads.

1. Can all 6 threads execute simultaneously?

2. What does the CPU scheduler do with the threads that cannot execute immediately?
Answer in your own words.

==> No all 6 threads cannot execute simultaneously because EC2 instance 
has only 2 vCPUs 

==> The CPU scheduler will ll not give time to thoses threads
execute instructions.


Exercise 4 — Context Switching

The concept
A context switch happens when the operating system stops executing one 
thread and starts executing another.

Before switching, the OS saves the current thread's execution state, 
including:

- CPU registers.
- Program counter.
- Stack pointer.

It then restores the saved state of the next thread so execution can 
resume where it left off.

This operation has a cost: during the switch, the CPU spends time 
managing execution state rather than executing application instructions.

Your exercise:

An EC2 instance has 2 vCPUs and 6 runnable threads.

Why does the operating system need context switching in this situation, 
and what information must it save before switching from one thread to 
another?


===> The OS need context switching to help it manage multiples threads
depending on time they have to execute their task. in our situation with 
6 runnable threads, the context switching help OS to starts and stop 
each threads

Before switching from one thread to anoyher, the OS must save current 
thread's execution state including : Stack , CPU register and program 
counter


Exercise 5 — Concurrency vs Parallelism
The concept
These two concepts are related but different.

Concurrency means multiple tasks make progress during overlapping 
periods. They don't necessarily execute at exactly the same time.

Parallelism means multiple tasks execute at exactly the same time, using 
separate processing resources.

For example:
- One CPU core switching between two tasks: concurrency.
- Two CPU cores executing two tasks simultaneously: parallelism.
Your exercise:

An EC2 instance has 1 vCPU and runs two application threads.

Can these two threads execute concurrently? Can they execute in parallel?


==> these 2 threads ll execute concurrently because of 1 vCPUs


Exercise 6 — Real-world CPU troubleshooting

Imagine your Node.js application runs on an EC2 instance with 2 vCPUs.

You observe:

- CPU utilization: 95%.
- Application response times are increasing.
- Several threads are waiting for CPU time.

Question: What do these symptoms suggest about your application, and 
what could happen if the situation continues?

Use the concepts we've covered: CPU scheduling, runnable threads and 
context switching.


==> These symptoms suggest that my application is consumming too much 
vCPU . That slow my application 


===> Correction 

- 95% CPU utilization: The two vCPUs are almost fully occupied.
- Runnable threads waiting: Threads are competing for CPU time.
- Increasing response times: Application tasks take longer because they cannot get CPU time immediately.
- Context switching: The scheduler switches between runnable threads, but excessive switching can add overhead.

2. What could happen if the situation continues?
- Application latency may continue increasing.
- Requests may accumulate faster than the application processes them.
- Requests may time out.
- The application may become unresponsive.

3. What could you do?

Two possible approaches:

- Vertical scaling: Move to an EC2 instance with more vCPUs.
- Horizontal scaling: Run additional application instances and distribute
requests between them.
You should also investigate whether the application has CPU-intensive 
operations that could be optimized.

