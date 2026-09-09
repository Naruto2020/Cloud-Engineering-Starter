# ============================================================

# Module 1 — Processes, Memory and CPU

# ============================================================

# We now move on to the second part:

#

# PROCESSES, MEMORY AND CPU

#

# This is a very important topic for a Cloud Engineer because

# many production problems can be reduced to questions such as:

#

# CPU overloaded?

# RAM overloaded?

# Too many processes?

# Process blocked?

#

# The goal is to understand what a running process actually

# consumes and how Linux manages CPU and memory resources.

# ============================================================

# 1. A Process — What Does It Actually Consume?

# ============================================================

# We have already seen:

#

#

# Program

# ↓

# Execution

# ↓

# Process

#

#

# But a process is not simply "code that is running".

#

# When Linux creates a process, it associates several

# important pieces of information with it:

#

#

# ┌─────────────────────────┐

# │       Process           │

# ├─────────────────────────┤

# │ PID                     │

# │ Memory                  │

# │ CPU                     │

# │ Open files              │

# │ Permissions             │

# │ State                   │

# │ Parent process          │

# └─────────────────────────┘

#

#

# For example:

#

# node app.js

#

# could result in:

#

#

# PID  = 1234

# RAM  = 150 MB

# CPU  = 5%

# PPID = 800

#

#

# PPID stands for Parent Process ID.

#

# It identifies the process that created or launched this

# process.

# ============================================================

# 2. The CPU

# ============================================================

# The CPU executes instructions.

#

# In a very simplified representation:

#

#

# Process A ─┐

# Process B ─┼──► CPU

# Process C ─┘

#

#

# A single CPU core cannot literally execute all processes

# simultaneously.

#

# Linux therefore uses a SCHEDULER.

#

# The scheduler decides which process gets CPU time.

#

#

# Process A

# ↓

# Process B

# ↓

# Process C

# ↓

# Process A

# ↓

# ...

#

#

# These switches happen extremely quickly, creating the

# impression that multiple processes are running at the same

# time.

#

# On a machine with multiple CPU cores, multiple instructions

# can actually be executed in parallel.

# ============================================================

# 3. CPU — %CPU

# ============================================================

# When you run:

#

# ps aux

#

# you can see information such as:

#

#

# USER   PID   %CPU   %MEM   COMMAND

#

#

# For example:

#

#

# steve  1234  85.0   4.2    node app.js

#

#

# This indicates that the process is currently using a

# significant amount of CPU.

#

# However, the exact interpretation of %CPU depends on factors

# such as:

#

# - The number of CPU cores

# - The operating system

# - The tool being used

# - How CPU usage is measured

#

# Therefore, %CPU should always be interpreted in context.

# ============================================================

# 4. RAM — Memory

# ============================================================

# RAM contains data and instructions that programs need while

# they are running.

#

# A simplified representation could look like this:

#

#

# RAM

# ┌────────────────────────────┐

# │ Linux Kernel               │

# ├────────────────────────────┤

# │ Node.js                    │

# │                            │

# │ app.js                     │

# │ variables                  │

# │ objects                    │

# ├────────────────────────────┤

# │ nginx                      │

# ├────────────────────────────┤

# │ PostgreSQL                 │

# └────────────────────────────┘

#

#

# For example, if your program contains:

#

# const users = [];

#

# and continuously adds a large amount of data to `users`,

# the program will consume more memory.

#

# This is why memory usage is an important resource to monitor

# in production.

# ============================================================

# 5. What Happens When RAM Is Full?

# ============================================================

# This is a very important production scenario.

#

# Imagine:

#

#

# RAM = 8 GB

#

# Node.js      3 GB

# PostgreSQL   2 GB

# Nginx        500 MB

# Linux        1 GB

# Other        1 GB

# --------------------

# Total        7.5 GB

#

#

# Then Node.js consumes another 1 GB.

#

# The system is now under severe memory pressure.

#

# Linux can use SWAP as an additional mechanism for handling

# memory pressure.

#

#

# RAM

# │

# │ almost full

# ▼

# Swap

# │

# ▼

# Disk

#

#

# However, disk storage is much slower than RAM.

#

# Therefore, a machine that is heavily relying on swap can

# become extremely slow.

# ============================================================

# 6. RAM vs Swap

# ============================================================

# Conceptually:

#

#

# FAST

# ▲

# │

# RAM

# │

# ▼

# SWAP

# │

# ▼

# DISK

# SLOW

#

#

# Swap allows the operating system to move certain memory

# pages from RAM to disk in order to free physical memory.

#

# But:

#

# SWAP IS NOT A HIGH-PERFORMANCE REPLACEMENT FOR RAM.

#

# In a Cloud environment, heavy or continuous swapping is often

# a signal that memory usage should be investigated.

# ============================================================

# 7. How Can We Check Memory Usage?

# ============================================================

# One useful command is:

#

# free -h

#

# You may see something similar to:

#

#

# total   used   free   shared  buff/cache  available

# Mem:           7.7G    3.2G   1.5G    200M       3.0G       4.1G

# Swap:          2.0G    100M   1.9G

#

#

# Important values include:

#

# total

# used

# available

# swap

#

#

# IMPORTANT:

#

# Do not look only at:

#

# free

#

#

# Linux intentionally uses some RAM for filesystem caches and

# other purposes.

#

# Therefore, `available` is often more useful for understanding

# how much memory can realistically be allocated to new

