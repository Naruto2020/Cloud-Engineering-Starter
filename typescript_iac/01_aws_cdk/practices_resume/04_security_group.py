============================================================
PART 4 — SECURITY GROUPS
============================================================

A Security Group acts as a virtual firewall for AWS resources.

It controls:

- Ingress  → incoming traffic
- Egress   → outgoing traffic


Our architecture:

                Internet
                   │
             TCP 80 / 443
                   ↓
          ┌─────────────────┐
          │  Load Balancer  │
          │      SG         │
          └─────────────────┘
                   │
                TCP 8080
                   ↓
          ┌─────────────────┐
          │   Application   │
          │      SG         │
          └─────────────────┘


============================================================
LOAD BALANCER SECURITY GROUP
============================================================

Example:

const loadBalancerSG = new ec2.SecurityGroup(
    this,
    'LoadBalancerSG',
    {
        vpc: vpc,
        description: 'Load Balancer Security Group',
        allowAllOutbound: false,
    }
);


allowAllOutbound: false

→ Disables the default allow-all outbound traffic.

The exercise intentionally keeps the Load Balancer egress
restricted because we are focusing on the required traffic.


INGRESS RULE — HTTPS

loadBalancerSG.addIngressRule(
    ec2.Peer.anyIpv4(),
    ec2.Port.tcp(443),
    'Allow HTTPS traffic'
)

Means:

Source:      0.0.0.0/0
Protocol:    TCP
Port:        443
Destination: Load Balancer

In other words:

Internet ──TCP 443──> Load Balancer


INGRESS RULE — HTTP

loadBalancerSG.addIngressRule(
    ec2.Peer.anyIpv4(),
    ec2.Port.tcp(80),
    'Allow HTTP traffic'
)

Means:

Internet ──TCP 80──> Load Balancer


============================================================
APPLICATION SECURITY GROUP
============================================================

Example:

const applicationSG = new ec2.SecurityGroup(
    this,
    'ApplicationSG',
    {
        vpc: vpc,
        description: 'Application Security Group',
        allowAllOutbound: true,
    }
);


allowAllOutbound: true

→ Allows outbound traffic by default.

The application can therefore initiate outbound connections.


============================================================
APPLICATION INGRESS
============================================================

applicationSG.addIngressRule(
    loadBalancerSG,
    ec2.Port.tcp(8080),
    'Allow HTTP traffic from LB'
)

This is the most important Security Group rule.

It means:

Source:
    LoadBalancerSG

Protocol:
    TCP

Port:
    8080

Destination:
    ApplicationSG


Therefore:

Load Balancer SG ──TCP 8080──> Application SG

The application does NOT allow the entire Internet on port 8080.

Instead, only resources associated with the Load Balancer SG
are allowed to connect to port 8080.


============================================================
SECURITY GROUP MENTAL MODEL
============================================================

Internet
   │
   ├── TCP 80 ────> LoadBalancerSG
   │
   └── TCP 443 ───> LoadBalancerSG
                        │
                        │ TCP 8080
                        ↓
                   ApplicationSG


This creates a layered security model:

Internet
   ↓
Load Balancer
   ↓
Application

The application is not directly exposed to the Internet.


============================================================
VERIFYING THE GENERATED SECURITY GROUPS
============================================================

Build the TypeScript project:

npm run build

Generate CloudFormation:

npx cdk synth > template.yaml

Search for Security Groups:

grep -n "AWS::EC2::SecurityGroup" template.yaml

Inspect specific sections:

sed -n "430,450p" template.yaml


The generated CloudFormation allows us to verify that CDK
translated our TypeScript configuration correctly.


Example:

TypeScript:

ec2.Port.tcp(443)

becomes:

IpProtocol: tcp
FromPort: 443
ToPort: 443


TypeScript:

ec2.Peer.anyIpv4()

becomes:

CidrIp: 0.0.0.0/0


TypeScript:

applicationSG.addIngressRule(
    loadBalancerSG,
    ec2.Port.tcp(8080)
)

becomes a CloudFormation SecurityGroupIngress resource
referencing the Load Balancer Security Group as the source.


============================================================
KEY CLOUD ENGINEER WORKFLOW
============================================================

Requirement
    ↓
TypeScript / CDK
    ↓
npm run build
    ↓
npx cdk synth
    ↓
CloudFormation
    ↓
Inspect generated resources
    ↓
Verify the architecture

The goal is NOT just to memorize CDK syntax.

The goal is to understand:

  CDK code
      ↓
  generated AWS resources
      ↓
  actual network/security architecture

So far, we are inspecting the generated infrastructure.
We have NOT deployed it with "cdk deploy".
============================================================