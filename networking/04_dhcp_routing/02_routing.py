
======================================================================

🌐 Routing — How Does a Packet Know Where to Go?

======================================================================

You already saw routing in practice:

ip route

and got:

default via 172.27.208.1 dev eth0
172.27.208.0/20 dev eth0 src 172.27.211.124

Now let's understand why Linux has these routes.


1. What is routing?

Routing is the process of deciding where a packet should be sent next.

Imagine your machine wants to communicate with:

172.27.211.50

This IP is inside your local network:

172.27.208.0/20

Your machine can communicate with it directly through eth0.

But if you want to communicate with:

8.8.8.8

that's outside your local network.

Your machine needs to send the packet to its default gateway:

172.27.208.1

So:

Your machine
172.27.211.124
      |
      | eth0
      v
172.27.208.1
Default Gateway
      |
      v
   Internet
      |
      v
    8.8.8.8


2. The Routing Table

Your Linux machine maintains a routing table.

You can see it with:

ip route

Your table:

default via 172.27.208.1 dev eth0
172.27.208.0/20 dev eth0 src 172.27.211.124

Think of it as a set of rules:

Destination	Where to send	Interface
172.27.208.0/20	Directly	eth0
Everything else	172.27.208.1	eth0


3. Local Network vs Remote Network

This distinction is very important for Cloud/DevOps.

Destination inside your subnet

For example:

172.27.211.50

Your machine checks:

172.27.211.50 ∈ 172.27.208.0/20

Yes.

So:

172.27.211.124
      |
      | eth0
      v
172.27.211.50

No default gateway is needed for the destination itself.

Destination outside your subnet

For example:

8.8.8.8

It doesn't belong to:

172.27.208.0/20

So Linux uses:

default via 172.27.208.1

Therefore:

172.27.211.124
      |
      v
172.27.208.1
      |
      v
    Internet
      |
      v
    8.8.8.8


4. The Most Important Routing Rule

When several routes could potentially match a destination, Linux chooses the most specific route — the route with the longest prefix.

For example:

10.0.0.0/8
10.20.0.0/16
10.20.30.0/24
default

For:

10.20.30.50

all three network routes could match.

Linux chooses:

10.20.30.0/24

because /24 is more specific than /16, which is more specific than /8.

This is called longest-prefix matching.


5. Let's inspect your machine

Run:

ip route

Then run:

ip route get 8.8.8.8

This second command is very useful.

It asks Linux:

"If I want to send a packet to 8.8.8.8, what route would you use?"

Paste the output here.


Yes — your interpretation is correct. You're now reading the routing table rather than just memorizing commands.

1. ip route

Your output:

default via 172.27.208.1 dev eth0 proto kernel
172.27.208.0/20 dev eth0 proto kernel scope link src 172.27.211.124

Your interpretation is correct:

Gateway: 172.27.208.1
Interface: eth0
Network: 172.27.208.0/20
Source IP: 172.27.211.124

One small terminology improvement:

172.27.208.0/20 is the network/prefix, rather than "network addresses."

2. ip route get 8.8.8.8

Your output:

8.8.8.8 via 172.27.208.1 dev eth0 src 172.27.211.124 uid 1000

And your interpretation is exactly right:

Destination:    8.8.8.8
Next hop:       172.27.208.1
Interface:      eth0
Source IP:      172.27.211.124

The key concept here is next hop.

What Linux is saying

You asked:

"Linux, I want to send a packet to 8.8.8.8. What should I do?"

Linux answers:

8.8.8.8
   ↓
Not in my local network
   ↓
Use default route
   ↓
Send to 172.27.208.1
   ↓
Through eth0
   ↓
Using source IP 172.27.211.124

So conceptually:

Your WSL machine
172.27.211.124
       |
       | eth0
       v
172.27.208.1
   next hop /
default gateway
       |
       v
    Internet
       |
       v
     8.8.8.8
     
And this is the important distinction

ip route tells you what routes exist.

ip route

ip route get <destination> tells you which route Linux would actually choose for a specific destination.

ip route get 8.8.8.8

That's a very useful troubleshooting command for a Cloud/DevOps engineer.

