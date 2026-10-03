
=========================================================================

	Network Security — Part 1: Why Network Traffic Gets Blocked

=========================================================================


We're moving from "How does traffic travel?" to "Who is allowed to 
communicate?"

This is especially important for Cloud Engineering because AWS networking
combines routing + filtering + identity/security controls.


1. Concept: Connectivity ≠ Permission

Suppose:

Client
  │
  │ TCP → 10.0.1.10:443
  ▼
Server

A route can exist:

Client → Router → Server

but the connection can still fail because something filters the traffic.

Think of the layers separately:

Routing
    ↓
"Can I find a path?"

Filtering
    ↓
"Am I allowed through?"

Service
    ↓
"Is something listening?"

This is why:

ping 10.0.1.10

and:

nc -vz 10.0.1.10 443

can produce different results.


2. What can filter traffic?

At different levels, you can encounter:

------------------------------------------------------------------
Mechanism			Typical role                      |
------------------------------------------------------------------

Host firewall		|	Filters traffic on the machine
Network firewall	|	Filters traffic between networks
AWS Security Group	|	Controls traffic to/from AWS resources
AWS Network ACL	     | Filters subnet traffic
Application firewall		|Filters HTTP/application requests


We'll eventually distinguish Security Groups vs Network ACLs, which is
particularly important for AWS.


3. First important distinction: inbound vs outbound

Imagine:

Client ─────────→ Server
       TCP :443

From the server's perspective:

Inbound traffic

From the client's perspective:

Outbound traffic

The same packet can therefore be described differently depending on which
machine you're looking at.

=========================================================================

Exercise

A server has this rule:

ALLOW TCP 443 from 10.0.0.0/16

A client has IP:

10.0.5.20

and tries:

10.0.1.10:443
Question

Is the client's source IP inside 10.0.0.0/16?

Answer only that first.

==> Yes the client's source IP is inside 10.0.0.0/16


Correct. 10.0.5.20 is inside 10.0.0.0/16. ✅

Let's verify it using the subnetting knowledge you already have:

10.0.0.0/16

has:

Network: 10.0.0.0
Range: 10.0.0.0 → 10.0.255.255
Host portion: last 16 bits

Therefore:

10.0.5.20
   ↑
inside 10.0.0.0/16

So the rule:

ALLOW TCP 443 from 10.0.0.0/16

matches the client's source IP.


Next question

Assume there is no other rule blocking the traffic.

The client connects to:

10.0.1.10:443

Would this rule allow the inbound TCP connection to the server?

Why?


==> Yes this rule allow the inbound TCP connection to the server
Because we have TCP, Port 443 and 10.0.5.20 is inside 10.0.0.0/16

So:

10.0.5.20 ── TCP:443 ──> 10.0.1.10
              ALLOWED

One important distinction:

The rule allows the traffic; it does not by itself guarantee that the connection succeeds.

A route must exist, the server must be listening on 443, and no other 
control can block it.


Next question

Suppose the rule is changed to:

ALLOW TCP 443 from 10.0.0.0/24

Would 10.0.5.20 still be allowed? Why or why not?

==> No 10.0.5.20 would not be allowed. 
Because we have host IP = 32 - 24 = 8
                Addresses = 2^8 = 256
                1st = 10.0.0.0 / last = 10.0.0.254
                broadcast = 10.0.0.255
That mean that with /24 the 3 first range (octet) are fixes
only the last one vary.
Therefore 10.0.5.20 is not inside 10.0.0.0/24


Next question What range of IP addresses does this rule allow? 

ALLOW TCP 443 from 10.0.0.0/16 

Give me the first and last address in the subnet. 

==> this rule allow the last two range (octet) of the given IP address 
1st = 10.0.0.0 / last = 10.0.255.255


The larger the prefix number, the smaller the range.

So /16 is larger than /24, and /24 is larger than /26.

Your idea about how many bits/octets are fixed is good. Let's make it systematic.

IPv4 CIDR cheat sheet

Prefix	Network bits	Host bits	Total addresses	Usable hosts*	Typical meaning

/8	8	24	16,777,216	16,777,214			Very large network
/16	16	16	65,536		65,534				Large network / VPC
/20	20	12	4,096		4,094				Large subnet
/21	21	11	2,048		2,046				Large subnet
/22	22	10	1,024		1,022				Large subnet
/23	23	9	512		510				Medium subnet
/24	24	8	256		254				Very common subnet
/25	25	7	128		126				Small subnet
/26	26	6	64		62				Small subnet
/27	27	5	32		30				Small network
/28	28	4	16		14				Very small network
/29	29	3	8		6				Tiny network
/30	30	2	4		2				Point-to-point
/31	31	1	2		Special case			Point-to-point
/32	32	0	1		1				Single IP / host route


*Traditional IPv4 calculation: total − network address − broadcast 
address. /31 is a special case commonly used for point-to-point links.

Your /16, /24, /26 idea

Think of the IP as 32 bits, not simply four independent ranges:

IPv4 = 32 bits

10.0.0.0
│ │ │ │
│ │ │ └── 8 bits
│ │ └──── 8 bits
│ └────── 8 bits
└──────── 8 bits

For the common prefixes:

/16 → first 16 bits are network
     → 10.0.x.x

/24 → first 24 bits are network
     → 10.0.0.x

/26 → first 26 bits are network
     → roughly 10.0.0.[0-63]
        for the first /26 block



For example, 10.0.0.0/26 gives:

Network:   10.0.0.0
Usable:    10.0.0.1 – 10.0.0.62
Broadcast: 10.0.0.63

And the /24 can be divided into four /26 subnets:

