# Bash & Linux Learning Journey

This repository documents my learning journey in **Linux and Bash**, with a focus on the practical skills required for **System Administration, Automation, and Cloud Engineering**.

The objective is not to learn Bash in isolation, but to understand how Linux systems work and how command-line tools and shell scripts can be used to manage, troubleshoot, and automate infrastructure.

---

## 🎯 Learning Objectives

Throughout this learning journey, I aim to develop practical skills in:

* Linux command-line navigation
* File manipulation and searching
* Text processing and log analysis
* Permissions and user management
* Process and service management
* System resource monitoring
* Linux networking
* Pipes and redirections
* Bash scripting
* Task automation
* SSH and remote administration
* AWS CLI
* Docker automation

The final goal is to apply these skills in real-world **Cloud Engineering and DevOps environments**.

---

# 📚 Learning Roadmap

## 🟢 Linux Fundamentals

### Filesystem and Navigation

Understanding the Linux filesystem and navigating efficiently through directories.

Topics include:

* Absolute and relative paths
* Files and directories
* Directory navigation
* Creating and managing directories
* Understanding the Linux filesystem hierarchy

---

### Reading and Searching

Working with files, text, and logs using essential Linux commands.

Commands and concepts include:

```bash
cat
less
head
tail
wc
sort
uniq
cut
grep
find
```

Practical examples:

```bash
grep "ERROR" app.log
tail -f app.log
find /var/log -name "*.log"
```

This section also introduces log analysis and efficient command-line searching.

---

## 🟢 Permissions and Users

Understanding Linux permissions and access control.

Topics include:

```text
-rwxr-xr--
```

Commands:

```bash
chmod
chown
chgrp

whoami
id
groups
sudo
```

Examples:

```bash
chmod 755 script.sh
chmod +x script.sh

sudo chown user:user file
```

### Cloud Perspective

Understanding who can read, write, or execute resources on a server is fundamental for system administration and Cloud environments.

---

## 🟢 Processes and System Management

Learning how Linux manages running processes and system services.

Commands include:

```bash
ps
top
htop
pgrep
kill
pkill
jobs
bg
fg
```

Service and log management:

```bash
systemctl
journalctl
```

Examples:

```bash
systemctl status nginx
journalctl -u nginx
```

These tools are essential for troubleshooting and maintaining Linux servers.

---

## 🟢 System Resources

Learning how to monitor and diagnose system performance.

Commands include:

```bash
free
df
du
lsblk
uptime
lscpu
```

Examples:

```bash
free -h
df -h
du -sh /var/log/*
```

The objective is to be able to investigate common server issues and determine whether performance problems are related to:

* CPU usage
* Memory usage
* Disk space
* System load

---

## 🟢 Linux Networking

Applying networking concepts directly within Linux environments.

Commands include:

```bash
ip
ss
ping
curl
wget
dig
nslookup
traceroute
```

Important commands:

```bash
ip addr
ip route
ss -tulpn
ping 8.8.8.8
curl https://example.com
```

Key concepts include:

* localhost
* 127.0.0.1
* 0.0.0.0
* Ports
* TCP
* UDP
* DNS
* Routing

---

# 🟡 Bash Fundamentals

## Pipes and Redirections

Understanding how Linux commands communicate with each other.

Operators:

```bash
>
>>
<
|
```

Examples:

```bash
cat server.log | grep ERROR
```

```bash
echo "hello" > file.txt
```

```bash
echo "another line" >> file.txt
```

Error handling and redirection:

```bash
2>
2>&1
```

Background execution:

```bash
&
```

A particular focus will be placed on understanding pipes and avoiding unnecessary command chaining when a single command can perform the required task.

---

## Variables

Learning how to define and use variables in Bash.

```bash
name="server-01"
echo "$name"
```

Environment variables:

```bash
$HOME
$USER
$PATH
$PWD
```

Exporting variables:

```bash
export AWS_REGION="eu-west-3"
```

Environment variables are particularly important when working with Cloud platforms and automation tools.

---

## Conditions

Using conditional logic in Bash scripts.

```bash
if
then
else
fi
```

Example:

```bash
if [ "$CPU" -gt 80 ]; then
    echo "High CPU"
fi
```

Logical operators:

```bash
&&
||
!
```

---

## Loops

Automating repetitive tasks with loops.

```bash
for
while
```

Example:

```bash
for server in server1 server2 server3
do
    echo "$server"
done
```

Working with files:

```bash
for file in *.log
do
    echo "$file"
done
```

---

## Functions

Organizing Bash scripts into reusable functions.

```bash
check_server() {
    echo "Checking server..."
}
```

Working with parameters:

