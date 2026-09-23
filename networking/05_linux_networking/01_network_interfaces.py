
===================================================================

	🐧 Linux Networking — Part 1: Network Interfaces

===================================================================

A network interface is the Linux representation of a connection
through which network traffic can enter or leave the machine.

You already have:

eth0

and:

lo


1. lo — Loopback

You saw:

lo
inet 127.0.0.1/8

lo is the loopback interface.

It allows a machine to communicate with itself.

For example:

ping -c 3 127.0.0.1

The traffic doesn't leave your machine.

Application
    ↓
127.0.0.1
    ↓
   lo
    ↓
Same machine

Typical uses include:

local APIs
databases
development servers
services listening only on localhost

You previously saw VS Code Server listening on:

127.0.0.1:36043

That's a good real-world example.


2. eth0 — Network Interface

Your WSL machine has:

eth0

with:

IP:  172.27.211.124/20
MAC: 00:15:5d:d3:1e:16

This is the interface used for your WSL network traffic.

You can inspect it with:

ip addr show eth0

or:

ip link show eth0

Notice the difference:

ip addr

Shows addressing information:

IP address
prefix
IPv6 address
interface state
ip link

Focuses more on the interface itself:

MAC address
interface state
MTU

3. Interface state

  "~$ ip addr show eth0"
  "eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000"
    link/ether 00:15:5d:08:8d:ea brd ff:ff:ff:ff:ff:ff
    altname enx00155d088dea
    "inet 172.27.211.124/20 brd 172.27.223.255 scope global eth0"
       valid_lft forever preferred_lft forever
    inet6 fe80::215:5dff:fe08:8dea/64 scope link proto kernel_ll
       valid_lft forever preferred_lft forever 


Two important flags here are:

UP
LOWER_UP
UP

The interface is administratively enabled.

LOWER_UP

Linux detects that the underlying link is operational.

Conceptually:

UP
 ↓
"Linux enabled this interface"

LOWER_UP
 ↓
"The link itself is operational"


4. MTU

You also saw:

mtu 1500

MTU means:

Maximum Transmission Unit

It is the maximum size of an IP packet that can normally be transmitted over that interface without fragmentation at that layer.

For Ethernet, 1500 bytes is a very common MTU.


🧪 Your turn

Run these two commands:

ip link show eth0

and:

ip addr show eth0

Paste the output.

Then try to identify:

Interface state
MAC address
MTU
IPv4 address
IPv6 address


================================================================

Linux Networking — Part 2: Interface Statistics

Now we move from what an interface is to what traffic is actually passing through it.

1. Concept

Linux keeps traffic counters for each network interface:

RX (receive) → packets/data coming into your machine
TX (transmit) → packets/data leaving your machine
errors
dropped packets

This is useful for troubleshooting things like:

"Is traffic actually reaching my interface?"
"Are packets being dropped?"
"Are there transmission errors?"
2. Command

Run:

ip -s link show eth0

You should see something similar to:

RX:
    bytes
    packets
    errors
    dropped
    ...
TX:
    bytes
    packets
    errors
    dropped
    ...
Your exercise

Run:

ip -s link show eth0

Paste the output here.

Then you will identify:

RX packets
RX errors
RX dropped
TX packets
TX errors
TX dropped

steve@DESKTOP-3P41CE7:~$ ip -s link show eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether 00:15:5d:08:8d:ea brd ff:ff:ff:ff:ff:ff
    RX:  bytes packets errors dropped  missed   mcast
     305455174   26219      0       0       0    5195
    TX:  bytes packets errors dropped carrier collsns
       3287784   14717      0       0       0       0
    altname enx00155d088dea


The counter ...

Direction	Packets	Errors	Dropped
RX	26,219	0	0
TX	14,717	0	0
One extra observation

Your interface also shows:

RX bytes: 305,455,174
TX bytes:   3,287,784

So since the interface statistics were collected/reset, your WSL instance has received considerably more data than it has transmitted.

And importantly:

RX errors   = 0
RX dropped  = 0
TX errors   = 0
TX dropped  = 0

There is no evidence of interface-level packet errors or drops in these counters.

What about mcast?

You also have:

mcast = 5195

That's the number of received multicast packets. Multicast is 
traffic addressed to a group of hosts rather than one specific host.


Next step: deliberately generate traffic

Let's see the counters change.

Run:

ping -c 5 8.8.8.8

Then immediately:

ip -s link show eth0

Question: Compare the new RX/TX packet counters with the previous values.

Which counter increased, and by approximately how much?


Both RX and TX increased.

Why?

When you run:

ping -c 5 8.8.8.8

your machine sends ICMP Echo Requests:

Your WSL
   │
   │ ICMP Echo Request
   ▼
8.8.8.8
   │
   │ ICMP Echo Reply
   ▼
Your WSL

So:

TX increases → your machine transmitted packets.
RX increases → your machine received the replies.

This gives us a useful troubleshooting principle:

Traffic counters tell you whether packets are actually entering or leaving an interface.

Next concept: interface state vs connectivity

You already know:

UP + LOWER_UP

means the interface itself is operational.

But an operational interface doesn't guarantee network connectivity.

For example:

Interface UP
      ↓
Route exists
      ↓
Packets transmitted
      ↓
Packets received
      ↓
Application/port reachable

Each layer can fail independently.



Your next exercise

Run:

1. ip -s link show eth0
2. ip route get 8.8.8.8
3. ping -c 3 8.8.8.8

Then tell me, in your own words, what each command is checking.

1. ip -s link show eth0 -> will check network interface (RX/TX)
2. ip route get 8.8.8.8 -> will check which route linux ll be used
   to reach 8.8.8.8 (eth0; next hop , gateway...)
3. ping -c 3 8.8.8.8 will send an ICMP call to check if this host
   ll answer (basic IP level)


Put them together

ip -s link
      ↓
Is my interface working / moving packets?

ip route get 8.8.8.8
      ↓
How will Linux route the packet?

ping 8.8.8.8
      ↓
Can I actually reach the destination with ICMP?

This is exactly the kind of layered thinking we want for Cloud Engineer network troubleshooting.

Linux Networking — interface + traffic statistics: completed.


