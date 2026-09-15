
======================================================================

1.8 — Linux Logs 📋

======================================================================


Now we move to logs, one of the most important skills for a Cloud/DevOps
engineer.

When something goes wrong on a server, you often follow this logic:

Service failed
    ↓
systemctl status
    ↓
Why did it fail?
    ↓
journalctl
    ↓
Find the error
    ↓
Fix it

=======================================================================

1. What is a log?



A log is a record of something that happened in the system or an application.

For example:

Application started
Connection established
User authenticated
Database connection failed
Port already in use
Process crashed

A real server can generate thousands or millions of log entries.



2. journalctl


On a system using systemd, logs are collected by the systemd journal.

You can inspect them with:

journalctl

This can produce a lot of output.

So we usually filter it.




3. Show the latest logs

journalctl -n 20

Meaning:

-n 20
   ↓
show the last 20 entries

You can also do:

journalctl -n 50


4. Logs for a specific service


This is extremely important.

journalctl -u nginx

-u means unit.

So:

journalctl -u nginx

means:

Show me the journal logs associated with the nginx service.

You can combine options:

journalctl -u nginx -n 20

Meaning:

Show me the last 20 nginx log entries.


5. Follow logs in real time

This is very useful when troubleshooting an application.

journalctl -u nginx -f

-f means follow.

It behaves similarly to:

tail -f

The terminal stays open and waits for new logs.

For example:

Sep 09 22:41:01 server nginx[1200]: Started
Sep 09 22:41:10 server nginx[1200]: Request received
Sep 09 22:41:12 server nginx[1200]: Connection error
                                           ↑
                                      new log

When a new event happens, it appears automatically.

Press:

Ctrl + C

to stop following.


6. Logs since a specific time

You can also filter by time.

For example:

journalctl --since "1 hour ago"

Or:

journalctl --since today

And for a service:

journalctl -u nginx --since "1 hour ago"

This is extremely useful when someone tells you:

"The application stopped working about 30 minutes ago."

You don't need to search through yesterday's logs.




7. A very common troubleshooting workflow


Imagine your Node.js application is running as a systemd service called myapp.

A user tells you:

"The website is down."

You could investigate like this:

Step 1 — Check the service

systemctl status myapp

You discover:

Active: failed


Step 2 — Check the logs

journalctl -u myapp -n 50

You discover:

Error: Cannot connect to database


Step 3 — Investigate further

Now you know the problem probably isn't:

CPU

or:

RAM

but rather:

Application → Database connection

That's the kind of reasoning you need as a Cloud/DevOps engineer.


======================================================================


🎯 Your exercise

Run these commands in your Debian WSL:

journalctl -n 20

Then:

journalctl --since "1 hour ago"

Then:

journalctl -b
What does -b mean?

Don't look it up yet. Try to reason about it from the meaning of logs and system startup.

Then answer these 4 questions:

What does journalctl -n 20 do?

-> display the last 20 journal entries


What does journalctl -u nginx do?

-> display nginx services logs


What does journalctl -f do?

-> follow and display real time logs 


What do you think journalctl -b does?

-> display journal entrie from current boot


==================================================================


Remember these four

Command	                Meaning

journalctl -n 20	    Last 20 journal entries

journalctl -u nginx	    Logs for nginx service

journalctl -f	        Follow logs in real time

journalctl -b	        Logs from current boot



Next concept: finding the actual error

Knowing how to display logs is only half the job.

As a Cloud/DevOps engineer, the important question is:

How do I find the line that explains why something failed?

We'll practice commands such as:

journalctl -u myapp | grep -i error

and learn how to recognize common problems like:

Permission denied
Connection refused
Address already in use
No such file or directory
Failed to start

That will turn journalctl from a simple log viewer into a
troubleshooting tool.
