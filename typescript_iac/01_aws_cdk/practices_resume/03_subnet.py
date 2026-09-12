============================================================
PART 3 — SUBNET CONFIGURATION
============================================================

A VPC can be divided into multiple subnets.

Example architecture:

VPC
│
├── AZ-1
│   ├── Public subnet
│   └── Private subnet
│
└── AZ-2
    ├── Public subnet
    └── Private subnet


CDK subnet configuration:

subnetConfiguration: [
    {
        cidrMask: 24,
        name: 'ingress',
        subnetType: ec2.SubnetType.PUBLIC,
    },
    {
        cidrMask: 24,
        name: 'application',
        subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
    },
]


IMPORTANT CONCEPT:

subnetType defines the role/connectivity of the subnet.

PUBLIC
  → Can have a route to an Internet Gateway.
  → Used for resources that need to be publicly reachable,
    such as internet-facing Load Balancers.

PRIVATE_WITH_EGRESS
  → Not directly reachable from the Internet.
  → Can access the Internet through a NAT Gateway.
  → Suitable for application servers that need outbound access.


cidrMask: 24

→ Defines the subnet size.
→ A /24 provides 256 IPv4 addresses in the CIDR range.

CDK automatically calculates subnet CIDRs from the VPC CIDR.

Example:

VPC: 10.0.0.0/16
      ↓
├── Public subnet
├── Public subnet
├── Private subnet
└── Private subnet


maxAzs: 2

Combined with two subnet types:

2 AZs × 2 subnet types = 4 subnets


Example architecture:

                   VPC
               10.0.0.0/16
                    │
         ┌──────────┴──────────┐
         │                     │
       AZ-1                   AZ-2
         │                     │
    ┌────┴────┐           ┌────┴────┐
    │         │           │         │
  Public    Private      Public    Private
    │         │           │         │
    │       NAT GW        │       NAT GW
    │         │           │         │
Internet   Internet    Internet   Internet


NAT GATEWAY

Private subnets cannot directly access the Internet.

Instead:

Private subnet
      ↓
  NAT Gateway
      ↓
Internet Gateway
      ↓
   Internet

With:

natGateways: 1

→ CDK creates one NAT Gateway.

With:

natGateways: 2

→ CDK creates two NAT Gateways.

This is an architecture/cost trade-off:

More NAT Gateways
→ better AZ-level resilience
→ higher cost

Fewer NAT Gateways
→ lower cost
→ less resilience


IMPORTANT CDK LESSON:

A high-level VPC construct can automatically create many
underlying AWS resources:

VPC
├── Subnets
├── Route Tables
├── Routes
├── Internet Gateway
└── NAT Gateway(s)

Therefore, always inspect the synthesized CloudFormation
instead of assuming that one line of CDK creates one resource.