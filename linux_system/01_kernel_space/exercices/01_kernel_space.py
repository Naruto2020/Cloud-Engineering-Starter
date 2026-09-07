# ============================================================

# Module 1 — Understanding a Linux Machine

# ============================================================

# Today's objective is to understand what a Linux system

# actually is and how its main components interact.

#

# By the end of this module, you should be able to explain

# the following architecture:

#

#

# ┌─────────────────────────────┐

# │       Applications          │

# │  nginx / node / python ...  │

# └──────────────┬──────────────┘

# │

# ▼

# ┌─────────────────────────────┐

# │           Kernel            │

# │ CPU │ RAM │ Disk │ Network  │

# └──────────────┬──────────────┘

# │

# ▼

# ┌─────────────────────────────┐

# │          Hardware           │

# │ CPU │ RAM │ SSD │ NIC ...   │

# └─────────────────────────────┘

# ============================================================

# 1. What is an Operating System?

# ============================================================

# A computer has hardware:

#

# - CPU

# - RAM

# - Disk

# - Network interface

# - Other devices

#

# However, an application such as:

#

# node app.js

#

# does not directly manipulate the CPU or the disk.

#

# Instead, it interacts with the Operating System.

#

# The Operating System is responsible for providing services

# such as:

#

# - Process management

# - Memory management

# - File management

# - Network management

# - User management

# - Access to hardware

#

# In Linux, the core of the Operating System is called

# the KERNEL.

# ============================================================

# 2. The Kernel

# ============================================================

# Imagine that your application needs to execute:

#

# const data = readFile("config.json");

#

# The application does not directly tell the SSD:

#

# "Hey SSD, give me the data."

#

# Instead, the application requests the service through

# the operating system using a SYSTEM CALL.

#

#

# Application

# │

# │ system call

# ▼

# Kernel

# │

# ▼

# Filesystem

# │

# ▼

# Disk

#

#

# The kernel therefore acts as an intermediary between

# applications and the hardware.

#

# It manages access to important system resources such as:

#

# - CPU

# - Memory

# - Storage

# - Network

# - Devices

# ============================================================

# 3. User Space vs Kernel Space

# ============================================================

# This is an important concept for a Cloud Engineer.

#

# We can simplify Linux into two main worlds:

#

#

# ┌──────────────────────────────┐

# │          USER SPACE          │

# │                              │

# │ bash                         │

# │ node                         │

# │ nginx                        │

# │ python                       │

# │ docker                       │

# │ etc.                         │

# └──────────────┬───────────────┘

# │

# System Calls

# │

# ┌──────────────▼───────────────┐

# │         KERNEL SPACE         │

# │                              │

# │ CPU                          │

# │ Memory                       │

# │ Filesystem                   │

# │ Network                      │

# │ Devices                      │

# └──────────────────────────────┘

#

#

# When you execute:

#

# ls

#

# "ls" is a program running in USER SPACE.

#

# When it needs information about files and directories,

# it requests that information from the kernel.

#

# The kernel then interacts with the filesystem and the

# underlying hardware when necessary.

# ============================================================

# 4. Processes

# ============================================================

# Now we reach another fundamental concept.

#

# When you run:

#

# node app.js

#

# you are executing a program.

#

# The operating system creates a PROCESS to run that program.

#

#

# app.js

# ↓

# Node.js

# ↓

# Process

# ↓

# PID = 1234

#

#

# PID stands for PROCESS ID.

#

# It is the unique identifier assigned to a process.

#

# You can inspect running processes with:

#

# ps

#

# or:

#

# ps aux

#

#

# Example output:

#

#

# USER    PID   %CPU   %MEM   COMMAND

# root      1    0.0    0.1   systemd

# steve  1234    2.1    1.4   node app.js

# steve  1280    0.0    0.2   bash

# ============================================================

# 5. Why is the PID important?

# ============================================================

# Because in production, you will often encounter problems

# such as:

#

# "My application is not responding."

#

# One of the first things you may want to check is whether

# the application process is still running.

#

# For example:

#

# ps aux | grep node

#

#

# If you find:

#

# steve  1234 ... node app.js

#

# you know that the Node.js process exists and has PID 1234.

#

# You can then investigate its state, resource usage,

# logs, network connections, etc.

#

# If necessary, you can also terminate the process:

#

# kill 1234

#

#

# This is the beginning of a fundamental Cloud Engineering

# skill:

#

# Application problem

# ↓

# Is the process running?

# ↓

# What is its PID?

# ↓

# What resources is it using?

# ↓

# What do the logs say?

# ↓

# What is the actual cause of the problem?

#

#

# The objective is not simply to memorize Linux commands.

# The objective is to understand what is happening inside

# the machine and develop a systematic troubleshooting mindset.


# ============================================================

# Your First Exercise

# ============================================================

# Do not look at the answers immediately.

#

# Try to reason about each question first.

# The goal is to understand the concepts, not simply memorize

# the answers.

# ============================================================

# Question 1

# ============================================================

# When you run:

#

# node app.js

#

# what is the difference between the PROGRAM and the PROCESS?

#

# Think about what exists on disk before you execute the command

# and what the operating system creates when the program starts.

The PROGRAM is the code/instruction stored on disk (eg :app.js)
The PROCESS is a running instance of that PROGRAM created and managed
by operating system

- app.js → program (the code)
- node app.js → starts a process
- The OS gives that process a PID and resources such as memory and CPU time.

💡 Key idea: One program can have multiple processes running at the same time.

# ============================================================

# Question 2

# ============================================================

# What is the purpose of a PID?

#

# Remember:

#

# PID = Process ID

#

# Think about why the operating system needs to identify

# individual processes.

The PID is a unique identifier assigned to a process. 
It helps operating system and users to identify and manage
that specific process.

# ============================================================

# Question 3

# ============================================================

# Why can:

#

# kill 1234

#

# stop an application?

#

# Think about the relationship between the PID and the process,

# and what the "kill" command actually targets.

kill 1234 will target the running process with  1234 PID and
send it a signal to terminate

💡 Key idea: kill targets a process, not directly the application/program.

# ============================================================

# Question 4

# ============================================================

# In this architecture:

#

#

# Node.js

# ↓

# ?

# ↓

# Kernel

# ↓

# Hardware

#

#

# What is missing?

#

# Think about the entity created by the operating system when

# Node.js is running.

The missing component is System call

# ============================================================

# Question 5

# ============================================================

# Do bash, node, and nginx belong to USER SPACE or KERNEL SPACE?

#

# Explain your answer based on the distinction between:

#

# User Space

# ↓

# System Calls

# ↓

# Kernel Space

#

# Do not just give the answer.

# Try to explain WHY they belong to that space.

Bash, node, and nginx belong to USER SPACE because they are all 
programs (application and/or interfaces) that run outside the kernel.
They helps users to interact with the OS through system calls.
