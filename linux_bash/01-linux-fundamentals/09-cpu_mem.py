
===================================================================

	Step 5.14 — CPU, Memory & System Load

===================================================================


Now we move from process-level troubleshooting to system-level 
troubleshooting.

So far, you learned how to identify a process consuming too much CPU:

top
 ↓
python → 98% CPU

But we also need to know whether the whole server is under pressure.


1. free — Check memory

Run:

free -h

The -h means human-readable.

Example:

               total   used   free   shared   buff/cache   available
Mem:             8Gi    6Gi    500Mi    ...       1.5Gi        2Gi
Swap:            2Gi    200Mi   1.8Gi

The most important column for many troubleshooting situations is:

available

It gives an estimate of how much memory is available for new applications
without swapping.

Why this matters


Suppose:

Mem:   8Gi total
       7.8Gi used
       100Mi available

The server may be experiencing memory pressure.


2. uptime — Load and system uptime

Run:

uptime

Example:

10:30:12 up 5 days, 3:21, 2 users, load average: 2.50, 1.80, 1.20

The important part is:

load average: 2.50, 1.80, 1.20

These represent approximately:

2.50 → last 1 minute
1.80 → last 5 minutes
1.20 → last 15 minutes

Load average tells you how much work is running or waiting 
for CPU/resources.

⚠️ Don't interpret 2.50 as automatically meaning "250% CPU." You n
need to consider the number of CPU cores.


3. lscpu — CPU information

Run:

lscpu

This gives information about the CPU, including:

CPU(s):                4
Model name:            ...
Architecture:          x86_64

The important number for our current discussion is:

CPU(s): 4

That tells us the system has 4 logical CPUs.


🧠 Cloud troubleshooting example

Imagine a server has:

4 CPUs
8 GB RAM

and:

uptime
→ load average: 8.0, 7.5, 6.9

A load of 8.0 on a 4-CPU system is potentially significant because there
is more runnable/waiting work than the CPUs can handle immediately.

But if the same load were on a machine with 16 CPUs, the interpretation 
would be very different.

So always consider:

Load average
      +
Number of CPUs
      +
CPU usage
      +
Memory availability



🧪 Exercise 13


Suppose your server has:

CPU(s): 4

and:

uptime
→ load average: 0.50, 0.40, 0.30

Answer:

1. What do the three numbers 0.50, 0.40, 0.30 represent?

==> The three number represent load average. The numbers of works process
waiting to run on last minutes

2. Which number represents the last 1 minute?

==> 0.50

3. Is a load average of 0.50 generally concerning on a 4-CPU system? Why?

==> No because load average of 0.50 < 4 logical cpu

4. Which command would you use to find out how many CPUs the server has?

==> lscpu

=====================================================================

	5.15 — free -h: Memory Troubleshooting

=====================================================================

Let's now focus specifically on RAM.

Run:

free -h

You might see:

               total   used   free   shared   buff/cache   available
Mem:            7.7Gi   3.1Gi  1.2Gi    ...       3.4Gi       4.2Gi
Swap:           2.0Gi   0B     2.0Gi

The important concepts are:

total → total RAM
used → memory currently used
free → completely unused memory
buff/cache → memory used for buffers and filesystem cache
available → estimated memory available for applications
Important Cloud/DevOps point

Don't look only at free.

Linux intentionally uses available RAM for caching, so seeing:

free = 200 MB

does not necessarily mean the server is running out of memory.

Instead, pay close attention to:

available


🧪 Exercise 14

Suppose free -h shows:

               total   used   free   buff/cache   available
Mem:            8Gi     6Gi    200Mi    1.8Gi        1.5Gi
Swap:           2Gi     1.2Gi  800Mi

Answer:

1. How much total RAM does the server have?

==> total RAM 8Gi

2. How much memory is currently available for applications?

==> 1,5Gi


3. Is free = 200Mi by itself enough to conclude that the server is
completely out of memory?

==> No because sometime part of memory is use for cache is good to 
check also available= 1.5Gi


4. What does significant swap usage potentially tell you about the server?

==> Significant swap potentially tell that a server it is maybe 
memory presure or server is too slow


