# IP Addressing

This section covers the fundamentals of **IPv4 addressing** and **CIDR notation**.

The goal is to understand how IPv4 addresses are structured, how to calculate the number of available addresses, and how a network can be divided into subnets.

## 📚 Topics Covered

* IPv4 address structure
* Network bits and host bits
* CIDR notation
* `/24` networks
* `/25` networks
* Network address
* Broadcast address
* Usable host IP addresses
* Basic subnetting

---

## 🌐 IPv4 Basics

An IPv4 address contains **32 bits**, divided into four octets:

```text
10.0.0.0
```

Each octet contains 8 bits:

```text
8 bits + 8 bits + 8 bits + 8 bits = 32 bits
```

CIDR notation indicates how many bits are used for the network portion.

For example:

```text
10.0.0.0/24
```

The `/24` means:

```text
24 bits → Network
8 bits  → Hosts
```

The number of host bits can be calculated with:

```text
32 - CIDR prefix = Host bits
```

---

## 🔢 Calculating Total IP Addresses

The number of total IP addresses is calculated using:

```text
2^(number of host bits)
```

### Example: `/24`

```text
32 - 24 = 8 host bits

2^8 = 256 total IP addresses
```

A `/24` network therefore contains **256 total addresses**.

---

## 📡 Network and Broadcast Addresses

Each subnet reserves two addresses:

* **Network address** → identifies the network
* **Broadcast address** → used to communicate with all hosts on the subnet

These two addresses cannot normally be assigned to hosts.

### Example: `10.0.0.0/24`

```text
Network address:   10.0.0.0
Usable hosts:      10.0.0.1 - 10.0.0.254
Broadcast address: 10.0.0.255
```

Therefore:

```text
256 total addresses
- 2 reserved addresses
= 254 usable host addresses
```

---

## ✂️ Basic Subnetting with `/25`

A `/25` network has:

```text
32 - 25 = 7 host bits

2^7 = 128 total addresses
```

### Example

```text
192.168.1.0/25
```

The address range is:

```text
Network address:   192.168.1.0
First usable IP:   192.168.1.1
Last usable IP:    192.168.1.126
Broadcast:         192.168.1.127
```

There are:

```text
128 total addresses
- 2 reserved addresses
= 126 usable host addresses
```

---

## 🔀 Splitting a `/24` into `/25` Subnets

A `/25` splits a `/24` network into **two subnets**.

For example:

```text
192.168.1.0/24
```

can be divided into:

### Network 1

```text
192.168.1.0/25

Network:   192.168.1.0
Usable:    192.168.1.1 - 192.168.1.126
Broadcast: 192.168.1.127
```

### Network 2

```text
192.168.1.128/25

Network:   192.168.1.128
Usable:    192.168.1.129 - 192.168.1.254
Broadcast: 192.168.1.255
```

So:

```text
192.168.1.0/24
        │
        ├── 192.168.1.0/25
        └── 192.168.1.128/25
```

Each `/25` subnet contains:

```text
128 total addresses
126 usable host addresses
```

---

## 🧠 Key Formulas

### Host bits

```text
32 - CIDR prefix
```

### Total addresses

```text
2^host_bits
```

### Usable host addresses

```text
Total addresses - 2
```

The two reserved addresses are the **network address** and the **broadcast address**.

---

## 📝 Exercises

The following exercises were completed as part of my networking practice:

* **Exercise 1:** IPv4 `/24` network
* **Exercise 2:** IPv4 `/25` subnetting

These exercises focus on calculating:

* number of host bits;
* total IP addresses;
* network address;
* broadcast address;
* first usable IP;
* last usable IP;
* basic subnet division.

---

## 🎯 Learning Goal

The objective is to become comfortable with IPv4 addressing and subnetting calculations before moving on to more advanced networking concepts such as:

* routing;
* DNS;
* TCP / UDP;
* network troubleshooting;
* Cloud networking and VPC subnets.

>This section will be updated as I progress through my Cloud Engineering learning journey and cover additional IP networking concepts.