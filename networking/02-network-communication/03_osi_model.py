# ==========================================
# TCP vs UDP - Layer 4
# ==========================================

# TCP (Transmission Control Protocol)
# is designed for reliable communication.


# When two applications communicate using TCP,
# they establish a connection first.


# Client                         Server
#   │                              │
#   │ -------- SYN -------------> │
#   │                              │
#   │ <------ SYN + ACK --------- │
#   │                              │
#   │ -------- ACK -------------> │
#   │                              │
#   │       TCP connection        │
#   │          established        │


# This is called the three-way handshake.


# ==========================================
# TCP provides
# ==========================================

# Connection establishment
# Reliable delivery
# Ordering
# Retransmission of lost data
# Acknowledgments
# Flow control


# Example:
#
# Client → Server
#
# Packet 1
# Packet 2
# Packet 3


# If packet 2 is lost:
#
# Packet 1
# Packet 3
#
# TCP can detect the problem
# and retransmit the missing data.


# ==========================================
# UDP
# ==========================================

# UDP (User Datagram Protocol)
# is much simpler.


# There is no TCP-style connection establishment.


# Client                    Server
#   │                         │
#   │ ---- UDP data -------> │
#   │ ---- UDP data -------> │
#   │ ---- UDP data -------> │


# UDP does not inherently guarantee:
#
# Delivery
# Ordering
# Retransmission


# UDP has less overhead
# and can be useful when the application
# prefers speed or can handle loss itself.


# ==========================================
# Simple Analogy
# ==========================================

# Imagine sending a package.


# TCP:
#
# "Did you receive package #1?"
#        ↓
# "Yes."
#        ↓
# "Here is package #2."
#        ↓
# "Yes, received."


# More control and more reliability.


# UDP:
#
# 📦 → 📦 → 📦 → 📦
#
# Send the data without establishing
# a reliable connection first.


# ==========================================
# TCP and UDP Use Ports
# ==========================================

# Both TCP and UDP use port numbers.


# Examples:
#
# TCP 443
# UDP 53


# The port identifies the service/application
# endpoint.


# A server might have:
#
# TCP :22     → SSH
# TCP :80     → HTTP
# TCP :443    → HTTPS
# UDP :53     → DNS


# ⚠️ The protocol matters.


# These are different endpoints:
#
# TCP 53
# UDP 53
#
# Even though they use the same port number,
# TCP and UDP are separate transport protocols.


# ==========================================
# Cloud Engineer Example
# ==========================================

# Imagine an AWS Security Group:
#
# Inbound rule
#
# Protocol: TCP
# Port: 443
# Source: 0.0.0.0/0


# This means:
#
# Allow incoming TCP traffic to port 443.


# If the rule were:
#
# Protocol: UDP
# Port: 443
#
# That would be UDP 443,
# which is different from TCP 443.


# ==========================================
# Linux - See TCP/UDP Services
# ==========================================

# Run:
#
# ss -tuln


# The options mean:
#
# -t → TCP
# -u → UDP
# -l → listening
# -n → don't resolve names; show numbers


# You might see something like:
#
# Netid   Local Address:Port
# tcp     0.0.0.0:22
# udp     0.0.0.0:68


# This tells you which TCP/UDP sockets
# are listening.


# ==========================================
# Exercise - TCP vs UDP
# ==========================================

Before running the command,
answer these questions:


1. Which protocol is connection-oriented?

TCP

2. Which protocol provides retransmission
of lost data?

TCP

3. Which protocol does not perform
a TCP three-way handshake?

UDP

4. Is this:

TCP :443

the same as:

UDP :443

NO

Why?

Because protocole mater.
The port number alone does not identify the transport endpoint;

5. What does this command show?

ss -tuln

This command show which local addresses IP are listening by which 
protocol (TCP , UDP)

or

shows listening TCP and UDP sockets, using numeric addresses and ports.


🔑 This is exactly how you troubleshoot a port

Imagine later you have an API that should run on port 8000.

You could investigate:

ss -tulpn | grep :8000

If you find:

tcp LISTEN 0 128 0.0.0.0:8000 ... users:(("python",pid=1234,...))

then:

ps -p 1234 -f

might reveal:

python app.py

You've now gone from:

Port → Socket → PID → Process → Application

That's a very useful real-world Linux/Cloud troubleshooting workflow.
