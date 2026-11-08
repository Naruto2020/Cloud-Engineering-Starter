
========================================================================

		Operating System Architecture

========================================================================


Notion 1: Kernel vs User Space

An operating system separates execution into two main areas: Kernel Space
and User Space.

1. Kernel Space

The kernel is the core component of an operating system. It manages 
access to hardware and system resources.

Its responsibilities include:

- CPU scheduling.
- Memory management.
- Process management.
- Hardware communication.
- Filesystem management.
- Network operations.

The kernel operates with privileged access to hardware.



2. User Space

User Space is where normal applications execute.

Examples:

- Node.js applications.
- Python scripts.
- Nginx.
- PostgreSQL.
- Docker CLI.

Applications do not have unrestricted access to hardware. They must 
request certain operations from the kernel.



3. How do they interact?

Imagine your Node.js application wants to read a file.

1. Node.js requests access to the file.
2. The request goes through a system call.
3. The kernel checks permissions and accesses the filesystem.
4. The kernel returns the result to Node.js.


4. Why is this separation important?

It provides:

- Security: Applications cannot freely access protected hardware or 
kernel memory.

- Stability: An application failure does not necessarily crash the entire
operating system.

- Resource management: The kernel controls how applications use CPU, 
memory and hardware.


Exercise 1
Imagine you are running a Python application on an EC2 Linux instance.

The application needs to read a file from disk.

Question: Why can't the Python application directly access the physical 
disk, and which operating system component handles the request?

Answer in your own words.


==> Python application can't  directly access the physical disk because 
it's bellong to User Space which is not the component that manage files 
system.

It ll call OS name System call to  send request to the Kernel 


===>  Correction and refinement

1. Why can't Python directly access the physical disk?

Correct. Python runs in User Space, where applications have restricted 
privileges. It cannot directly control hardware or access protected kernel resources.

2. How does it communicate with the kernel?

Correct. It uses a system call to request an operation from the kernel.



Notion 2: System Calls


A system call is the mechanism that allows an application running in User
Space to request a service from the kernel.

Applications cannot directly perform privileged operations, so they ask
the kernel to perform them.


1. Common Linux system calls


System call	Purpose
openat()	Open a file
read()		Read data
write()		Write data
close()		Close a file descriptor
fork()		Create a process
execve()	Execute a program
socket()	Create a network socket
connect()	Establish a connection



2. How a system call works

Imagine a Python application wants to read a file.
User Space

Python application calls open() and read()

System call

Kernel Space
Checks permissions and handles filesystem access

Storage

Disk data is accessed when necessary


The kernel then returns the result to the application.


3. What happens technically?

When an application makes a system call:

1. It prepares the system call number and arguments.
2. The CPU executes a special instruction to enter kernel mode.
3. The kernel identifies and executes the requested operation.
4. The kernel returns a result and execution resumes in User Space.
This transition is called a mode switch (User Mode → Kernel Mode).


Important: A mode switch is not necessarily a context switch. A system call can enter and leave the kernel without switching to another 
thread.


Exercise 2

Imagine your Node.js application needs to send an HTTP request to an 
external API.

Question: Which operating system component handles the low-level network 
operations, and how does your application request those operations?

Answer in your own words. We'll correct it before moving to the next 
notion.

==> The OS that handles the low-level network  operations is : 
Kernel

Those operations are request througth System Call



Notion 3: User Mode vs Kernel Mode

The CPU operates in different privilege modes:

- User Mode: Applications run with restricted privileges. They cannot 
directly execute privileged instructions or access protected kernel memory.

- Kernel Mode: The operating system kernel runs with elevated privileges 
and can manage hardware and system resources.


When an application makes a system call, the CPU transitions from User 
Mode to Kernel Mode. Once the operation finishes, execution returns to 
User Mode.

Why does this matter?

It protects the operating system from applications that crash, behave 
incorrectly, or attempt unauthorized operations.

