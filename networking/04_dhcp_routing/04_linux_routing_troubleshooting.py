
================================================================

🔧 Routing Troubleshooting Scenario

================================================================

Imagine you're on a Linux server and an application cannot reach:

10.20.30.50

You run:

ip route get 10.20.30.50

and get:

10.20.30.50 via 192.168.1.1 dev eth0 src 192.168.1.20

At first glance, Linux does have a route.

Now imagine the application still cannot connect.

Your troubleshooting approach

What would you check next?

Think about the layers we've already studied:

Application
   ↓
TCP / UDP / Port
   ↓
IP / Routing
   ↓
ARP / MAC
   ↓
Ethernet

I want you to propose the next commands you'd run and explain what
each one would tell you.

==> 1- The route exist so let check if my OS know my next hop 
address MAC : ip neigh 


   A- If ARP is okay : 192.168.1.1 dev eth0 lladdr 00:...

      ==> 2- Let call next hop with ICMP 
         ping -c 3 192.168.1.1 

      A-1. If it respond 
         ==> 3- nc -vz 10.20.30.50 443

         A-1-2. If it respond
            ==> investigate on services  

         A-1-3 If It does not respond  
            check TCP or UDP

      A-2. If It does not respond  
         ==> check DHCP configuration

   B- If ARP NOK 
      ==> check eth0

============================================

	You final troubleshooting


Application cannot reach 10.20.30.50
                │
                ↓
1. ip route get 10.20.30.50
                │
                ↓
        Route / next hop ?
                │
                ↓
2. 	    ip neigh
                │
                ↓
       IP → MAC du next hop ?
          /              \
        OK                NOK
        │                  │
        ↓                  ↓
3. ping gateway       Check local connectivity
        │              eth0 / IP / ARP / VLAN
        ↓
     Réponse ?
     /       \
   YES        NO
    │          │
    ↓          ↓
4. nc -vz    Investigate
   10.20.30.50  gateway/network
   443
    │
    ↓
  TCP 443 ?
   /    \
 YES     NO
 │        │
 ↓        ↓
App/TLS   Firewall / service /
HTTP      routing retour / ACL
