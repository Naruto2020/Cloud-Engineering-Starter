# ============================================================
# 1.6 — Linux Services and `systemd`
# ============================================================

# So far, we have started applications manually:
#
# node app.js

# The problem is that on a real server, we do not necessarily
# want to open a terminal and start the application manually.

# We want Linux to be able to:
#
# - start the application automatically;
# - monitor it;
# - restart it if necessary;
# - manage its logs;
# - stop it cleanly;
# - run it as a specific user.
#
# This is one of the main roles of `systemd`.


# ============================================================
# 1. What is `systemd`?
# ============================================================

# On many modern Linux distributions:
#
# Linux
#   │
#   └── systemd
#         │
#         ├── nginx
#         ├── ssh
#         ├── cron
#         └── other services

# `systemd` is, among other things, the init system
# and service manager.

# You can check PID 1 with:
#
# ps -p 1 -f

# On a system using `systemd`, you will generally see
# `systemd` or an init process associated with `systemd`.


# ============================================================
# 2. Service vs Process
# ============================================================

# This is an important distinction.

# A process:
#
# node app.js
#     ↓
# PID 1234
#
# is an instance of a program that is currently running.

# A service represents an application or functionality
# that the system is responsible for managing.

# For example:
#
# Service: nginx
#       ↓
# nginx process
#       ↓
# PID(s)

# So:
#
# The service is managed by systemd;
# the service runs one or more processes.


# ============================================================
# 3. First Command: `systemctl`
# ============================================================

# The main command used to interact with systemd is:
#
# systemctl

# To check the status of a service:
#
# systemctl status nginx

# You can try this with a service available on your machine.

# Start by listing all currently loaded services:
#
# systemctl list-units --type=service

# You will see a list similar to:
#
# UNIT                     LOAD   ACTIVE   SUB
# ssh.service              loaded active   running
# systemd-journald.service loaded active   running
# ...

# ============================================================
# 4. `active`, `inactive`, `failed`
# ============================================================

# A service can be in several states, including:
#
# active
# inactive
# failed

# For example:
#
# nginx.service
#     ↓
# active (running)
#
# means that the service is currently running.

# On the other hand:
#
# nginx.service
#     ↓
# failed
#
# means that there was a problem with the service.


# ============================================================
# 5. Essential Commands
# ============================================================

# You should know these commands:

# Check the status:

systemctl status nginx

# Start a service:

sudo systemctl start nginx

# Stop a service:

sudo systemctl stop nginx

# Restart a service:

sudo systemctl restart nginx

# Enable a service to start automatically at boot:

sudo systemctl enable nginx

# Disable a service from starting automatically at boot:

sudo systemctl disable nginx


# ============================================================
# 6. Logs
# ============================================================

# And now we reach another essential element.

# You run:
#
# systemctl status nginx
#
# and you see:
#
# Active: failed

# The next question is immediately:
#
# Why?

# You are going to check the logs.

# With systemd:
#
# journalctl

# For a specific service:
#
# journalctl -u nginx

# To follow new logs in real time:
#
# journalctl -u nginx -f

# The `-f` means "follow".

# Conceptually, this is similar to:
#
# tail -f


# ============================================================
# 🧠 The Cloud Engineer Mindset
# ============================================================

# Imagine this situation:
#
# User
#     ↓
# Load Balancer
#     ↓
# Server
#     ↓
# Node.js
#     ↓
# ❌

# You do not immediately start modifying the code.

# You diagnose the problem step by step:
#
# 1. Is the machine working?
#        ↓
# 2. Does the process exist?
#        ↓
# 3. Is the service active?
#        ↓
# 4. Is the port listening?
#        ↓
# 5. What do the logs say?
#        ↓
# 6. What about CPU / RAM?
#        ↓
# 7. What about the network?

# The tools start fitting together:
#
# ps
#  ↓
# processes
#
# systemctl
#  ↓
# services
#
# journalctl
#  ↓
# logs
#
# top
#  ↓
# CPU / RAM
#
`Restart=on-failure`# ss
#  ↓
# ports / sockets

# This combination is what starts building
# real Linux / Cloud engineering skills.

# ============================================================
# 🎯 Questions
# ============================================================

# Before going further, answer these 6 questions:

1. What is the difference between a process and a service?

A service is an application or feature  on my OS
While a process is a running instance of a service


2. What does `systemctl start nginx` do?

`systemctl start nginx` will starts nginx service immediatly


3. What is the difference between `start` and `enable`?
Starts will launch directly a service
While enable will prepare it to be launch when OS restart


4. What is `systemctl status` used for?
`systemctl status` is use to know the service status 
(start, stop, running, PID, logs, error... )


5. What is `journalctl` used for?
`journalctl` is use to view logs

6. Why is `Restart=on-failure` useful on a server?
`Restart=on-failure` is useful because it help to restart
a server automaticaly if it crashes or exit with an error

# ============================================================
# Next Step
# ============================================================

# Next, we will study Linux logs in depth.
#
# After that, we will be able to complete
# the Linux fundamentals block.
