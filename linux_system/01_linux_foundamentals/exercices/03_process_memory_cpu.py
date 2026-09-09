# ============================================================

# Module 1.5 — Processes: Parent, Child and Signals

# ============================================================

# We have just finished CPU and RAM.

#

# We now need to understand PROCESSES in more depth,

# followed by SERVICES and LOGS.

#

# Our current model is:

#

#

# Program

# ↓

# Process

# ↓

# PID

#

#

# We are now going to add another important concept:

#

# PPID

#

# PPID stands for Parent Process ID.

# ============================================================

# 1. Parent and Child Processes

# ============================================================

# When one process creates another process, we obtain a

# parent/child relationship.

#

#

# Parent

# │

# ├── Child

# │

# └── Child

#

#

# For example:

#

#

# bash

# │

# ├── node app.js

# │

# └── sleep 1000

#

#

# The `sleep` process has:

#

# PID  = its own unique process identifier

# PPID = the PID of its parent process (bash)

#

#

# This is exactly what you were observing with:

#

# ps -p 295 -o pid,ppid,state,%cpu,%mem,cmd

#

#

# This command allows you to inspect specific information

# about a process, including:

#

# PID   → Process ID

# PPID  → Parent Process ID

# STATE → Current process state

# %CPU  → CPU usage

# %MEM  → Memory usage

# CMD   → Command that started the process

# ============================================================

# 2. How Does Linux Create a Process?

# ============================================================

# Two concepts are important here:

#

# fork()

# exec()

#

#

# ------------------------------------------------------------

# fork()

# ------------------------------------------------------------

#

# `fork()` creates a new process based on the existing process.

#

# Conceptually:

#

#

# Parent

# │

# fork()

# │

# ├── Parent

# └── Child

#

#

# The child process initially inherits many properties from

# its parent.

# ------------------------------------------------------------

# exec()

# ------------------------------------------------------------

# `exec()` replaces the current program inside a process with

# another program.

#

# Conceptually:

#

#

# bash

# │

# fork()

# │

# ▼

# New process

# │

# exec()

# ↓

# sleep

#

#

# You do NOT need to know how to program `fork()` or `exec()`

# at this stage.

#

# You only need to understand the principle because it explains

# how Linux starts and manages programs.

#

# A simplified mental model is:

#

#

# Parent process

# ↓

# fork()

# ↓

# Child process

# ↓

# exec()

# ↓

# New program

#

#

# This is an important foundation for understanding how shells

# launch commands and how processes are created.

# ============================================================

# 3. Signals

# ============================================================

# When you run:

#

# kill 295

#

# you are not sending a magical command saying:

#

# "Kill this program."

#

# You are sending a SIGNAL to the process with PID 295.

#

#

# The default signal sent by `kill` is:

#

# SIGTERM

#

#

# SIGTERM essentially means:

#

# "Please terminate cleanly."

#

#

# The process can receive the signal and perform cleanup

# before exiting.

#

# For example:

#

#

# close files

# close connections

# perform cleanup

# ↓

# exit

# ============================================================

# 3.1 SIGTERM vs SIGKILL

# ============================================================

# ------------------------------------------------------------

# SIGTERM

# ------------------------------------------------------------

# Command:

#

# kill 295

#

#

# This sends:

#

# SIGTERM

#

#

# The process can handle this signal and perform cleanup

# before terminating.

#

#

# kill 295

# ↓

# SIGTERM

# ↓

# "Please stop cleanly"

# ↓

# cleanup

# ↓

# exit

# ------------------------------------------------------------

# SIGKILL

# ------------------------------------------------------------

# Command:

#

# kill -9 295

#

#

# This sends:

#

# SIGKILL

#

#

# SIGKILL cannot be caught, blocked, or handled by the target

# process.

#

# The operating system terminates the process immediately.

#

#

# kill -9 295

# ↓

# SIGKILL

# ↓

# FORCED TERMINATION

#

#

# Practical rule:

#

# Do not automatically start with:

#

# kill -9

#

#

# In production, a common approach is:

#

# 1. Send SIGTERM

# 2. Give the process time to shut down cleanly

# 3. Investigate if it does not terminate

# 4. Use SIGKILL only when necessary

#

#

# This is important because forced termination can prevent

# an application from performing its normal cleanup.

# ============================================================

# 4. Process States

# ============================================================

# You have already seen:

#

# S

#

#

# Linux processes can have several states.

#

#

# R → Running / Runnable

# S → Sleeping

