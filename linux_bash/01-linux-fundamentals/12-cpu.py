
=========================================================================

		Step 6 — CPU / RAM / Disk

=========================================================================


Step 5 is complete. Now we move into resource monitoring and performance analysis.

The goal is not just to know commands like top or free, but to answer:

"Why is this server slow?"

We'll work through CPU, RAM, and disk systematically.


6.1 CPU: utilization vs load

There are two concepts you need to keep separate.

CPU utilization

From top:

%Cpu(s):  85.0 us, 5.0 sy, 0.0 ni, 10.0 id

Here:

us = user-space CPU usage
sy = kernel/system CPU usage
id = idle CPU

So approximately:

85% + 5% = 90% CPU busy
10% idle


Load average

From:

uptime

you might see:

load average: 3.20, 2.10, 1.50

These represent:

3.20 → last 1 minute
2.10 → last 5 minutes
1.50 → last 15 minutes

Load is not a percentage.

Its meaning depends partly on how many CPU cores the machine has.

For example:

4 CPUs
load average = 1.0

is very different from:

1 CPU
load average = 1.0


What is load average?

When you run:

uptime

you might see:

14:30:10 up 5 days,  3:21,  2 users,  load average: 2.40, 1.80, 1.20

The last three numbers are the load average:

2.40   1.80   1.20
 │       │      │
 │       │      └── last 15 minutes
 │       └───────── last 5 minutes
 └───────────────── last 1 minute

But what does 2.40 actually mean?

Load = work that is waiting to run

Very roughly, Linux's load represents the amount of work that is:

running on the CPU, or
ready/waiting for CPU, and also certain tasks waiting on uninterruptible 
I/O.

So imagine a restaurant.

CPU cores = cooks
processes = orders

If you have 4 cooks:

4 cooks
4 orders being handled
0 orders waiting

The system has enough CPU capacity.

But:

4 cooks
4 orders being handled
3 orders waiting

there is more work than the cooks can handle immediately.

That's the intuition behind a load above the number of CPUs.

Why does the number of CPUs matter?

Suppose:

Server A → 1 CPU
load = 1.0

There is roughly one CPU's worth of work.

Now:

Server B → 4 CPUs
load = 1.0

There is still roughly one CPU's worth of work, but you have four CPUs 
available.

So these are very different situations.

4-CPU server

Load	Rough interpretation

0.5	Very light
1.0	About 25% of 4 CPUs' capacity
2.0	About half of total CPU capacity
4.0	Around full CPU capacity
5.0	More work than the CPUs can handle immediately
8.0	Significant pressure

These aren't strict CPU percentages because load isn't simply CPU 
utilization.


Load average ≠ CPU percentage

This is the part I should have explained earlier.

Suppose:

4 CPUs
load average: 5.20

You cannot say:

"The CPU is at 520%."

That's wrong.

You need to look at CPU utilization separately:

top

For example:

load average: 5.20
CPU idle: 2%

That combination strongly suggests CPU pressure.

But imagine:

load average: 5.20
CPU idle: 70%

Now we need to investigate further. Some of the load may be related to 
processes waiting on I/O rather than simply CPU computation.

That's why a Cloud Engineer doesn't diagnose a server from one number.


Why three load averages?

Linux gives you:

1 minute    5 minutes    15 minutes
   ↓            ↓            ↓
  5.2          4.8          3.1

This gives you a sense of the trend.

For example:

load average: 5.2, 4.8, 3.1

means the recent load is increasing.

Whereas:

load average: 1.2, 2.5, 4.0

means the load was higher in the past and is currently decreasing.

So load averages help you see both current pressure and recent history.

What should you actually do as a Cloud Engineer?

Don't memorize:

"load > 4 = bad."

Instead, use this reasoning:

uptime
   ↓
What is the load?
   ↓
How many CPUs do I have?
   ↓
Compare load to CPU capacity
   ↓
Check actual CPU utilization with top
   ↓
If CPU isn't explaining the load
   ↓
Investigate I/O / processes / other resources

For example:

uptime
lscpu
top

Together, these commands tell you much more than uptime alone.


===================================================================


Exercise 1

A server has 4 logical CPUs.

You run:

uptime

