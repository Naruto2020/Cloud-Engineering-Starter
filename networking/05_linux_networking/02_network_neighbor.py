
==================================================================

Linux Networking — Part 3: Network Neighbors

Now we'll connect what you learned about ARP with the Linux
commands you use to inspect it.

Concept

For IPv4, your machine needs to know:

IP address → MAC address

Linux stores this information in its neighbor table.

You already saw this earlier with:

ip neigh

Example:

172.27.208.1 dev eth0 lladdr 00:15:5d:cd:f4:61 REACHABLE

This means:

"To reach 172.27.208.1 through eth0, I know its MAC address."

Remember the distinction:

Routing:
IP destination → next hop

ARP / neighbor table:
next-hop IP → MAC address


Exercise

Run:

ip neigh show dev eth0

Paste the output.

Then identify:

IP address
MAC address
Interface
Neighbor state


===============================================================

Linux Networking — Part 4: Sockets & Connections

Since you've already covered Linux fundamentals, we'll focus on the
networking perspective and avoid repeating basic Linux material.

You already used:

ss -tuln

Now let's connect it to what you've learned about IP + ports + TCP.

Concept

A network service typically listens on:

IP address : Port


For example:

0.0.0.0:22
127.0.0.1:8080
172.27.211.124:443

The important distinction is:

127.0.0.1:8080 → only locally accessible
0.0.0.0:8080 → listening on all IPv4 interfaces
172.27.211.124:8080 → specifically bound to that interface/IP

This becomes very important in cloud troubleshooting.

Exercise

Run:

ss -lntp

Look at the Local Address:Port column.

Find one listening TCP socket and tell me:

Local IP/address
Port
Process/PID


The key idea is the IP address the service is bound to.

127.0.0.1:37617

127.0.0.1 is the loopback interface, so the service accepts 
connections originating from the same machine.

A remote machine trying:

172.27.211.124:37617

would not normally reach that listener because the application 
isn't listening on eth0.

Cloud relevance

This is a very common cloud troubleshooting issue:

Application
    ↓
Listening on 127.0.0.1:8080
    ↓
Works locally ✅

Load Balancer / another server
    ↓
172.x.x.x:8080
    ↓
Connection fails ❌

Changing the application binding to an appropriate non-loopback
address can make it externally reachable—but then security groups, 
firewalls, routing, and authentication also matter.

One question

Suppose a web application is listening on:

0.0.0.0:8080

What does 0.0.0.0 mean in this context?

==> It is mean the application can linten on all IPV4 interface
on port :8080


Mental model
127.0.0.1:8080
→ loopback only

172.27.211.124:8080
→ that specific interface/IP

0.0.0.0:8080
→ all local IPv4 interfaces


=============================================================

Linux Networking — Part 5: Listening vs Reachability

Now let's make one important distinction before moving on.

A service can be listening without being reachable.


For example:

Application
   ↓
0.0.0.0:8080
   ↓
Listening ✅

But external connectivity still depends on:

Client
  ↓
Routing
  ↓
Network interface
  ↓
Firewall / Security Group
  ↓
Port 8080
  ↓
Application


So when troubleshooting:

"The application is running" does not automatically mean 
"the application is reachable."


Practical test

We can test a TCP port directly with:

nc -vz 127.0.0.1 <PORT>

This asks:

"Can I establish a TCP connection to port ex: 37617 on localhost?"

Run it and paste the result.

steve@DESKTOP-3P41CE7:~$ nc -vz 127.0.0.1 37617
Connection to 127.0.0.1 37617 port [tcp/*] succeeded!

Exactly. This is the practical difference we wanted to demonstrate.

ss -lntp
      ↓
127.0.0.1:37617
      ↓
Something is listening

Then:

nc -vz 127.0.0.1 37617
      ↓
TCP connection succeeded
      ↓
The port is actually reachable locally
The troubleshooting distinction
Test	Question
ss -lntp	Is something listening?
nc -vz IP PORT	Can I establish a TCP connection?
ping IP	Can I get an ICMP response?
ip route get IP	How will Linux route the traffic?
ip neigh	What Layer-2 neighbor is known?

This gives you a strong troubleshooting chain:

Application
    ↓
TCP port
    ↓
IP
    ↓
Routing
    ↓
Neighbor / MAC
    ↓
Interface

And this is exactly the kind of reasoning you'll later apply to AWS
EC2 → Security Group → VPC routing → application port.