# D → Uninterruptible sleep

# T → Stopped

# Z → Zombie

#

#

# A simplified view:

#

#

# R

# ↓

# Process is running or ready to run

#

# S

# ↓

# Process is sleeping / waiting

#

# D

# ↓

# Process is waiting in an uninterruptible state,

# commonly related to I/O

#

# T

# ↓

# Process is stopped

#

# Z

# ↓

# Process has terminated but still has an entry

# in the process table

# ============================================================

# 5. Zombie Processes

# ============================================================

# A ZOMBIE process is a process that has finished executing,

# but whose parent has not yet collected its termination

# status.

#

# Conceptually:

#

#

# Parent

# │

# └── Zombie

#

#

# The process is no longer actually executing its program.

#

# It remains as an entry in the process table until the parent

# retrieves its termination status.

#

# Therefore:

#

# Zombie ≠ CPU-intensive process

#

# A zombie process does not continue consuming CPU to perform

# its original work.

#

# The important point is the relationship between the child

# process and its parent.

# ============================================================

# 6. Orphan Processes

# ============================================================

# Now consider the opposite situation.

#

# Normally:

#

#

# Parent

# │

# └── Child

#

#

# What happens if the parent process terminates while the child

# is still running?

#

#

# Parent ❌

#

# Child

# │

# └── becomes an ORPHAN

#

#

# The orphan process is then adopted by another process.

#

# On modern Linux systems, this is typically associated with

# PID 1, although the exact re-parenting mechanism can depend

# on the process hierarchy and environment.

#

# This brings us to a very important process:

# ============================================================

# 7. PID 1

# ============================================================

# PID 1 is a special process in a Linux system.

#

# On a typical Linux distribution using systemd:

#

#

# PID 1 = systemd

#

#

# You can inspect PID 1 with:

#

# ps -p 1 -f

#

#

# You may see something similar to:

#

#

# root         1       0  ... /sbin/init

#

#

# or a command/path associated with systemd.

#

#

# PID 1 has a special role in the system and is responsible

# for important parts of the system's process and service

# management.

#

# Understanding PID 1 will become particularly useful when we

# move on to:

#

# systemd

# services

# service dependencies

# logs

# system startup

#

#

# The important mental model for now is:

#

#

# Process

# │

# ├── PID

# │

# ├── PPID

# │

# ├── State

# │

# └── Signals

#

#

# These concepts allow us to understand not only that a process

# exists, but also how it was created, who its parent is, what

# state it is in, and how Linux can communicate with it.



# ============================================================

# What You Should Have in Mind Now

# ============================================================

# At this point, you should have the following mental model

# of processes on a Linux system:

#

#

# Linux

# │

# PID 1

# │

# systemd

# │

# ┌────┴────┐

# │         │

# bash       sshd

# │

# ┌───┴────┐

# │        │

# node     sleep

#

#

# Linux manages a hierarchy of processes.

#

# A process can create child processes, which creates a

# parent/child relationship represented by the PID and PPID.

# ============================================================

# Process Information

# ============================================================

# Every process has several important attributes, including:

#

#

# PID

# PPID

# STATE

# CPU

# RAM

#

#

# PID:

# Process ID.

# The unique identifier of the process.

#

# PPID:

# Parent Process ID.

# The PID of the process that created or launched it.

#

# STATE:

# The current state of the process.

#

# CPU:

# The amount of CPU resources being used by the process.

#

# RAM:

# The amount of memory being used by the process.

# ============================================================

# Communication with the System

# ============================================================

# Processes interact with the operating system through

# mechanisms such as:

#

# System Calls

# Signals

#

#

# SYSTEM CALLS allow a program to request services from

# the kernel.

#

# For example, a program may need to:

#

# - Read a file

# - Write to a file

# - Allocate memory

# - Create a process

# - Open a network connection

#

#

# The general idea is:

#

#

# Application

# │

# │ System Call

# ▼

# Kernel

# │

# ▼

# Hardware

#

#

# SIGNALS allow the operating system or another process

# to notify a process about an event or request an action.

#

# For example:

#

#

# kill PID

# │

# ▼

# SIGTERM

# │

# ▼

# Process

#

#

# The key concepts to remember are:

#

#

# Program

# ↓

# Process

# ↓

# PID / PPID / STATE

# ↓

# CPU / RAM / Resources

# ↓

# System Calls + Signals

# ↓

# Kernel

#

#

# This mental model will be useful when we move on to

# Linux services, systemd, logs, and troubleshooting.