and get:

load average: 5.20, 4.80, 3.10

Answer:

What is the 1-minute load?
What is the 5-minute load?
What is the 15-minute load?
The server has 4 CPUs. Is a 1-minute load of 5.20 something you should 
investigate?
Is 5.20 equivalent to 520% CPU usage?

Your turn.

1- the 1-minute load is 5.20
2- the 5-minute load is 4.80
3- the 15-minute load is 3.10
4- 4 CPUs + load 5.20: I should investigate.
5- No 

=======================================================================

Exercise 18

A server has 4 logical CPUs.

You run:

uptime
load average: 1.2, 1.0, 0.8

And:

top
%Cpu(s): 20.0 us, 5.0 sy, 0.0 ni, 75.0 id

Answer:

What is the current (1-minute) load?
How many CPUs does the server have?
Is the load currently higher than the number of CPUs?
Is the CPU heavily utilized?
Based on these two outputs, does the server appear to have a serious 
CPU problem?
What does 75.0 id mean?

1- the current 1-minute load is 1.2
2- the server have 4 logical CPUs
3- No the load isn't currently higher than the number of CPUs
4- No
5- No the server don't have a serious CPU problem
6- 75% of CPU time is idle.


Key concept to keep

You now have the correct mental model:

             uptime
                ↓
          Load average
                ↓
      Compare with CPU count
                ↓
              + 
               ↓
              top
                ↓
       CPU utilization/idle
                ↓
       Diagnose CPU pressure

And remember:

Load average is a measure of system work/pressure, not a CPU percentage.


=======================================================================

		6.2 — Finding the CPU culprit

=======================================================================


6.2 — Finding the CPU culprit

Now that you understand what CPU pressure means, the next question is:

Which process is causing it?

You already learned ps, top, and pgrep in Step 5. Here we'll use them 
together for diagnosis.


For example:

ps aux --sort=-%cpu | head

might show:

USER   PID   %CPU   %MEM   COMMAND
steve  4521  91.5   8.2    python app.py
mysql  2100   4.2  18.5    mysqld
root   1200   1.0   1.1    systemd

Now we can move from:

"The server has CPU pressure."

to:

"Python process 4521 is consuming most of the CPU."

That distinction is critical in production troubleshooting.

Next exercise

I'll give you a realistic top output and you'll identify whether the 
problem is CPU capacity or a single runaway process.


6.2 — Finding the CPU Culprit

Let's apply the concept.

A server has 4 logical CPUs.

You run:

uptime

and get:

load average: 5.8, 4.9, 2.7

Then you run:

ps aux --sort=-%cpu | head

and get:

USER      PID   %CPU   %MEM   COMMAND
steve    4521  385.0    8.2   python app.py
mysql    2100    5.5   20.1   mysqld
root     1200    1.2    1.0   systemd
nginx    1300    0.8    2.0   nginx
Important detail

You have 4 logical CPUs, so a single process can potentially use more 
than 100% CPU.

For example:

100% ≈ one logical CPU fully utilized
200% ≈ two logical CPUs
400% ≈ four logical CPUs

So:

python → 385% CPU

means this Python process is consuming roughly 3.85 logical CPUs worth 
of CPU capacity.

Exercise 19

Answer these:

Is the server experiencing significant CPU pressure? Why?
Which process is the main CPU consumer?
What is its PID?
Approximately how many logical CPUs is the Python process consuming?
Is 385% CPU a mistake? Explain.
If you wanted to investigate this process further, which command would 
you use to observe it in real time?

1- yes the server have a significant CPU pressure. Because, the server
has 4 logical CPUs  and 1-minute load is 5.8 and python app cpu usage 
is 385% that mean 3.85 on 4 logical CPU

2-  4521  385.0    8.2   python app.py

3-  4521 

4- 3.85

5- No 385% is on 4 logical CPUs which are 100% per each logical CPU

6- top


Score: 6 / 6 ⭐

And this is the level of reasoning I want from the course:

uptime
  ↓
load average
  ↓
compare with CPU count
  ↓
top / ps
  ↓
identify process
  ↓
understand how much CPU it consumes
  ↓
investigate the application

You've now properly covered the CPU side of Step 6.
