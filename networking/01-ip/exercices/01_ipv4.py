# ==========================================
# Exercise 1 - IPv4 Networking
# ==========================================

# Don't use a calculator yet.

# For this network:
# 10.0.0.0/24

# Answer these 4 questions:

# 1. How many total IP addresses are available?

# 2. What is the network address?

# 3. What is the broadcast address?

# 4. What is the range of usable host IPs?


# ==========================================
# Your answers:
# ==========================================

1.  2^8 = 256 

An IPv4 address has 32 bits.
The /24 tells us that 24 bits are used for network.
And  32 - 24 = 8  remaining for hists (machine) 

Therefore : 2^8 = 256  total IP addresses.

2. 10.0.0.0

3. 10.0.0.255

With /24, the last octet contains the 8 host bits: 10.0.0.[xxxxxxxx]
The broadcast address is when all host bits are 1: 11111111
And 11111111 = 255

Therefore: Broadcast = 10.0.0.255

4. 10.0.0.1  =>   10.0.0.254

Since total addresses = 256, usable hosts are 256 - 2 (network address and Broadcast address) = 254


# ==========================================
# Exercise 2 - /25
# ==========================================

# Now let's make it slightly harder.

# Consider:
# 192.168.1.0/25

# Remember:
# 32 - 25 = ?

# Find:

# 1. Number of host bits

# 2. Number of total addresses

# 3. Network address

# 4. Broadcast address

# 5. First usable IP

# 6. Last usable IP


# Don't worry if you don't know /25 yet.
# Try to reason it out from /24.


# ==========================================
# Your answers:
# ==========================================

1. 32 - 25 = 7

2. 2^7 = 128

3. 192.168.1.0

4. 192.168.1.127
Since the /25 bits use for network
Network addresses is 128 and not 256
The broadcast address is when all host bits are 1: 1111111
And 1111111 = 127
Therefore Broadcast = 127

5. 192.168.1.1

6. 192.168.1.126

NB: A /25 splits a /24 network into 2 subnets.
Network 1 :  192.168.1.0/25  
192.168.1.1 => 192.168.1.126

Network 2 : 192.168.1.128/25
192.168.1.129 => 192.168.1.254