```bash
$1
$2
$@
$#
```

---

## Bash Scripts

Building executable and reliable Bash scripts.

```bash
#!/bin/bash
```

Running scripts:

```bash
chmod +x script.sh
./script.sh
```

Script reliability and error handling:

```bash
set -e
set -u
set -o pipefail
```

---

# 🟠 System Automation

## Cloud-Oriented Automation

Applying Bash scripting to common system administration tasks.

Potential automation tasks include:

* Checking server health
* Cleaning logs
* Backing up files
* Monitoring disk usage
* Checking running processes
* Restarting services
* Creating multiple users
* Installing and configuring servers
* Collecting system information

Example project:

```text
server-health.sh
```

Possible output:

```text
Server: web-01

CPU:       34%
Memory:    61%
Disk:      72%

Nginx:     RUNNING
SSH:       RUNNING

Network:   OK
```

---

## SSH and Remote Administration

Learning how to securely interact with remote Linux servers.

Commands:

```bash
ssh
scp
rsync
```

Example:

```bash
ssh ubuntu@server-ip
```

File transfer:

```bash
scp app.log ubuntu@server:/tmp/
```

Key concepts:

* Private keys
* Public keys
* SSH authentication
* `authorized_keys`
* Secure remote administration

---

## Cron and Task Scheduling

Automating recurring tasks.

```bash
crontab
```

Example:

```bash
0 2 * * * /home/user/backup.sh
```

The objective is to understand how scheduled tasks work locally before connecting these concepts to Cloud-based automation.

---

# 🔴 Cloud Integration

## Bash and AWS

Using Bash together with the AWS CLI.

Examples:

```bash
aws s3 ls
```

```bash
aws ec2 describe-instances
```

Example script:

```bash
#!/bin/bash

INSTANCE_ID="i-123456"

aws ec2 describe-instances \
    --instance-ids "$INSTANCE_ID"
```

JSON processing with:

```bash
jq
```

The goal is to automate AWS operations and interact with cloud infrastructure directly from the command line.

---

## Bash and Docker

Using Bash to automate container operations.

Commands include:

```bash
docker ps
docker images
docker logs
docker exec
```

Automation scenarios:

* Starting containers
* Checking container status
* Collecting logs
* Cleaning unused resources
* Automating simple deployments

---

# 🚀 Final Project — Server Operations Toolkit

The final project will combine the concepts learned throughout this repository.

```text
cloud-tools/
│
├── health-check.sh
├── disk-check.sh
├── log-analyzer.sh
├── service-check.sh
├── backup.sh
├── cleanup.sh
└── deploy.sh
```

The project will incorporate:

* Linux commands
* Variables
* Conditions
* Loops
* Functions
* Script parameters
* Exit codes
* Logging
* Error handling
* System monitoring
* SSH
* AWS CLI

---

# 🎯 Target Skill Level

| Domain                 | Target |
| ---------------------- | ------ |
| Linux Navigation       | ⭐⭐⭐⭐⭐  |
| Files and Directories  | ⭐⭐⭐⭐⭐  |
| Permissions            | ⭐⭐⭐⭐⭐  |
| Processes              | ⭐⭐⭐⭐⭐  |
| Services / systemd     | ⭐⭐⭐⭐⭐  |
| Logs                   | ⭐⭐⭐⭐⭐  |
| Linux Networking       | ⭐⭐⭐⭐⭐  |
| Pipes and Redirections | ⭐⭐⭐⭐⭐  |
| Bash Variables         | ⭐⭐⭐⭐⭐  |
| Conditions             | ⭐⭐⭐⭐   |
| Loops                  | ⭐⭐⭐⭐   |
| Functions              | ⭐⭐⭐⭐   |
| Bash Scripts           | ⭐⭐⭐⭐⭐  |
| SSH                    | ⭐⭐⭐⭐⭐  |
| Cron                   | ⭐⭐⭐⭐   |
| AWS CLI                | ⭐⭐⭐⭐⭐  |
| Docker + Bash          | ⭐⭐⭐⭐   |

---

## 📈 Progress

This repository is continuously updated as I progress through my Linux and Bash learning journey.

The focus is on building practical knowledge through exercises and projects rather than simply memorizing commands.

Each new section will reflect the concepts explored and the skills developed throughout the learning process.

**Learning path:**

```text
Linux Fundamentals
        ↓
System Administration
        ↓
Bash Fundamentals
        ↓
Automation
        ↓
Cloud Integration
        ↓
Server Operations Toolkit
```

---

> **Note:** This repository is a living learning project and will continue to evolve as I progress through Linux, Bash, automation, and Cloud Engineering concepts.
