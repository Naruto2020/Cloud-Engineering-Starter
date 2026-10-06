
=======================================================================

		6.3 — RAM: free -h

=======================================================================


Before the command, the important idea is:

High RAM usage does not automatically mean a memory problem.

Linux deliberately uses unused RAM for things like filesystem cache. What matters more is how much memory is actually available and whether the system is actively relying on swap.

1. The command
free -h

Example:

               total        used        free      shared  buff/cache   available
Mem:            16Gi        12Gi       500Mi       300Mi       3.5Gi       4.0Gi
Swap:            2Gi        1.0Gi       1.0Gi

Let's understand each important column.

Column	Meaning
total	Total RAM
used	RAM currently in use
free	Completely unused RAM
buff/cache	RAM used for buffers/cache
available	RAM Linux estimates it can make available for applications
Swap used	RAM pages currently stored in swap
2. Why free can be misleading

Imagine:

total:       16 Gi
used:        12 Gi
free:       500 Mi
available:    4 Gi

At first glance:

"Only 500 MiB is free! RAM is almost finished!"

Not necessarily.

Linux can reclaim much of the 3.5 GiB cache when applications need memory.

That's why:

available: 4 Gi

is much more useful for judging whether you're actually running out of RAM.

3. What is swap?

Swap is disk space used as an extension of memory.

Very simplified:

RAM
 ↓
fast

Swap
 ↓
much slower

If the system doesn't have enough RAM, Linux can move some memory pages to swap.

Some swap usage is not automatically a problem.

But if the machine is constantly moving data:

RAM ↔ Swap ↔ RAM ↔ Swap

that can cause serious performance degradation.

This is called swapping / memory pressure.


4. Cloud-engineering mindset

When investigating a slow server, don't say:

"RAM is 80% used, therefore RAM is the problem."

Instead ask:

How much RAM is available?
Is swap being used?
Is swap usage significant?
Is the system actively under memory pressure?
What process is consuming the RAM?

This is the same troubleshooting mindset we used with CPU.

Exercise 20

You run:

free -h

and get:

               total        used        free      shared  buff/cache   available
Mem:            16Gi        13Gi       400Mi       200Mi       3.6Gi       3.8Gi
Swap:            2Gi        1.6Gi       400Mi

Answer one question at a time, starting with:

Q1. Is 400Mi of free RAM by itself enough to conclude that the server 
is running out of memory? Why or why not?

==> No the most important output is available => 3.8Gi linux sometime
used part of memory for cache

Q2

Look again at:

Swap:  2Gi  1.6Gi  400Mi

Is the 1.6Gi of swap usage automatically a problem? Why or why not?

==> No because some pages have been moved to swap because were inactive


Q3

Given the whole output:

Mem:   16Gi  13Gi  400Mi  200Mi  3.6Gi  3.8Gi
Swap:   2Gi  1.6Gi  400Mi

Would you say the server is:

A. Definitely out of RAM
B. Definitely healthy
C. Possibly under memory pressure, and we should investigate further

Which one, and why?

==> C  

Available: 3.8 GiB → there is still a reasonable amount available.
Swap used: 1.6 GiB / 2 GiB → quite significant, so we should investigate.
Free: 400 MiB → low, but not enough by itself to prove a problem.
Cache: 3.6 GiB → some memory can be reclaimed.

There are signs that memory pressure may exist, but we need more 
evidence before declaring RAM exhaustion.

Q4

If you wanted to find which process is consuming the most RAM, which 
command would you use?

==> top for real time  ; ps aux sort=-%mem | head ; 


Suppose you run it and get:

USER       PID  %CPU  %MEM  COMMAND
steve     4521   5.2  42.5  python app.py
mysql     2100   2.1  18.3  mysqld
root      1200   1.0   5.2  nginx

Which process should you investigate first for memory usage, and 
approximately how much RAM is it consuming relative to the system?


==> 4521   5.2  42.5  python app.py


Q6 — Final RAM question

You now know:

available RAM: 3.8 GiB
swap used:     1.6 GiB
python app:   42.5% RAM

What would be your next step as a Cloud Engineer?

A. Immediately kill -9 4521
B. Investigate the Python application's logs and behavior
C. Immediately reboot the server

==> B 
