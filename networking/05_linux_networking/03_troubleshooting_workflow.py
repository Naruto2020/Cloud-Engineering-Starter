
===============================================================

Linux Networking — Part 6: Troubleshooting Workflow

===============================================================

Now we'll put everything together.

When a service is unreachable, don't randomly run commands. 
Work layer by layer.


Scenario

Imagine an application should be available at:

172.27.211.124:8080

but a client says:

"I can't connect."

*** Step 1 — Is the interface operational?
ip link show eth0

Look for:

UP, LOWER_UP

*** Step 2 — Does the machine have the expected IP?
ip addr show eth0

*** Step 3 — Does Linux have a route?
ip route get 172.27.211.124

*** Step 4 — Is the application listening?
ss -lntp


*** Step 5 — Can TCP actually connect?
nc -vz 172.27.211.124 8080

*** Step 6 — If using a hostname

Then check DNS:

dig example.com


====================================================

Your exercise

Let's troubleshoot a realistic scenario.

Suppose you are told:

"The application on 127.0.0.1:37617 works locally, but another machine cannot connect to it."

You already know:

ss → 127.0.0.1:37617
nc localhost 37617 → succeeded

Question

What is the first thing you would investigate to explain why 
another machine cannot reach it?

==> No need investigation : nc localhost 37617 → succeeded show
that app is running on localhost so no remote machine can reach it

==================================================================

Linux Networking — Part 7: End-to-End Troubleshooting

==================================================================

You have a web application that should be reachable at:

172.27.211.124:8080

A remote client reports:

"Connection refused."

You are on the server.

You don't know yet whether the problem is:

the application
the listening address
the port
routing
or something else


First principle

Don't start with five commands.

Ask:

What is the most useful first piece of evidence I need?

Your task

What command would you run first, and what question would that 
command answer?

One command only.

==> nc -vz 172.27.211.124 8080 -> because you said that application
is reachable on 172.27.211.124:8080  so no need to check port with
ss -lntp.better check TCP connexion directly

================================================================

Linux Networking — Part 8: curl vs nc


We have one more useful distinction before moving toward network
security and AWS VPC networking.

You already know:

nc -vz <IP> <PORT>

tests TCP connectivity.

But if the service is an HTTP application, we can go one level higher.

nc
nc -vz 172.27.211.124 8080

Answers:

Can I establish a TCP connection to port 8080?

It does not tell us whether the HTTP application is functioning 
correctly.

curl

curl http://172.27.211.124:8080

Answers something closer to:

Can I communicate with the HTTP application and receive an HTTP 
response?

So:

curl
  ↓
HTTP/application layer
  ↓
TCP
  ↓
IP

while:

nc
  ↓
TCP
  ↓
IP


Troubleshooting example

Suppose:

nc -vz 10.0.1.10 8080

returns: succeeded

but: curl http://10.0.1.10:8080

returns: HTTP/1.1 500 Internal Server Error

Then the network path and TCP port are working. The problem is
higher up, at the application/HTTP layer.

Your question

If: nc -vz 10.0.1.10 8080

times out, would you immediately investigate the application code?

Why or why not?

No Because nc -vz 10.0.1.10 8080 command rely to layer 4 TCP
so i ll investigate on what can block TCP connexion
(firewall ? , security group, routing pb ...)


curl
  ↓
HTTP / Application
  ↓
TCP :8080
  ↓
IP / Routing
  ↓
Ethernet / Neighbor
  ↓
Interface

And the key principle:

Troubleshoot from the lowest layer necessary based on the evidence
you already have.

