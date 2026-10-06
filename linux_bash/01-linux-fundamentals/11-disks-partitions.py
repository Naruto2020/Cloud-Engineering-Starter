
================================================================

5.16 — Disks, Partitions & lsblk

================================================================


When troubleshooting a Linux server, df tells you about filesystems, but sometimes you need to understand the underlying disks 
and partitions.

That's where lsblk comes in.

1. lsblk

Run: lsblk

Example:

NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda      8:0    0   50G  0 disk
├─sda1   8:1    0   49G  0 part /
└─sda2   8:2    0    1G  0 part [SWAP]

Think of the hierarchy like this:

Physical disk
    │
    ├── Partition
    │
    └── Partition

In this example:

sda → the disk, 50G
sda1 → a partition, 49G, mounted at /
sda2 → a partition, 1G, used for swap
TYPE tells you whether something is a disk, part, etc.
MOUNTPOINTS tells you where a filesystem is attached.


2. Why is this useful?

Imagine: df -h

shows: /dev/sda1   49G   47G   2G   96%   /

You know the filesystem / is nearly full.

Then: lsblk

helps you understand the underlying storage structure.

This becomes especially useful with cloud VMs when you attach 
additional storage. For example:

sda   50G
sdb  100G

You can identify that the server has another disk available, but it
isn't necessarily mounted or usable yet.

3. Important distinction

Keep these three concepts separate:

Command	Main question
df -h	How full are my filesystems?
du -sh	What files/directories use the space?
lsblk	What disks and partitions exist?

A useful mental model:

lsblk
  ↓
Disks / partitions
  ↓
Filesystem
  ↓
df -h
  ↓
Files/directories
  ↓
du


Exercise 16

Given:

NAME    SIZE TYPE MOUNTPOINTS
sda      80G disk
├─sda1   78G part /
└─sda2    2G part [SWAP]
sdb     100G disk

Answer:

1. How many disks are present?
2. What is the size of sda?
3. Which partition is mounted as /?
4. Which partition is used for swap?
5. Is sdb currently shown as mounted to a filesystem?
6. Which command would you use to check how much space is available
on /?

Your turn.

1. 2 disks are present.
2. sda size is 80G
3. sda1 is the partition which is mounted as /
4. sda2 is use for swap
5. No
6. df -h /

================================================================

5.17 — Practical Resource Troubleshooting

Let's combine what you've learned instead of introducing another 
command.

Imagine you're responsible for a production Linux server. Users 
report:

"The application is very slow."

You investigate and collect:

CPU

top

%Cpu(s): 96.5 us, 1.2 sy, 0.0 ni, 2.0 id

Memory

free -h

               total   used   free   buff/cache   available
Mem:             8Gi    7Gi    150Mi    850Mi        600Mi
Swap:            2Gi    1.8Gi  200Mi

Disk

df -h /

Filesystem      Size  Used  Avail  Use%
/dev/sda1        50G   49G    1G    98%


Processes

ps aux --sort=-%cpu | head

USER      PID  %CPU  %MEM  COMMAND
app      4521  91.2   12.5 python app.py
mysql    2100   3.1   18.2 mysqld
root     1200   1.0    1.2 systemd


Exercise 17 — Troubleshooting

Based on all four outputs, answer:

What resource has the most obvious CPU problem?
What process is responsible for most of the CPU usage?
Is the server also experiencing memory pressure? Explain briefly.
Is the disk usage concerning? Why?
Before simply restarting the Python application, what would you 
investigate?


1. python app
2. PID = 4521 ->  python app.py → 91.2% CPU
3. Yes. Because  available = 600 Mi on 8 GiB is quite low
   and swap: 1.8Gi / 2Gi
4. Yes because Filesystem      Size  Used  Avail  Use%
   /dev/sda1        50G   49G    1G    98%
5. I ll investigate why the application is consuming so much CPU
   command : top , journalctl -u app ; tail -n 50 app.log ...

================================================================

Step 5 — Final Review Exercise

Let's do one final scenario covering the commands and concepts from
this step.

A production server has become slow. You run:

ps aux --sort=-%cpu | head

USER      PID   %CPU  %MEM  COMMAND
app      4521   88.5   10.2  python app.py
mysql    2100    4.2   22.1  mysqld
root     1200    0.8    1.1  systemd

Then:

free -h
               total   used   free   buff/cache   available
Mem:             8Gi    7Gi    180Mi    820Mi        700Mi
Swap:            2Gi    1.7Gi  300Mi

And:

df -h /

Filesystem      Size  Used  Avail  Use%
/dev/sda1        50G   48G    2G    96%

Finally: systemctl status nginx

shows:

Active: active (running)

Your questions

1. Which process is consuming the most CPU?
2. What is its PID?
3. Is nginx currently running?
4. Is there evidence of memory pressure? Give two pieces of evidence.
5. Is the root filesystem getting dangerously full?
6. Give me three commands you would use to investigate this server 
   further.
7. Would you immediately run kill -9 4521? Why or why not?


1. PID: 4521 -> %CPU 88.5  python app.py
2. PID: 4521
3. Yes
4. Yes there is evidence of memory pressure -> available 700Mi 
   on 8Gi and swap: 1.7Gi / 2Gi
5. Yes -> /dev/sda1        50G   48G    2G    96%
6. top , journalctl -u nginx , du -sh /*
7. No i ll investigate first why this process it is consuming too
   much CPU -> top ; journalctl ; tail -n 50 journal.log
