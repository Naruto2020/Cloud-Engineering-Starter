
🌐 Network Fundamentals for Cloud Engineer
Lesson 8 — DNS (Domain Name System)

Let's continue in English and keep the same approach:

Concept → Example → Command → Exercise → Troubleshooting

1. What is DNS?

DNS = Domain Name System.

DNS translates a domain name into an IP address.

For example:

google.com
     ↓
     DNS
     ↓
142.250.x.x

Humans prefer names:

google.com

Computers communicate using IP addresses:

142.250.x.x

So DNS is essentially the name-resolution system of the Internet.

2. Why do we need DNS?

Imagine you want to connect to a web server.

Without DNS, you would need to remember:

142.250.74.14

instead of:

google.com

DNS allows applications to use names.

The simplified process is:

You type:

https://google.com

        ↓

DNS asks:

"What IP address belongs to google.com?"

        ↓

DNS returns:

142.250.x.x

        ↓

Your computer connects to that IP

        ↓

TCP :443

        ↓

HTTPS

So remember this chain:

Domain name
     ↓
DNS
     ↓
IP address
     ↓
TCP/UDP
     ↓
Port
     ↓
Application


3. DNS is not HTTP

This distinction is important.

When you type:

https://example.com

several different protocols are involved.

DNS

Finds the IP:

example.com
      ↓
93.184.216.34


TCP

Creates the transport connection:

Client → Server


TCP :443


HTTPS

Actually communicates with the web server:

GET / HTTP/1.1

So:

DNS finds the server. HTTPS communicates with the server.

4. What is a DNS server?

A DNS server answers DNS queries.

For example:

Client
   |
   | "What is the IP of example.com?"
   ↓
DNS Server
   |
   | "93.184.216.34"
   ↓
Client

Your computer normally doesn't know the IP address of every website.

Instead, it asks a DNS resolver.

5. DNS records

DNS doesn't only store domain → IP mappings.

It stores different types of DNS records.

The most important ones for us are:

Record	Purpose
A	Domain → IPv4
AAAA	Domain → IPv6
CNAME	Name → another name
MX	Mail server
A record
example.com → 93.184.216.34

IPv4.

AAAA record
example.com → 2606:2800:220:1:...

IPv6.

CNAME

For example:

www.example.com
        ↓
example.com

It says essentially:

"This name is an alias for another DNS name."

MX

Used for email.

example.com
     ↓
MX
     ↓
mail.example.com


6. The command you'll use a lot: dig

On Linux:

dig example.com

Try:

dig google.com

You'll get something similar to:

;; ANSWER SECTION:
google.com.    300    IN    A    142.250.x.x

The important part is:

google.com.    A    142.250.x.x

Meaning:

google.com has this IPv4 address.


7. Ask specifically for an A record

You can tell dig exactly what you want:

dig google.com A

For IPv6:

dig google.com AAAA

For mail servers:

dig google.com MX

For a CNAME:

dig www.example.com CNAME
8. A useful simplified dig

You can use:

dig +short google.com

Instead of all the detailed DNS information.

You might get:

142.250.x.x
142.250.x.x

This is very useful when troubleshooting.

9. nslookup

Another command is:

nslookup google.com

It also performs DNS resolution.

For Cloud/DevOps work, you'll commonly see both:

dig
nslookup

I recommend becoming more comfortable with dig, because it gives you more useful information for troubleshooting.

10. One important troubleshooting concept

Suppose:

curl https://example.com

doesn't work.

There are many possible causes.

You can test DNS separately:

dig example.com

If DNS works:

example.com → IP

then DNS resolution is probably working.

You can then investigate the next layer:

DNS
 ↓
IP connectivity
 ↓
TCP :443
 ↓
TLS
 ↓
HTTP/HTTPS

This is exactly how a Cloud Engineer should think about troubleshooting.

#========================================================================================
# Exercice
#========================================================================================


🧪 Exercise 1 — Your turn

Run these commands in your Debian WSL:

dig google.com

Then:

dig +short google.com

Then:

dig google.com A

And finally:

nslookup google.com


🧠 Your DNS mental model

At this point, you should understand this:

                    DNS
                     │
                     ▼
              "What is the IP
               of google.com?"
                     │
                     ▼
             DNS resolver
          10.255.255.254:53
                     │
             ┌───────┴───────┐
             ▼               ▼
         A record         AAAA record
             │               │
             ▼               ▼
        IPv4 address      IPv6 address

And then the application can use that address:

google.com
    ↓
DNS
    ↓
142.251.142.14
    ↓
TCP
    ↓
443
    ↓
HTTPS

That's the bigger picture I want you to keep in your head.


#==============================================================================

     Recursive vs authoritative DNS

#==============================================================================     

This is the next important concept.

You currently have:

Your Debian
     ↓
10.255.255.254:53
     ↓
Recursive resolver

Your resolver is answering your questions.

But it isn't necessarily the server that owns the DNS information for google.com.

The authoritative DNS infrastructure for google.com includes Google's authoritative servers.

Very simplified:

              You
               │
               │ "What is google.com?"
               ▼
      Recursive DNS Resolver
         10.255.255.254
               │
               │ "I need to find the answer."
               ▼
       DNS hierarchy
               │
               ▼
    Authoritative DNS server
        for google.com
               │
               │ "A = 142.251.142.14"
               ▼
      Recursive Resolver
               │
               ▼
              You

This distinction is very important in Cloud Engineering.

🎯 One concept to remember

Don't confuse these two:

Recursive resolver

"I'll find the answer for you."

Client
  ↓
Recursive Resolver
  ↓
finds answer
  ↓
Client


Authoritative DNS server

"I am responsible for the official DNS records for this domain."

Recursive Resolver
       ↓
Authoritative Server
       ↓
Official DNS records

#===============================================================================

     🧪 Next practical exercise

#===============================================================================

Let's actually ask dig to show us the DNS delegation path.

Run:

dig +trace google.com

This command is very interesting because instead of simply asking your configured resolver for 
the final answer, it shows the DNS resolution process through the hierarchy.

You'll probably see something along the lines of:

.
↓
.com
↓
google.com
↓
IP address