# applications without significant memory pressure.

# ============================================================

# 8. top

# ============================================================

# One of the most important commands for monitoring a Linux

# system is:

#

# top

#

# It provides a dynamic view of processes and system resources.

#

# For example:

#

#

# top - 15:30:10 up 2 days

# Tasks: 150 total

# %Cpu(s): 12.5 us, 3.2 sy, ...

# MiB Mem : 7900 total, ...

#

#

# You can then see individual processes:

#

#

# PID    USER      %CPU   %MEM   COMMAND

# 1234   steve      80.0    5.2   node

# 500    root        2.0    1.1   nginx

# 700    postgres    1.5    8.0   postgres

#

#

# You can immediately start asking:

#

# Why is Node.js using 80% of the CPU?

#

# This is exactly the kind of question a Cloud Engineer must

# learn to investigate.

# ============================================================

# 9. CPU vs RAM — Understanding the Difference

# ============================================================

# It is important to distinguish CPU problems from memory

# problems.

# ------------------------------------------------------------

# Situation A — High CPU Usage

# ------------------------------------------------------------

#

# CPU : 99%

# RAM : 30%

#

#

# This could indicate a CPU-bound workload.

#

# For example:

#

#

# while (true) {

# // CPU-intensive calculation

# }

#

#

# The program continuously performs calculations and therefore

# consumes a significant amount of CPU while potentially using

# relatively little RAM.

# ------------------------------------------------------------

# Situation B — High Memory Usage

# ------------------------------------------------------------

#

# CPU : 10%

# RAM : 98%

#

#

# This could indicate a memory-related problem.

#

# For example:

#

#

# const data = [];

#

# while (true) {

# data.push("huge amount of data");

# }

#

#

# The amount of memory used by the program can continuously

# increase.

#

# Eventually, this can contribute to an:

#

# OUT OF MEMORY (OOM)

#

# condition.

# ============================================================

# 10. The OOM Killer

# ============================================================

# Linux has a mechanism called the:

#

# OOM KILLER

#

# OOM stands for:

#

# Out Of Memory

#

#

# If the system experiences severe memory pressure and cannot

# satisfy memory allocations, Linux may select processes to

# terminate in order to reclaim memory.

#

# Conceptually:

#

#

# PostgreSQL

# ↓

# High memory usage

#

# Node.js

# ↓

# High memory usage

#

# RAM

# ↓

# FULL

# ↓

# OOM

# ↓

# Linux terminates a process

#

#

# As a result, an application can suddenly disappear or stop

# working without being explicitly stopped by an administrator.

#

# In production environments, this is a very important

# situation to diagnose.

#

# A Cloud Engineer should therefore be able to investigate:

#

# - Which process consumed the memory?

# - How much memory was available?

# - Was swap being used?

# - Did the system trigger the OOM Killer?

# - Which process was terminated?

# - What caused memory usage to grow?

#

# The objective is not simply to observe that the server is

# "slow" or "out of memory".

#

# The objective is to identify the resource under pressure,

# understand why it is under pressure, and find the root cause.




# ============================================================

# Exercise — Processes, Memory and CPU

# ============================================================

# After running the commands, answer the following questions.

#

# Try to answer them using your own understanding of the

# concepts covered in this module.

# ============================================================

# Question 1

# ============================================================

# What is the difference between CPU and RAM?

#

# Think about the role of each resource:

#

# CPU → ?

# RAM → ?

CPU executes programs.
RAM stores programs data

# ============================================================

# Question 2

# ============================================================

# If you see:

#

#

# CPU = 95%

# RAM = 20%

#

#

# What type of problem would you suspect?

#

# Explain your reasoning.

I would suspect a CPU-bound.
Because 95% CPU usage is very high.

# ============================================================

# Question 3

# ============================================================

# If you see:

#

#

# CPU = 10%

# RAM = 98%

#

#

# What type of problem would you suspect?

#

# Explain your reasoning.

I would suspect a memory problem.
Because 98% RAM usage is too high.

# ============================================================

# Question 4

# ============================================================

# What is the purpose of SWAP?

#

# Think about the relationship between:

#

# RAM

# ↓

# Swap

# ↓

# Disk

SWAP is used by OS to move some data to de Disk when there
is not enough place on RAM

# ============================================================

# Question 5

# ============================================================

# Why should you NOT necessarily assume that:

#

#

# free = 0

#

#

# means that Linux has no memory available?

#

# Think about how Linux uses RAM for caching and the difference

# between `free` and `available`.

Because sometime Linux use RAM for caching so it is better
to look at available than only free.

# ============================================================

# Question 6

# ============================================================

# What is the purpose of:

#

# top

#

#

# What kind of information can you observe with this command?

The top command gives us a dynamic overview of all
processes running on the OS

# ============================================================

# Question 7

# ============================================================

# What does OOM mean?

#

# OOM = ?

#

#

# What can happen when a Linux system runs critically low

# on memory?

OOM mean Out Of Memory.
when Linux system runs critically low on memory,
the OOM killer can be triggered.


# ============================================================

# Question 8

# ============================================================

# In:

#

#

# PID   PPID   STATE

# 415   300    S

#

#

# What do PID, PPID, and S represent?

#

#

PID   →  unique Process ID

PPID  → unique Parent Process ID

S     → Process is in Sleeping State

#

#

# Try to explain what this tells you about the process.

This help me to find and manage one specific process,
its parent process and its state

