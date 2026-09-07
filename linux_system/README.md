# 🐧 Linux & System — Learning Roadmap

This section covers the Linux and system fundamentals required to progress toward Cloud Engineering.

The goal is not to memorize commands, but to understand how a Linux system works and how to troubleshoot it.

---

## 1. Linux Fundamentals

**Objective:** Become comfortable navigating and interacting with a Linux system through the command line.

### Topics

* Linux command line
* Working with files and directories
* Absolute and relative paths
* Creating, copying, moving and deleting files
* Reading and searching file contents
* Wildcards and pattern matching
* Pipes and command chaining
* Input/output redirection
* Standard input, output and error
* Exit codes

### Main commands

```bash
pwd
ls
cd
mkdir
touch
cp
mv
rm
cat
less
head
tail
grep
find
sort
uniq
wc
cut
xargs
```

---

## 2. Linux Filesystem

**Objective:** Understand how files and directories are organized in Linux.

### Topics

* Linux filesystem hierarchy
* Root directory `/`
* Home directories
* Configuration files
* Logs
* Temporary files
* System and device files
* `/proc` and system information

### Important directories

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── opt
├── proc
├── root
├── run
├── tmp
├── usr
└── var
```

### Key directories

| Directory | Purpose                        |
| --------- | ------------------------------ |
| `/home`   | User files                     |
| `/etc`    | System configuration           |
| `/var`    | Variable data and logs         |
| `/tmp`    | Temporary files                |
| `/proc`   | Kernel and process information |
| `/dev`    | Devices                        |
| `/usr`    | Programs and libraries         |
| `/opt`    | Additional software            |

---

## 3. Linux Permissions & Users

**Objective:** Understand how Linux controls access to files and system resources.

### Topics

* Users
* Groups
* File ownership
* Read / write / execute permissions
* Permission notation
* Numeric permissions
* `sudo`
* Changing ownership and permissions

### Main commands

```bash
whoami
id
groups
useradd
passwd
chmod
chown
chgrp
sudo
```

Example:

```bash
chmod 755 script.sh
```

Understand the relationship between:

```text
Owner       Group       Others
 rwx         r-x         r--
```

---

## 4. Processes

**Objective:** Understand how Linux executes and manages programs.

### Topics

* Programs vs processes
* Process IDs (PID)
* Parent and child processes
* Foreground and background processes
* Signals
* Terminating processes
* CPU and memory consumption

### Main commands

```bash
ps
ps aux
top
htop
kill
kill -9
```

Mental model:

```text
Program
   ↓
Process
   ↓
CPU / RAM
```

---

## 5. Services & systemd

**Objective:** Understand how long-running applications and system services are managed.

### Topics

* Services
* `systemd`
* Service lifecycle
* Starting and stopping services
* Restarting services
* Enabling services at boot
* Checking service status

### Main commands

```bash
systemctl status
systemctl start
systemctl stop
systemctl restart
systemctl enable
```

Example:

```bash
systemctl status nginx
```

---

## 6. Logs & Troubleshooting

**Objective:** Learn how to investigate problems on a Linux server.

### Topics

* System logs
* Application logs
* `systemd` journal
* Reading logs
* Following logs in real time
* Identifying errors
* Basic troubleshooting methodology

### Main commands

```bash
journalctl
journalctl -u nginx
journalctl -f
```

Basic troubleshooting approach:

```text
Application not working
        ↓
Is the process running?
        ↓
Is the service active?
        ↓
Is the port open?
        ↓
What do the logs say?
        ↓
Is the network working?
        ↓
Are permissions correct?
```

---

## 7. Bash & Shell Scripting

**Objective:** Automate repetitive system administration tasks.

### Topics

* Shell basics
* Variables
* Conditions
* Loops
* Functions
* Arguments
* Exit codes
* Pipes
* Redirections
* Command chaining
* Script execution

Example:

```bash
#!/bin/bash

echo "Starting application..."

