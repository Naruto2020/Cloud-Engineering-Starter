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

# ==========================================
# Exercise 3 - /26
# ==========================================

# Consider this network:
# 10.0.0.0/26

# Find:

# 1. Host bits

# 2. Total addresses

# 3. Network address

# 4. Broadcast address

# 5. First usable IP

# 6. Last usable IP


# ==========================================
# Your answers:
# ==========================================

1. 32 - 26 = 6

2. 2^6 = 64

3. 10.0.0.0

4. 10.0.0.63

5. 10.0.0.1

6. 10.0.0.62

# ==========================================
# Subnetting Logic to Remember
# ==========================================

# An IPv4 address contains 32 bits.
#
# The CIDR prefix (/24, /25, /26, etc.)
# tells us how many bits are used for the network.
#
# Formula:
#
# Host bits = 32 - CIDR prefix
#
# Total addresses = 2^(host bits)


# Example with a /24 network:
#
# /24 -> 256 addresses -> 1 subnet


# When we increase the prefix by 1:
#
# /25 -> 128 addresses per subnet -> 2 subnets
# /26 ->  64 addresses per subnet -> 4 subnets
# /27 ->  32 addresses per subnet -> 8 subnets
# /28 ->  16 addresses per subnet -> 16 subnets


# Important pattern:
#
# Increasing the prefix by 1:
# -> divides the number of addresses by 2
# -> doubles the number of subnets


# Example:
#
# A /24 network:
# 192.168.1.0 - 192.168.1.255
#
# Split into /25:
#
# Subnet 1: 192.168.1.0/25
# Range: .0 - .127
#
# Subnet 2: 192.168.1.128/25
# Range: .128 - .255
#
#
# Split into /26:
#
# Subnet 1: 192.168.1.0/26
# Range: .0 - .63
#
# Subnet 2: 192.168.1.64/26
# Range: .64 - .127
#
# Subnet 3: 192.168.1.128/26
# Range: .128 - .191
#
# Subnet 4: 192.168.1.192/26
# Range: .192 - .255