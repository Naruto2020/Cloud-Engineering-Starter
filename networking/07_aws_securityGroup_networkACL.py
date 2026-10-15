
======================================================================

	Lesson 5.2 — AWS Security Groups vs. Network ACLs

======================================================================




1. Definition

A Network Access Control List (Network ACL or NACL) is a network security
control in Amazon VPC that filters traffic entering and leaving a subnet.

It acts like a firewall at the subnet boundary. It can explicitly allow 
or deny traffic based on rules such as the protocol, port range, and 
source or destination IP address.

For example, you can configure a Network ACL to:

- Allow inbound HTTPS traffic on TCP port 443.
- Deny traffic from a particular IP address.
- Allow or deny outbound traffic according to defined rules.

2. Where does it operate?

Let's imagine an AWS VPC containing a subnet with two EC2 instances.
Amazon VPC
Your isolated virtual network in AWS

Subnet
Network ACL
Filters traffic at the subnet level

EC2 A
Security Group A

EC2 B
Security Group B


The distinction is the scope of each control:

- Network ACL: associated with a subnet, so it applies to traffic 
entering or leaving that subnet.

- Security Group: associated with network interfaces of resources such 
as EC2 instances.

Both controls can affect the same connection. The traffic must be 
permitted by the applicable controls.

3. Default vs. custom Network ACLs

AWS provides two common types:

- Default Network ACL: created with a VPC. By default, it allows all 
inbound and outbound traffic.

- Custom Network ACL: created with more restrictive rules as needed. 
A newly created custom NACL denies traffic by default until you add rules.
These defaults matter when troubleshooting: don't assume every NACL 
blocks traffic, or that every NACL allows it.

4. How a Network ACL evaluates traffic

A NACL has separate inbound and outbound rule lists.

Each rule includes:

Field					Meaning

Rule number			Determines evaluation order
Protocol			For example, TCP
Port range			For example, 443
Source or destination		An IP address or CIDR range
Action				ALLOW or DENY


Unlike a Security Group, a Network ACL is stateless. It doesn't 
automatically permit return traffic just because it allowed the original 
request.

We'll study rule-number evaluation next, once these fundamentals are clear.

Quick understanding check

An AWS VPC has one subnet containing three EC2 instances. That subnet 
has one Network ACL, while each EC2 instance has its own Security Group.

If you add a DENY rule to that subnet's Network ACL, which scope does 
that rule apply to: the subnet's traffic or only one specific EC2 instance?



Next concept: Default vs. custom NACLs

AWS has two important starting configurations:

NACL type			Initial behavior
Default NACL	Allows all inbound and outbound traffic by default.
Custom NACL	Denies all inbound and outbound traffic by default until 
you add rules.

Remember: default behavior is not the same as guaranteed connectivity. 
Routes, Security Groups, host firewalls, and other controls can still 
block traffic.

Understand this scenario

You create a new custom NACL and associate it with a subnet containing 
an EC2 instance. You haven't added any rules yet.

Will an inbound connection to that EC2 instance be allowed by the NACL 
or denied by the NACL?


==> An inbound connection to that EC2 instance ll be denied by NACL


Concept: What happens to an HTTPS request?
Imagine an EC2 instance receives an HTTPS request from a client.


Client
Sends TCP request to port 443

Network ACL
Subnet-level filtering · Stateless

Security Group
Resource-level filtering · Stateful

EC2 instance
HTTPS service listening on port 443


Both controls must permit the relevant traffic. Even then, routing and 
the availability of the service matter.


Example: The request and response
Suppose the client uses this connection:
Client: 10.0.5.20:51500
Server: 10.0.1.10:443
Protocol: TCP


The request travels to the server's port 443. The response travels back 
to the client's temporary port 51500.

The key difference:

- Security Group (stateful): tracks the connection and automatically 
permits its return traffic.

- Network ACL (stateless): evaluates each direction independently, so its
rules must also allow the necessary response traffic.

Remember: 51500 is an example of an ephemeral port; the actual client 
port can vary.

========================================================================

Exercise — apply what you've learned

An EC2 instance has:

- A Security Group allowing inbound TCP 443 from 10.0.0.0/16.
- A Network ACL allowing inbound TCP 443 from the same range.
- A valid route and a service listening on port 443.

However, the Network ACL has no outbound rule allowing the response traffic.
Will the HTTPS connection succeed? Why or why not?

Take your time and explain your reasoning. We'll correct your answer 


==> The HTTPS connection ll not succeed. Because Network ACL is stateless
so it is evaluate each request independently so ll not provide an 
automaticaly return and there is no outbound rules to permit the response


Let's trace it:
Client                         EC2 instance
10.0.5.20:51500                10.0.1.10:443
     │                               │
     ├──── HTTPS request ───────────>│
     │                               │
     │       Network ACL             │
     │       Allows inbound 443 ✓    │
     │                               │
     │<──── HTTPS response ──────────┤
     │                               │
     ✗ Outbound NACL rule missing


The Security Group automatically permits return traffic for the tracked 
connection. However, the Network ACL evaluates the response 
independently, so its outbound rules must permit it.

For this example, the outbound NACL must allow the response traffic to 
the client's ephemeral port (51500).

Key takeaway

Control	Stateful?	Return traffic
Security Group	Yes	Automatically permitted for tracked connections
Network ACL	No	Must be allowed by the applicable rules


Network ACL rule numbers
AWS evaluates NACL rules in ascending numerical order. The first matching
rule determines whether traffic is allowed or denied.

Rule number	Source			Action

100		10.0.0.0/16		ALLOW
110		10.0.5.20/32		DENY
*		All other traffic	DENY


Your exercise
A client at 10.0.5.20 connects to TCP port 443.
Will the packet be allowed or denied, and why?
Take your time and explain your reasoning. I'll correct your answer 
before we move to the next concept.


==> ye the packet ll be allowed , because ip is inside source range 


Correct! ✅ The packet will be ALLOWED because 10.0.5.20 belongs to the 
source CIDR range 10.0.0.0/16.

Rule 100 matches first, so AWS applies ALLOW and stops evaluating rules. 
Rule 110 is never reached.

