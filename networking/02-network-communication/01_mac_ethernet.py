# ==========================================
# Lesson 2 - MAC Addresses & Ethernet
# ==========================================

# Now we move from Layer 3 (IP) down to Layer 2.


# ==========================================
# 1. What is a MAC address?
# ==========================================

# A MAC address identifies a network interface
# on a local network.

# Example:
# 00:1A:2B:3C:4D:5E


# An IP address identifies a device logically
# at Layer 3.

# Example:
# 192.168.1.10


# A MAC address identifies the network interface
# at Layer 2.

# Example:
# 00:1A:2B:3C:4D:5E


# The main difference:
#
# IP address  -> Layer 3 -> Logical network communication
# MAC address -> Layer 2 -> Local network communication


# ==========================================
# 2. IP vs MAC
# ==========================================

# Imagine two devices on the same local network:
#
# PC A
# IP:  192.168.1.10
# MAC: AA:AA:AA:AA:AA:AA
#
# PC B
# IP:  192.168.1.20
# MAC: BB:BB:BB:BB:BB:BB


# If PC A wants to communicate with PC B,
# the destination IP is:
#
# 192.168.1.20


# But on the local Ethernet network,
# the Ethernet frame needs a destination MAC:
#
# BB:BB:BB:BB:BB:BB


# So:
#
# IP packet
#     ↓
# Ethernet frame
#     ↓
# Destination MAC


# ==========================================
# 3. What is Ethernet?
# ==========================================

# Ethernet is a technology used to communicate
# at Layer 2.


# An Ethernet frame contains information such as:
#
# Destination MAC
# Source MAC
# Payload
# ...


# The payload can contain an IP packet:
#
# Ethernet Frame
# └── IP Packet
#     └── TCP Segment
#         └── Application Data


# This is called encapsulation.
#
# Each layer adds its own information.


# When an application sends data:
#
# Application
#     ↓
# TCP
#     ↓
# IP
#     ↓
# Ethernet


# ==========================================
# 4. What does a switch do?
# ==========================================

# A switch connects devices on a local network.


# Example:
#
#             Switch
#          /     |     \
#         /      |      \
#       PC A    PC B    Server


# A switch learns which MAC address
# is connected to which port.


# Example:
#
# MAC Address          Port
# AA:AA:AA:AA:AA:AA    1
# BB:BB:BB:BB:BB:BB    2
# CC:CC:CC:CC:CC:CC    3


# If PC A sends an Ethernet frame to PC B,
# the switch looks at the destination MAC:
#
# BB:BB:BB:BB:BB:BB
#
# and forwards the frame to port 2.


# ==========================================
# 5. Where does ARP come in?
# ==========================================

# Suppose PC A knows the destination IP:
#
# 192.168.1.20


# But PC A does not know the destination MAC:
#
# ???


# PC A uses ARP
# (Address Resolution Protocol)
# to discover the MAC address associated
# with the destination IP.


# Conceptually:
#
# PC A:
# "Who has 192.168.1.20?"
#
#        ↓
#
# PC B:
# "I have 192.168.1.20.
#  My MAC is BB:BB:BB:BB:BB:BB."


# PC A can now associate:
#
# 192.168.1.20
#       ↓
# BB:BB:BB:BB:BB:BB


# PC A can then send the Ethernet frame
# to the correct destination MAC.


# ==========================================
# Big Picture
# ==========================================

# Application
#      ↓
#     TCP
#      ↓
# IP Address
#      ↓
#     ARP
#      ↓
# MAC Address
#      ↓
#   Ethernet
#      ↓
#    Switch


# Later, when we study routing,
# we will see why the MAC address changes
# when traffic crosses networks,
# while the IP destination generally remains
# the same end-to-end.
# ==========================================
# 2. IP vs MAC
# ==========================================

# Imagine two devices on the same local network:
#
# PC A
# IP:  192.168.1.10
# MAC: AA:AA:AA:AA:AA:AA
#
# PC B
# IP:  192.168.1.20
# MAC: BB:BB:BB:BB:BB:BB


# If PC A wants to communicate with PC B,
# the destination IP is:
#
# 192.168.1.20


# But on the local Ethernet network,
# the Ethernet frame needs a destination MAC:
#
# BB:BB:BB:BB:BB:BB


# So:
#
# IP packet
#     ↓
# Ethernet frame
#     ↓
# Destination MAC


# ==========================================
# 3. What is Ethernet?
# ==========================================

# Ethernet is a technology used to communicate
# at Layer 2.


# An Ethernet frame contains information such as:
#
# Destination MAC
# Source MAC
# Payload
# ...


# The payload can contain an IP packet:
#
# Ethernet Frame
# └── IP Packet
#     └── TCP Segment
#         └── Application Data


# This is called encapsulation.
#
# Each layer adds its own information.


# When an application sends data:
#
# Application
#     ↓
# TCP
#     ↓
# IP
#     ↓
# Ethernet


# ==========================================
# 4. What does a switch do?
# ==========================================

# A switch connects devices on a local network.


# Example:
#
#             Switch
#          /     |     \
#         /      |      \
#       PC A    PC B    Server


