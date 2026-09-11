# Step 5 — Processes & System ⚙️
# Now we move to **Linux processes**, a very important topic for Cloud/DevOps work.
#
# ## 5.1 — What is a process?
#
# A **process** is a program that is currently running.
#
# For example:
#
# Program                         Process
# -----------------------------------------------
# python app.py          →        running Python process
# nginx                  →        running nginx process
# docker                 →        running Docker process
# bash                   →        your current shell process
#
# Every running process has a unique **PID**:
#
# > **PID = Process ID**
#
# Example:
#
# PID    COMMAND
# 1234   python
# 2456   nginx
# 3012   bash
#
# The PID is useful because you can use it to inspect or stop a process.
#
# ---
#
# ## 5.2 — `ps`
#
# The simplest command is:
#
# ps
#
# It shows processes associated with your current shell.
#
# Example:
#
#     PID TTY          TIME CMD
#    4210 pts/0    00:00:00 bash
#    4382 pts/0    00:00:00 ps
#
# Here:
#
# - `4210` → PID of `bash`
# - `4382` → PID of `ps`
# - `CMD` → command/program
#
# Notice something interesting: **`ps`** **itself appears as a process** because it is running while Linux collects the information.
#
# ---
#
# ## 5.3 — `ps aux`
#
# For system administration, you'll often use:
#
# ps aux
#
# This gives you a much larger list of running processes.
#
# You'll see columns such as:
#
# USER       PID  %CPU  %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# steve     4210   0.0   0.1  ...    ... pts/0    Ss   ...      ... bash
# root      1023   0.2   0.5  ...    ... ?       S    ...      ... nginx
#
# Important columns:
#
# - `USER` → who owns the process
# - `PID` → process ID
# - `%CPU` → CPU usage
# - `%MEM` → memory usage
# - `COMMAND` → command/program
#
# This is extremely useful when troubleshooting a server.
#
# ---
#
# # Exercise 1 🧪
#
# Run these commands in your Debian WSL terminal:
#
# ps
#
# then:
#
# ps aux
#
# Then answer these **without worrying about every column yet**:
#
# ### Questions
#

**1.** What does the PID represent?

PID = unique Process ID

**2.** In `ps aux`, what does `%CPU` tell you?

`%CPU`  -> CPU usage

**3.** In `ps aux`, what does `%MEM` tell you?

`%MEM` -> Memory usage

**4.** If you see:

steve    4521   0.0   0.2   ...   python app.py

what is the PID of `python app.py`?

4521


# 5.3 — Find a process with `pgrep`
# Now imagine you have many processes:
#
# ps aux
#
# and you want to find only the processes related to **Python**.
#
# Instead of searching manually, you can use:
#
# pgrep python
#
# This returns the PIDs of processes whose name matches `python`.
#
# For example:
#
# 4521
# 4788
#
# You can also use:
#
# pgrep -a python
#
# The `-a` option shows the **PID + command**:
#
# 4521 python app.py
# 4788 python worker.py
#
# This is very useful in cloud/server troubleshooting.
#
# ### Exercise 2 🧪
#
# Suppose you run:
#
# pgrep -a nginx
#
# and get:
#
# 1024 nginx: master process /usr/sbin/nginx
# 1031 nginx: worker process
# 1032 nginx: worker process
#
# Answer:
#

**1.** How many nginx processes are running?

3 nginx process are running

**2.** What is the PID of the nginx master process?

1024

**3.** What are the PIDs of the worker processes?

1031 ; 1032


# 5.4 — Monitoring processes with `top`
# `ps` gives you a **snapshot** of processes.
#
# But what if you want to watch them **in real time**?
#
# That's where `top` comes in:
#
# top
#
# It continuously updates information such as:
#
# - CPU usage
# - memory usage
# - running processes
# - process IDs
# - system load
#
# You'll see something similar to:
#
# PID    USER     %CPU   %MEM   COMMAND
# 4521   steve     85.2    2.1   python
# 1024   root       2.3    0.8   nginx
# 3012   steve       0.5    0.3   bash
#
# If a Python process suddenly consumes **85% CPU**, `top` lets you spot it quickly.
#
# ### Important
#
# To exit `top`, press:
#
# q
#
# ---
#
# ## Exercise 3 🧪
#
# Imagine `top` shows:
#
# PID    USER    %CPU    %MEM    COMMAND
# 1200   root     92.5     1.2   python
# 1400   root      3.1     8.5   postgres
# 1500   steve     1.0     0.5   nginx
#
# Answer:

**1.** Which process is consuming the most CPU?

Python is consuming the most CPU = 92.5%

**2.** Which process is consuming the most memory?

Postgres is consuming the most memory = 8.5%

**3.** What is the PID of the Python process?

1200

**4.** If you are investigating a CPU problem, which
process would you investigate first?

Python -> CPU -> 92.5%


# 5.5 — Stopping a process with `kill`
# Now we have found a process consuming too many resources.
#
# Suppose:
#
# PID    COMMAND
# 1200   python
#
# Linux allows us to send a signal to that process:
#
# kill 1200
#
# By default, `kill` sends **SIGTERM**.
#
# Think of it as:
#
# > "Please stop gracefully."
#
# If the process refuses to stop, you can use:
#
# kill -9 1200
#
# `-9` sends **SIGKILL**:
#
# > "Stop immediately."
#
# ⚠️ In real server administration, **prefer** **`kill PID`** **first**.
# Use `kill -9` only when necessary because the process doesn't get a chance
# to shut down cleanly.
#
# ---
#
# ## Exercise 4 🧪
#
# You have this process:
#
# PID    USER    %CPU    COMMAND
# 4521   steve     95.0   python app.py
#
# You want to stop it.
#
# ### Questions
#

**1.** What command would you try first?

KILL  4521

**2.** The process doesn't stop. What command could you use as a 
last resort?

KILL -9 4521


**3.** What does the `-9` mean in `kill -9 4521`?

The `-9` send a SIGKILL to stop immediatly the process


# 5.6 — `pkill`: Kill by process name
# So far, we've used the PID:
#
# kill 4521
#
# But sometimes you don't know the PID.
#
# For example, you want to stop a process named `python`.
#
# You can use:
#
# pkill python
#
# This tells Linux:
#
# > Find processes matching `python` and terminate them.
#
# You can also use:
#
# pkill -9 python
#
# to send SIGKILL.
#
# ⚠️ Be careful: `pkill python` can affect **multiple Python processes**.
#
# For example:
#
# 4521 python app.py
# 4788 python worker.py
# 4910 python backup.py
#
# Running:
#
# pkill python
#
# could terminate **all three**.
#
# That's why using a specific PID with `kill` is often safer.
#
# ---
#
# ## Exercise 5 🧪
#
# You have:
#
# 4521 python app.py
# 4788 python worker.py
# 5010 nginx
#

You want to stop **only** **`python app.py`**.
Which is safer?

**A**

pkill python

**B**

kill 4521

And explain **why**.

kill 4521 is safer , Because it send signal to terminate
a process using it PID (unique)
While pkill  send signal to terminate a process using process name
wich can be one intance between many python instance
