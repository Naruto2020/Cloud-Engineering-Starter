========================================================================

Lesson 9 — DHCP

========================================================================

Let's continue with the same structure:

Concept → Example → Protocol → Command → Exercise → Troubleshooting

1. What is DHCP?

DHCP = Dynamic Host Configuration Protocol.

DHCP automatically gives a device the network configuration it needs to
communicate.

For example, when your computer joins a network, it needs:

IP address
Subnet mask
Default gateway
DNS server

Instead of configuring everything manually, DHCP can provide it
automatically.

Without DHCP

You would manually configure:

IP:       192.168.1.20
Subnet:   255.255.255.0
Gateway:  192.168.1.1
DNS:      1.1.1.1


With DHCP
Computer
   ↓
"Give me network configuration"
   ↓
DHCP server
   ↓
"Here is your configuration"

===================================================================

2. What does DHCP actually provide?

A DHCP server can provide several parameters.

For example:

IP address:       192.168.1.50
Subnet mask:      255.255.255.0
Default gateway:  192.168.1.1
DNS server:       192.168.1.1
Lease time:       86400 seconds

The important ones for you as a Cloud Engineer are:

IP address

Identifies the device at Layer 3.

192.168.1.50
Subnet mask / prefix

Defines the network.

192.168.1.0/24
Default gateway

Tells the machine where to send traffic destined for other networks.

192.168.1.1

DNS server

Tells the machine where to send DNS queries.

192.168.1.1

This connects directly to our previous lesson.

3. DHCP uses UDP

DHCP uses:

UDP port 67
UDP port 68

Conventionally:

DHCP Server → UDP 67
DHCP Client → UDP 68

So:

Client                         Server
UDP :68                       UDP :67
   |                              |
   | ------ DHCP messages ------> |

Why UDP?

Because the client may not have an IP address yet!

That's an important detail.


4. The interesting problem: the client has no IP

Imagine a brand-new computer connects to a network.

It doesn't know:

"My IP address is 192.168.1.50."

It may not even know where the DHCP server is.

So how can it communicate?

DHCP initially uses broadcast communication on the local network.

Conceptually:

New computer
     |
     | "Is there a DHCP server?"
     | Broadcast
     ↓
Local network
     |
     ├── DHCP Server
     ├── Computer A
     ├── Computer B
     └── Printer

The DHCP server can hear the request and respond.

5. The DORA process ⭐

The classic DHCP process is called DORA.

D → Discover
O → Offer
R → Request
A → Acknowledgment

Let's go through it.

Step 1 — DHCP Discover

The client says:

"I need an IP address. Is there a DHCP server?"

Client
   |
   | DHCP DISCOVER
   | Broadcast
   ↓
Network

At this point, the client doesn't have its normal IP configuration yet.

Step 2 — DHCP Offer

A DHCP server responds:

"I can give you 192.168.1.50."

DHCP Server
     |
     | DHCP OFFER
     | 192.168.1.50
     ↓
Client

The offer can contain other configuration information too:

IP:       192.168.1.50
Subnet:   /24
Gateway:  192.168.1.1
DNS:      192.168.1.1


Step 3 — DHCP Request

The client says:

"I want that address."

Client
   |
   | DHCP REQUEST
   | "I want 192.168.1.50"
   ↓
DHCP Server


Step 4 — DHCP ACK

The server confirms:

"Okay. You can use 192.168.1.50."

DHCP Server
     |
     | DHCP ACK
     ↓
Client

The client can now configure its network interface.

6. The complete DORA process

Keep this diagram in your head:

Client                              DHCP Server
  |                                      |
  | -------- DISCOVER -----------------> |
  |                                      |
  | <--------- OFFER ------------------- |
  |                                      |
  | -------- REQUEST ------------------> |
  |                                      |
  | <---------- ACK -------------------- |
  |                                      |

Or simply:

DISCOVER
    ↓
OFFER
    ↓
REQUEST
    ↓
ACK
Memory trick

DORA

Discover → Offer → Request → ACK

7. DHCP leases

DHCP doesn't necessarily give an IP address permanently.

It usually gives a lease.

For example:

IP: 192.168.1.50
Lease: 24 hours

The client can renew the lease.

Conceptually:

IP assigned
    ↓
Lease active
    ↓
Renew
    ↓
Lease continues

If the device disappears from the network, the address can eventually become available for another device.

This is why DHCP is called dynamic.

8. DHCP vs DNS

Don't confuse them.

DHCP

Answers:

"What network configuration should my machine use?"

DHCP
 ↓
IP
Subnet
Gateway
DNS server
DNS

Answers:

"What IP address belongs to this domain?"

DNS
 ↓
google.com
 ↓
142.251.x.x

So:

DHCP → configures your network
DNS  → resolves names


a useful Cloud Engineer habit is:

ip addr
ip route
cat /etc/resolv.conf


Answer these five questions:

What does DORA stand for?

-> Discover : DHCP client broadcast to ask conf to server
   Offer : DHCP server propose conf to client
   Request: DHCP client request to use conf
   Ack : DHCP server acknowleges

Why does a DHCP client initially use broadcast?

-> because it have no network conf (ip , subnet, dhcp, dns)

Which UDP port does the DHCP server use?

-> UDP PORT: 67

Which UDP port does the DHCP client use?

-> UDP PORT : 68

What is the main difference between DHCP and DNS?

DHCP : give network conf and DNS resolve name


==============================================================