10.0.0.0/26       → .0   – .63
10.0.0.64/26      → .64  – .127
10.0.0.128/26     → .128 – .191
10.0.0.192/26     → .192 – .255


The rule to remember

PREFIX ↑  →  NETWORK ↑  →  HOSTS ↓  →  RANGE ↓

So:

/16  >  /24  >  /26  >  /28  >  /30
large                              small

And one correction to your original statement:

More prefix bits = smaller range, not bigger range.

This is one of the most important CIDR concepts for AWS VPCs and Security
Groups.


Next question

Now let's connect this to network security.

A server has this rule:

ALLOW TCP 22 from 10.0.0.0/16

A client at:

10.0.5.20

tries to connect to:

10.0.1.10:22

Would the firewall rule allow the traffic? Why?

==> Yes the firewall rule will allow the traffic.
Because we have TCP , Port : 22 and 10.0.5.20 belong to 10.0.0.0/16


Next question — inbound vs outbound

Imagine:

Client                         Server
10.0.5.20  ────────────────>  10.0.1.10
              TCP :443

From the client's perspective, is this traffic inbound or outbound?

And from the server's perspective?

==> From the client perspective this traffic is outbound
And from the server is inbound


Next question

Suppose:

Client:  10.0.5.20
Server:  10.0.1.10:443

The client sends a TCP connection request, but the server never receives it.

Which side's filtering rules would you investigate first: the client's 
outbound rules or the server's inbound rules? Why?

==> I will first investigate server's inbound rules
Because the client have no interet in blocking the same traffic he ll 
need to use.But the server have to filter inbound traffics for his 
security


You're thinking in the right direction about where the traffic enters, but there's an important correction.

We should not assume the client has no reason to block outbound traffic. A firewall can intentionally restrict outbound connections too.

For this scenario:

Client                         Server
10.0.5.20  ───── TCP:443 ───> 10.0.1.10
            OUTBOUND          INBOUND

If the server never receives the connection request, we should investigate
both sides, but the first distinction is:

Client outbound filtering → could prevent the packet from leaving.
Server inbound filtering → could prevent the packet from being accepted.
Routing/network controls → could prevent it from reaching the server at all.

So a better troubleshooting mindset is:

Don't assume which side is blocking. Trace the traffic path and test each
layer/control.

For example:

Client
  ↓
Outbound firewall?
  ↓
Routing
  ↓
Network firewall / ACL?
  ↓
Server
  ↓
Inbound firewall?
  ↓
Service listening on :443?

Your security intuition is good: servers commonly enforce inbound 
restrictions, but outbound filtering is also a real security control.


Next question

Now let's introduce AWS Security Groups.

Imagine an EC2 server has this inbound rule:

TCP 443
Source: 10.0.0.0/16

A client at 10.0.5.20 connects to the server on port 443.

Does the Security Group rule care about the client's MAC address? Or does
it use the client's IP address?


==> The Security Group rule don't care about MAC address it use
client's IP address


For:

TCP 443
Source: 10.0.0.0/16

AWS evaluates the source IP against 10.0.0.0/16.

Client                         EC2
10.0.5.20  ───── TCP:443 ───> 10.0.1.10
     ↑
     │
Security Group evaluates
this IP


Next question

Why do you think AWS Security Groups use IP addresses rather than MAC
addresses?


Because IP addresses belong to OSI layer 3 -> communication between
network, while MAC belong to Layer 2 -> local nestwork / Ethernet


One question

If a packet travels:

Client → Router → Server

which layer changes at the router: Layer 2 (MAC), Layer 3 (IP), or both?


==> layer 2


Correct. ✅

Layer 2 changes at the router because the Ethernet frame is rebuilt for the next network.

Client              Router              Server
MAC A ───────────> MAC R1
                   │
                   └──────────────> MAC B

The important distinction:

Layer 2: MAC addresses change at each hop.
Layer 3: Source/destination IP addresses normally remain the same
end-to-end (ignoring things like NAT).

So your mental model is now solid:

L2 → MAC → hop-by-hop
L3 → IP  → end-to-end
L4 → TCP/UDP + port → service



Next question

An EC2 Security Group has:

Inbound:
TCP 22
Source: 10.0.0.0/16

A client at 10.0.5.20 connects to SSH on the EC2 instance.

Which three pieces of information does the Security Group use to decide
whether this rule matches?


==> Source IP address ; Protocol TCP and PORT 22

connection refused does not mean that service is unavailable.
it just mean that server recieve connection request but no service is 
listening on that port or a firewall reject something block

Important troubleshooting rule

Don't immediately conclude:

refused = service definitely down

Instead:

refused = the TCP connection was actively rejected; check whether the 
service is listening and whether anything is explicitly rejecting the 
connection.


Next question

Suppose you have:

Client: 10.0.5.20
Server: 10.0.1.10:443

The route is valid, and the Security Group allows TCP 443, but:

nc -vz 10.0.1.10 443

returns:

Connection refused

What would you check next on the server?

i ll check the port if is already use , and/or firewall ? 

Yes — that's the right direction. ✅

I'd refine it slightly: first check whether anything is listening on TCP
port 443, then investigate the host firewall if necessary.

For example:

ss -lntp | grep ':443'

You're looking for something like:

LISTEN ... 0.0.0.0:443 ...

or:

LISTEN ... 10.0.1.10:443 ...
One terminology correction

You said:

"check if the port is already use"

For a server, we'd normally say:

"Check whether a service is listening on port 443."

A port being "in use" doesn't necessarily mean the expected service is 
available.

So your troubleshooting path is:

nc → Connection refused
          ↓
Is something listening on :443?
          ↓
      Yes / No
          ↓
If needed → check host firewall