# A switch learns which MAC address
# is connected to which port.


# Example:
#
# MAC Address          Port
# AA:AA:AA:AA:AA:AA    1
# BB:BB:BB:BB:BB:BB    2
# CC:CC:CC:CC:CC:CC    3


# If PC A sends an Ethernet frame to PC B,
# the switch looks at the destination MAC:
#
# BB:BB:BB:BB:BB:BB
#
# and forwards the frame to port 2.


# ==========================================
# 5. Where does ARP come in?
# ==========================================

# Suppose PC A knows the destination IP:
#
# 192.168.1.20


# But PC A does not know the destination MAC:
#
# ???


# PC A uses ARP
# (Address Resolution Protocol)
# to discover the MAC address associated
# with the destination IP.


# Conceptually:
#
# PC A:
# "Who has 192.168.1.20?"
#
#        ↓
#
# PC B:
# "I have 192.168.1.20.
#  My MAC is BB:BB:BB:BB:BB:BB."


# PC A can now associate:
#
# 192.168.1.20
#       ↓
# BB:BB:BB:BB:BB:BB


# PC A can then send the Ethernet frame
# to the correct destination MAC.


# ==========================================
# Big Picture
# ==========================================

# Application
#      ↓
#     TCP
#      ↓
# IP Address
#      ↓
#     ARP
#      ↓
# MAC Address
#      ↓
#   Ethernet
#      ↓
#    Switch


# Later, when we study routing,
# we will see why the MAC address changes
# when traffic crosses networks,
# while the IP destination generally remains
# the same end-to-end.


# ==========================================
# Exercise - IP vs MAC
# ==========================================

# Imagine this local network:
#
# PC A
# IP:  192.168.1.10
# MAC: AA:AA:AA:AA:AA:AA
#
# PC B
# IP:  192.168.1.20
# MAC: BB:BB:BB:BB:BB:BB
#
# PC A and PC B are connected
# to the same Ethernet switch.


# PC A wants to send data to PC B.


# Answer these questions:


1. What is the destination IP?
IP:  192.168.1.20

2. What is the destination MAC?
MAC: BB:BB:BB:BB:BB:BB


# 3. If PC A doesn't know PC B's MAC address,
#    what protocol does it use?
PC A will use ARP protocol

# 4. What device forwards the Ethernet frame
#    between PC A and PC B?
Switch

# ==========================================
# Your answers:
# ==========================================

# ==========================================
# Exercise - ARP + Switch
# ==========================================

# Imagine this local network:
#
# PC A
# IP:  192.168.1.10
# MAC: AA:AA:AA:AA:AA:AA
#
# PC B
# IP:  192.168.1.20
# MAC: BB:BB:BB:BB:BB:BB
#
# PC C
# IP:  192.168.1.30
# MAC: CC:CC:CC:CC:CC:CC
#
# All three PCs are connected
# to the same Ethernet switch.


# PC A wants to send data to PC B.


# Answer these questions:


# 1. Does PC A use PC B's IP address or MAC address
#    to determine where the Ethernet frame should go?

Yes PC A use both  IP to identifies the logical destination
and MAC to identifies local network inteface

# 2. What happens if PC A doesn't know PC B's MAC address?
If PC A does not know PC B's MAC address, it will rely on ARP
protocol

# 3. Does the switch use the IP address or MAC address
#    to decide which port to forward the frame to?
The switch use MAC adrress.
Because it know which MAC address is connecter to
which port

# 4. Does PC C receive the unicast Ethernet frame
#    intended for PC B?
No Because the switch forwards the unicast Ethernet frame only to the
port associated with PC B's MAC address.

# Give your reasoning, not just the answers.


# ==========================================
# Complete Flow - ARP + Ethernet + Switch
# ==========================================

# The complete flow:
#
#         Application
#              ↓
#             TCP
#              ↓
#       Destination IP
#              ↓
#             ARP
#              ↓
#       Destination MAC
#              ↓
#          Ethernet
#              ↓
#           Switch
#              ↓
#        Correct port
#              ↓
#            PC B


# ==========================================
# ⭐ One sentence to remember
# ==========================================

# IP tells us who we want to communicate with;
# ARP finds the local MAC address;
# the switch uses that MAC address
# to deliver the Ethernet frame.

# ==========================================
# Complete Layer 2 Picture
# ==========================================

# You should be able to distinguish
# these three things:


# ARP table on PC
#
# IP → MAC


# Switch MAC table
#
# MAC → Port


# IP communication
#
# IP → IP


# ==========================================
# Complete Path
# ==========================================

# PC A
#   │
#   │ "I want 192.168.10.20"
#   ↓
#  ARP -> Broadcast FF.FF.FF.FF.FF.FF to all PC on LAN
#   │
#   │ 192.168.10.20 → BB:BB:BB:BB:BB:BB
#   ↓
# Ethernet frame
#   │
#   │ Destination MAC = BB:BB:BB:BB:BB:BB
#   ↓
# Switch
#   │
#   │ MAC → Port 2
#   ↓
# PC B
