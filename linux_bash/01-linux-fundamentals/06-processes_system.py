# 5.7 — `top` vs `ps`
# Before we move to background jobs and `systemctl`, let's make sure you understand the tools we've seen.
#
# | Command | Main purpose                         |
# |---------|--------------------------------------|
# | `ps`    | Snapshot of processes                |
# | `ps aux`| Detailed snapshot of system processes |
# | `pgrep` | Find PIDs by process name            |
# | `top`   | Real-time process monitoring         |
# | `kill PID` | Stop a specific process           |
# | `pkill name` | Stop processes by name          |
#
# ## Exercise 6 🧪 — Choose the right command
#
# For each situation, choose the **best command**:
#
# ### 1.
#

You want to see all running processes with CPU and memory usage.

**A.** `pgrep`

**B.** `ps aux`

**C.** `kill`

B -> ps aux

# ### 2.

You want to continuously monitor CPU usage in real time.

**A.** `top`

**B.** `ps`

**C.** `pkill`

A -> top

# ### 3.

You know the PID is `4521` and want to terminate exactly that process.

**A.** `pkill 4521`

**B.** `kill 4521`

**C.** `pgrep 4521`

B -> kill 4521

# ### 4.

You want to find the PIDs of processes named `nginx`.

**A.** `pgrep nginx`

**B.** `kill nginx`

**C.** `top nginx`

A -> pgrep nginx


# 5.8 — Background & Foreground Processes
# The next important concept is understanding **foreground vs background** processes.
#
# When you run:
#
# sleep 30
#
# your terminal is occupied for 30 seconds.
#
# The command is running in the **foreground**.
#
# You can't use that terminal normally until it finishes.
#
# You can press:
#
# Ctrl + C
#
# to interrupt it.
#
# ---
#
# ## Running a command in the background
#
# Add `&`:
#
# sleep 30 &
#
# Now Linux starts the process in the **background**.
#
# You'll typically see something like:
#
# [1] 5234
#
# Where:
#
# - `[1]` → **job number**
# - `5234` → **PID**
#
# Your terminal is immediately available again.
#
# You can run:
#
# ps
#
# and potentially see the `sleep` process.
#
# ---
#
# ## `jobs`
#
# To see background jobs belonging to your current shell:
#
# jobs
#
# Example:
#
# [1]+  Running    sleep 30 &
#
# ---
#
# ## `fg`
#
# To bring a background job back to the foreground:
#
# fg %1
#
# Here `%1` means **job number 1**, not PID 1.
#
# This distinction is important:
#
# %1    → job number
# 5234  → PID
#
# ---
#
# ## Exercise 7 🧪
#
# Suppose you run:
#
# sleep 60 &
#
# and Linux responds:
#
# [1] 5234
#
# Answer:

**1.** What is the **job number**?
job number is 1


**2.** What is the **PID**?

5234

**3.** What command would show your background jobs?

jobs

**4.** What command would bring job 1 back to the foreground?

fg %1

**5.** Is `%1` the PID or the job number?

`%1` is job number


# 5.9 — `Ctrl + Z`, `bg`, and `fg`
# Let's continue with **job control**.
#
# Suppose you start:
#
# sleep 60
#
# The command runs in the **foreground**.
#
# ### `Ctrl + Z`
#
# Pressing:
#
# Ctrl + Z
#
# does **not** kill the process.
#
# It **pauses/stops** the foreground process.
#
# You may see:
#
# [1]+  Stopped    sleep 60
#
# The job still exists.
#
# ---
#
# ### `bg`
#
# Now you can resume the stopped job **in the background**:
#
# bg %1
#
# The process continues running, but your terminal is available again.
#
# You can check:
#
# jobs
#
# and see:
#
# [1]+  Running    sleep 60 &
#
# ---
#
# ### `fg`
#
# You can bring it back to the foreground:
#
# fg %1
#
# So the complete flow is:
#
# sleep 60
#     ↓
# Ctrl + Z
#     ↓
# Stopped
#     ↓
# bg %1
#     ↓
# Running in background
#     ↓
# fg %1
#     ↓
# Foreground
#
# ### ⚠️ Important distinction
#
# Ctrl + C
#
# ➡️ **terminates/interupts** the foreground process.
#
# Ctrl + Z
#
# ➡️ **stops/pauses** the foreground process.
#
# They are **not the same**.
#
# ---
#
# # 🧪 Exercise 8
#
# Imagine you run:
#
# sleep 120
#
# Then you press:
#
# Ctrl + Z
#
# Linux responds:
#
# [1]+  Stopped    sleep 120
#
# Answer:
#
**1.** Did the process get terminated?

No just stopped/paused

**2.** What command would resume job 1 in the background?

bg %1

**3.** What command would bring job 1 back to the foreground?

fg %1

**4.** What is the difference between `Ctrl + C` and `Ctrl + Z`?

The fist terminate (kill) the foreground process while the second
just pauses it


# 5.10 — `systemctl`: Managing Services
# Now we move from individual processes to **services**.
#
# A **service** is a program designed to run in the background and provide functionality to the system or other applications.
#
# Common examples:
#
# nginx       → web server
# ssh         → remote access
# docker      → container runtime
# postgresql  → database
#
# On modern Debian systems, services are commonly managed by **systemd**.
#
# The main command is:
#
# systemctl
#
# For example:
#
# systemctl status ssh
#
# This asks:
#
# > What is the current status of the SSH service?
#
# You might see:
#
# ● ssh.service - OpenBSD Secure Shell server
#      Loaded: loaded
#      Active: active (running)
#
# The important part is:
#
# Active: active (running)
#
# which means the service is currently running.
#
# You can also use:
#
# systemctl is-active ssh
#
# which gives a simpler result:
#
# active
#
# ---
#
# ## Cloud/DevOps perspective ☁️
#
# Imagine your application is unreachable.
#
# You could investigate:
#
# Application
#     ↓
# Is the process running?
#     ↓
# Is the service running?
#     ↓
# Is the server healthy?
#     ↓
# Is the network working?
#
# `systemctl` becomes particularly useful when your application depends on services such as **Nginx, SSH, Docker, or a database**.
#
# ---
#
# # 🧪 Exercise 9
#
# Suppose you run:
#
# systemctl status nginx
#
# and get:
#
# ● nginx.service
#      Loaded: loaded
#      Active: active (running)
#
# Answer:
#

**1.** Is the nginx service running?

Yes the nginx service is running


**2.** What does `systemctl status nginx` allow you to check?

`systemctl status nginx` allow me to check the current running
status of nginx service

**3.** What command would give you the simpler `active` / `inactive` result?

`systemctl  is-active nginx`

**4.** What is the difference between a **process** and a **service**?

A service is a program design to run OS (app, feature...) while
a process is just one of a running instance of the service