if [ -f "app.conf" ]; then
    echo "Configuration found"
else
    echo "Configuration missing"
fi
```

Important concepts:

```text
Variables
Conditions
Loops
Functions
Arguments
Exit codes
Pipes
Redirections
```

---

## 8. System Resources

**Objective:** Understand how to inspect and diagnose machine resources.

### Topics

* CPU
* RAM
* Disk usage
* Disk I/O
* System load
* Processes consuming resources
* Basic system monitoring

### Main commands

```bash
top
free -h
df -h
du -sh
uptime
vmstat
uname
```

Troubleshooting mindset:

```text
Server is slow
      ↓
CPU?
RAM?
Disk?
I/O?
Network?
Process?
```

---

## 9. Storage & Filesystems

**Objective:** Understand how Linux manages disks and storage.

### Topics

* Files
* Directories
* Disks
* Partitions
* Filesystems
* Mount points
* Volumes

### Main commands

```bash
lsblk
df -h
du -sh
mount
umount
```

Mental model:

```text
Physical Disk
      ↓
Partition
      ↓
Filesystem
      ↓
Mount Point
      ↓
/data
```

This foundation will later make Cloud storage concepts easier to understand:

```text
Linux Storage
      ↓
Cloud Storage
      ↓
EBS / EFS / Persistent Disks / Object Storage
```

---

## 10. Linux Networking

**Objective:** Understand how applications communicate through a Linux system.

### Topics

* Network interfaces
* IP addresses
* Routing
* Ports
* TCP / UDP
* Sockets
* DNS
* HTTP / HTTPS
* Network troubleshooting

### Main commands

```bash
ip addr
ip route
ss
ping
curl
wget
dig
nslookup
traceroute
```

Mental model:

```text
Application
     ↓
Socket
     ↓
TCP / UDP
     ↓
IP
     ↓
Network Interface
     ↓
Network
```

Example:

```bash
ss -tulpn
```

This helps identify listening ports and the processes using them.

---

## 11. Operating System Fundamentals

**Objective:** Understand the main concepts behind a Linux operating system.

### Topics

* Kernel
* User space
* Kernel space
* System calls
* Processes
* Threads
* CPU
* Memory
* Filesystems
* I/O
* Signals
* Permissions

Mental model:

```text
Applications
      ↓
System Calls
      ↓
Kernel
      ↓
Hardware
```

The goal is to understand the concepts without going deeply into kernel development.

---

# 🎯 Progression Toward Cloud Engineering

The Linux and system roadmap should progressively connect to the technologies that come later.

```text
Linux Fundamentals
        ↓
Filesystem
        ↓
Permissions & Users
        ↓
Processes
        ↓
Services
        ↓
Logs & Troubleshooting
        ↓
Bash
        ↓
System Resources
        ↓
Storage
        ↓
Networking
        ↓
Docker
        ↓
Cloud
        ↓
Terraform
        ↓
CI/CD
        ↓
Kubernetes
```

---

# 🧠 Main Objective

By the end of this section, the goal is to be able to look at a Linux server and reason about it:

```text
What is running?
        ↓
Which process is using the resources?
        ↓
Which ports are open?
        ↓
Where are the configuration files?
        ↓
Where are the logs?
        ↓
Which user owns the process?
        ↓
Which permissions are required?
        ↓
How is the application communicating?
        ↓
Where could the problem be?
```

The objective is therefore **system reasoning and troubleshooting**, rather than simply memorizing Linux commands.

---

## Next Step

Once these Linux and system fundamentals are sufficiently comfortable, the next major step is **Docker**.

Docker will build directly on concepts already learned:

```text
Linux
  ↓
Processes
  ↓
Filesystem
  ↓
Networking
  ↓
Resources
  ↓
Docker
```

This will make it possible to understand containers as Linux processes and isolated environments, rather than only learning Docker commands.

---

> **Note:** This roadmap will be updated as progress is made through the exercises and new system concepts are introduced.
