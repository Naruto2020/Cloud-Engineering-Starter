
======================================================================

	Lesson 10 — Linux Routing Troubleshooting

======================================================================


Now let's turn the theory into a real troubleshooting workflow.

You already know:

ip route

shows the routing table, and:

ip route get <destination>

shows the route Linux would choose.

1. Start with the routing table

Run:

ip route

On your machine, we know you have:

default via 172.27.208.1 dev eth0
172.27.208.0/20 dev eth0 src 172.27.211.124

This immediately tells us:

Local network → 172.27.208.0/20 → eth0
Everything else → 172.27.208.1 → eth0
2. Check a specific destination

Suppose you cannot reach:

8.8.8.8

First:

ip route get 8.8.8.8

You already saw:

8.8.8.8 via 172.27.208.1 dev eth0 src 172.27.211.124

So Linux has a route.

That's important because we can now say:

The kernel knows where to send the packet.

But that doesn't necessarily mean the packet will successfully arrive.

3. Routing vs connectivity

This distinction is important.

Imagine:

ip route get 8.8.8.8

returns:

8.8.8.8 via 172.27.208.1 dev eth0

but:

ping -c 3 8.8.8.8

fails.

That does not automatically mean the routing table is wrong.

There are several possibilities:

Application
    ↓
DNS?
    ↓
Transport?
    ↓
IP routing?
    ↓
Gateway?
    ↓
Firewall?
    ↓
Destination?

For example, ICMP may simply be blocked.


.

4. A useful troubleshooting sequence


When a destination cannot be reached, think in layers.

Step 1 — Is the interface up?

ip addr

Look for:

eth0: ... UP ...

and an IP address.

Step 2 — Do I have a route?
ip route

or more specifically:

ip route get <destination>

For example:

ip route get 8.8.8.8
Step 3 — Can I reach the gateway?

Your gateway is:

172.27.208.1

So you could test:

ping -c 3 172.27.208.1

However, remember what we learned earlier:

A failed ping does not necessarily mean the gateway is unreachable.

ICMP can be blocked.

Step 4 — Can I reach the destination?
ping -c 3 8.8.8.8

If this works, basic IP connectivity exists.

Step 5 — If you're testing a hostname, check DNS

For example:

ping -c 3 google.com

If:

ping 8.8.8.8

works but:

ping google.com

fails, suspect DNS.

Then:

cat /etc/resolv.conf

or:

dig google.com


🧠 The troubleshooting decision tree

Think about it like this:

Can't reach destination
          |
          v
     Interface UP?
       /       \
     NO        YES
     |          |
   Fix       Route exists?
              /      \
            NO       YES
            |         |
          Fix       Gateway/
                    connectivity?
                       |
                    Continue
                       |
                  DNS involved?
                       |
                 Check DNS

This is much more useful than simply memorizing commands.

Practical exercise

Let's test your machine.

Run these three commands:

ip route get 172.27.211.50
ip route get 8.8.8.8
ip route get 1.1.1.1



# ==========================================
# Routing - Key Concepts
# ==========================================

Your machine:

IP:      172.27.211.124/20
Network: 172.27.208.0/20
Gateway: 172.27.208.1


If the destination is on the local network,
Linux sends traffic directly through the interface.

Example:

172.27.208.1 → eth0

No "via" because 172.27.208.1 is directly reachable.


If the destination is outside the local network,
Linux sends the traffic to the gateway.

Example:

8.8.8.8 → via 172.27.208.1 dev eth0


==========================================
Routing Table
==========================================

Example:

10.0.0.0/8       dev eth0
192.168.1.0/24   via 10.0.0.1 dev eth1
default          via 10.0.0.254 dev eth0


Linux first finds which routes match
the destination.

Then it chooses the most specific route
(longest prefix match).


Example 1:

Destination: 10.50.2.10

Matches 10.0.0.0/8

→ eth0 directly
→ no gateway


Example 2:

Destination: 192.168.1.50

Matches 192.168.1.0/24

→ via 10.0.0.1
→ dev eth1


Example 3:

Destination: 8.8.8.8

No specific route matches.

→ default route
→ via 10.0.0.254
→ dev eth0


==========================================
🔑 Important Rule
==========================================

A route does not necessarily need a gateway.

Direct route:

10.0.0.0/8 → dev eth0

Next-hop route:

192.168.1.0/24 → via 10.0.0.1 dev eth1

Default route:

default → via 10.0.0.254 dev eth0


==========================================
Routing Decision Process
==========================================

1. Which routes match the destination?

2. Pick the most specific route
   (longest prefix match).

3. Check whether the route is:

   - directly reachable
   - or uses a "via" gateway


==========================================
Big Picture
==========================================

Routing
   ↓
Determine next hop
   ↓
Local destination?
   ↓
Directly through interface

OR

Outside local network?
   ↓
Send to gateway
   ↓
ARP resolves gateway IP → MAC
   ↓
Ethernet frame
   ↓
Interface
