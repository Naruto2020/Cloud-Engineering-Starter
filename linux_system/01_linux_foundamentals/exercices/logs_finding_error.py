
====================================================================

1.8 — Linux Logs: Finding Errors 🔎

====================================================================



Now let's move from "how to read logs" to "how to troubleshoot with logs."

Imagine a service has failed:

systemctl status myapp
        ↓
Active: failed

The next question is:

Why did it fail?

That's where journalctl becomes really useful.


1. Search for errors with grep

You can combine commands:

journalctl -u nginx | grep -i error


Here:


journalctl -u nginx
        ↓
get nginx logs
        ↓
grep -i error
        ↓
keep lines containing "error"


What does -i mean?

It makes the search case-insensitive.

So it finds:

error
ERROR
Error
ErRoR


2. Search for failed

Another useful command:

journalctl -u nginx | grep -i failed

Or:

journalctl -u nginx | grep -i "connection refused"

This can quickly reveal the important part of a large log.



3. Common errors you should recognize

Permission denied
Permission denied

Usually means:

The process doesn't have the required permission to access a file, directory, socket, etc.

Potential causes:

wrong file permissions
wrong owner
wrong service user


Address already in use
bind(): Address already in use

Usually means:

Another process is already using that port.

For example:

myapp → wants port 3000
         ↓
port 3000 already occupied
         ↓
myapp fails

You could investigate with:

ss -tulpn

Connection refused
connect() failed: Connection refused

Usually means:

Your application tried to connect to something, but nothing was
accepting the connection at that address/port.

For example:

API
 ↓
Database :5432
 ↓
Connection refused

Possible causes include:

database isn't running

wrong port

wrong IP/hostname

firewall/network issue

No such file or directory

No such file or directory

Usually means the application expected a file, directory, executable, 
or path that doesn't exist.



4. A very useful command

You can combine -u, -n, and grep:

journalctl -u nginx -n 100 | grep -i error

Meaning:

Look at the last 100 nginx journal entries and show me the ones containing "error", regardless of capitalization.

This is much more practical than reading hundreds of lines manually.



🎯 Practical exercise

Let's test your understanding.

A- Imagine you run:

journalctl -u myapp -n 50

and see:

Sep 12 22:10:01 server myapp[1200]: Starting application
Sep 12 22:10:02 server myapp[1200]: Connecting to database
Sep 12 22:10:02 server myapp[1200]: Connection refused
Sep 12 22:10:02 server myapp[1200]: Application failed
Sep 12 22:10:02 server systemd[1]: myapp.service: Main process exited

Answer these:

1. What is the most likely root problem?

-> Connection to database


2. Is systemd itself necessarily the problem?

-> Not quiet sure that the system is the problem
i will investigate on link with database


3. What command could you use to search specifically for errors?

-> journalctl -u myapp -n 50 | grep -Ei "error|failled|refused"


4. If the application wants to connect to PostgreSQL on port 5432,
what command could you use to check whether something is listening on
that port?

ss -tulpn | grep :5432

B- Suppose you run:

systemctl status myapp

and get:

Active: failed

Then:

journalctl -u myapp -n 20

shows:

Error: EACCES: permission denied, open '/var/log/myapp/app.log'

Question: What do you investigate first?

A. CPU usage
B. RAM usage
C. File permissions / ownership
D. Network ports

-> C File permissions / ownership

And which Linux command(s) would you use to investigate it?

-> ls -ld /var/log/myapp
   ls -l /var/log/myapp/app.log
   systemctl cat myapp
   id "username"


Then compare:

Service user
     ↓
     steve

Directory owner/permissions
     ↓
     ?

File owner/permissions
     ↓
     ?