Quick challenge 🧠

Without running any command, tell me what you expect Linux to do for:

ip route get 172.27.211.50

Would it use:

A. 172.27.208.1 as the gateway

or

B. send directly through eth0

And why?

B because it ll check if  172.27.211.50   bellong to  172.27.208.0/20  
and it is so it ll send directly through eth0

Exactly. B is correct. 👍

Your reasoning is exactly how you should think about routing.

Why?

Your machine has:

IP:       172.27.211.124/20
Network:  172.27.208.0/20

The destination is:

172.27.211.50

Linux checks whether the destination belongs to the local network:

172.27.211.50 ∈ 172.27.208.0/20

Yes.

Therefore, Linux does not need the default gateway.

It uses:

dev eth0

and communicates directly on the local network.

The routing decision
Destination: 172.27.211.50
       ↓
Matches 172.27.208.0/20?
       ↓
      YES
       ↓
Use eth0 directly
       ↓
No default gateway

Whereas for 8.8.8.8:

Destination: 8.8.8.8
       ↓
Matches 172.27.208.0/20?
       ↓
      NO
       ↓
Use default route
       ↓
172.27.208.1 via eth0



🔑 Core routing rule


If the destination matches a more specific/local route, use that route. Otherwise, use the default route.

And there's one more step we'll add now: ARP.

For 172.27.211.50, Linux knows the IP is local, but Ethernet still needs a MAC address. So the process becomes:

IP destination
     ↓
Routing decision
     ↓
Local network?
     ↓
YES
     ↓
ARP: "Who has 172.27.211.50?"
     ↓
Destination MAC
     ↓
Ethernet frame
     ↓
eth0

This connects Routing + ARP + Ethernet, which is exactly the kind 
of chain you need to understand for cloud networking.



Routing — Multiple Routes & Longest Prefix Match

A real Cloud/DevOps machine can have many routes.

Imagine this routing table:

10.0.0.0/8        via 192.168.1.1
10.20.0.0/16      via 192.168.1.2
10.20.30.0/24     via 192.168.1.3
default           via 192.168.1.254

Now suppose the destination is:

10.20.30.50

Which routes match?

Route 1
10.0.0.0/8

Yes — 10.20.30.50 is inside 10.0.0.0/8.

Route 2
10.20.0.0/16

Yes — it also matches.

Route 3
10.20.30.0/24

Yes — it also matches.

So we have three possible routes.

Which one does Linux choose?

Linux chooses the most specific route.

Compare:

/8
/16
/24

A larger prefix means a more specific network:

/24  ← most specific
/16
/8   ← least specific

Therefore:

10.20.30.50
      ↓
10.20.30.0/24
      ↓
via 192.168.1.3

This is called:

Longest Prefix Match

Why does default exist?

The default route is essentially:

0.0.0.0/0

It matches everything.

But because /0 is extremely broad, any more-specific matching route wins.

For example:

Destination: 10.20.30.50

10.20.30.0/24  → matches ✅
default /0     → matches ✅

Choose /24.

For:

8.8.8.8

Suppose none of the specific routes match:

10.0.0.0/8       ❌
10.20.0.0/16     ❌
10.20.30.0/24    ❌
default /0       ✅

Therefore:

8.8.8.8
   ↓
default route


🧠 Your turn

Using this routing table:

10.0.0.0/8        → Gateway A
10.20.0.0/16      → Gateway B
10.20.30.0/24     → Gateway C
default           → Gateway D

Tell me which gateway Linux will use for each destination and why:

1. 10.20.30.50

-> Gateway C because 10.20.30.50 ∈ 10.20.30.0/24 and /24 is more 
specific than /16 and /8.


2. 10.20.40.50

-> Gateway B because 10.20.40.50 ∈ 10.20.0.0/16 but not on
10.20.30.0/24 so is the most specific


3. 10.50.1.10

-> Gateway A because 10.50.1.10 ∈ 10.0.0.0/8 but no /16 or /24
 so is the most specific


4. 8.8.8.8

-> Gateway D because 8.8.8.8 doesn't match any of those gateway A, B, C
so falls back to default
