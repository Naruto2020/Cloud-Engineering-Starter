
=====================================================================

5.12 — journalctl: Reading Service Logs

=====================================================================


The next tool is extremely important for troubleshooting Linux servers:

journalctl

journalctl reads logs collected by systemd's journal.

For example:

sudo journalctl -u nginx

means:

Show the logs for the nginx service.

You might see:

Sep 11 10:15:02 server nginx[1024]: Starting nginx
Sep 11 10:15:03 server nginx[1024]: Configuration loaded
Sep 11 10:20:15 server nginx[1024]: Reloading configuration


Useful combinations

Logs for a specific service

sudo journalctl -u nginx

Only recent logs

sudo journalctl -u nginx -n 20

-n 20 → show the last 20 log entries.


Follow logs live

sudo journalctl -u nginx -f


This is similar to:

tail -f app.log

It continuously displays new log entries.

Logs since the current boot

sudo journalctl -u nginx -b


🧠 Your troubleshooting toolkit is becoming complete

You can now combine several commands:

systemctl status nginx
        ↓
Is the service running?

journalctl -u nginx
        ↓
What happened?

ps aux
        ↓
What processes are running?

top
        ↓
Is something consuming CPU/RAM?

pgrep nginx
        ↓
What are the nginx PIDs?

This is exactly the kind of reasoning you'll use when 
troubleshooting a cloud server.


🧪 Exercise 11

Imagine nginx is not working.

You run:

systemctl status nginx

and see:

Active: failed

You want to investigate why nginx failed.

Questions

1. What command would you use to see nginx's logs?

==> journalctl -u nginx 


2. What command would show only the last 20 nginx log entries?

==> journalctl -u nginx -n 20


3. What command would let you follow nginx logs live?

==> journalctl -u nginx -f


4. If systemctl status nginx says failed, does that automatically
tell you why it failed? Explain briefly.

==> No if systemctl status nginx only give service status to investigate
on faill you have to go check logs  first


5.13 — A realistic troubleshooting scenario


Let's combine what you've learned so far.

Imagine you deploy an application on a Linux server. Users report:

"The application is down."

You investigate:

systemctl status nginx

and get:

Active: active (running)

So nginx itself is running.

You then check the processes:

ps aux | grep python

and find:

steve    4521  95.0  2.1  ... python app.py

The Python process is consuming 95% CPU.

You then check:

top

and confirm that python is the main CPU consumer.

Finally, you inspect the application logs.

This illustrates an important DevOps principle:

Don't immediately kill a process just because it uses a lot of CPU. Investigate first.

High CPU could be caused by:

an infinite loop
a traffic spike
a bad query
a memory/CPU-intensive operation
a bug
a legitimate workload


🧪 Exercise 12 — Troubleshooting

You have this situation:

systemctl status nginx
→ active (running)

ps aux
→ python app.py → 98% CPU

top
→ python app.py → 98% CPU

journalctl -u nginx
→ no errors

The application is still slow.

What would you do first?

A.

kill -9 <python-PID>

B.

Investigate the Python application's own logs and determine why it is consuming 98% CPU.

5.13 — A realistic troubleshooting scenario

Let's combine what you've learned so far.

Imagine you deploy an application on a Linux server. Users report:

"The application is down."

You investigate:

systemctl status nginx

and get:

Active: active (running)

So nginx itself is running.

You then check the processes:

ps aux | grep python

and find:

steve    4521  95.0  2.1  ... python app.py

The Python process is consuming 95% CPU.

You then check:

top

and confirm that python is the main CPU consumer.

Finally, you inspect the application logs.

This illustrates an important DevOps principle:

Don't immediately kill a process just because it uses a lot of CPU. Investigate first.

High CPU could be caused by:

an infinite loop
a traffic spike
a bad query
a memory/CPU-intensive operation
a bug
a legitimate workload
🧪 Exercise 12 — Troubleshooting

You have this situation:

systemctl status nginx
→ active (running)

ps aux
→ python app.py → 98% CPU

top
→ python app.py → 98% CPU

journalctl -u nginx
→ no errors

The application is still slow.

What would you do first?

A. kill -9 <python-PID>

B. Investigate the Python application's own logs and determine 
why it is consuming 98% CPU.

C. Restart the entire server.

Choose A, B, or C and explain why.C.

==> B because kill the process or restart entire server ll not
let me know why application is slow
