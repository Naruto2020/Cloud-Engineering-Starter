# ============================================================
# Exercise 12 — Application Load Balancer + EC2
# ============================================================

# Goal
# ============================================================

Connect an Application Load Balancer to the EC2 instance and
understand how CDK represents the ALB architecture through
CloudFormation resources.

The goal was also to verify what CDK actually creates underneath
the high-level constructs instead of assuming that the TypeScript
code directly represents the final AWS resources.


# ============================================================
# 1. ALB architecture
# ============================================================

The architecture we wanted to build was:

Internet
   │
   │ HTTP :80
   ▼
Application Load Balancer
   │
   │ Listener :80
   ▼
Target Group
   │
   │ HTTP :8080
   ▼
EC2 Instance

The ALB is public.

The EC2 instance remains in a private subnet.


# ============================================================
# 2. Main CDK concepts
# ============================================================

ApplicationLoadBalancer
→ Creates the Application Load Balancer.

addListener()
→ Creates a listener that accepts incoming traffic.

addTargets()
→ Connects the listener to a Target Group and defines the
  backend target.

Target Group
→ Defines where the ALB sends the traffic.


# ============================================================
# 3. CloudFormation resources
# ============================================================

When we ran `cdk synth`, the high-level CDK configuration was
translated into several CloudFormation resources.

We verified:

AWS::ElasticLoadBalancingV2::LoadBalancer
AWS::ElasticLoadBalancingV2::Listener
AWS::ElasticLoadBalancingV2::TargetGroup
AWS::EC2::Instance

The `V2` in `AWS::ElasticLoadBalancingV2::*` is part of the
CloudFormation resource namespace used for Elastic Load
Balancing resources.

The important point is that this does not mean we created
a "different version" of the ALB in our architecture.

We are using the CDK high-level Application Load Balancer
construct, and CDK translates it into the corresponding
CloudFormation resources.


# ============================================================
# 4. Target Group verification
# ============================================================

We inspected the synthesized CloudFormation to verify the
Target Group configuration.

The important properties were:

TargetType: instance

Targets:
  - Id:
      Ref: InstanceC1063A87

This confirms that the Target Group targets the EC2 instance
we created earlier.

The Target Group also contains:

Port: 8080
Protocol: HTTP

So the ALB receives the request on port 80 and forwards it
to the EC2 target on port 8080.


# ============================================================
# 5. Security Groups
# ============================================================

The network flow is controlled by the Security Groups:

Internet
   │
   │ :80
   ▼
LoadBalancerSG
   │
   │ :8080
   ▼
ApplicationSG
   │
   ▼
EC2

The Load Balancer Security Group allows incoming HTTP traffic
on port 80.

The Application Security Group allows traffic from the
Load Balancer Security Group on port 8080.

The EC2 instance is therefore not directly exposed to the
Internet.


# ============================================================
# 6. Network placement
# ============================================================

The ALB is placed in public subnets.

The EC2 instance remains in a private application subnet.

This gives us:

Internet
   ↓
Public ALB
   ↓
Private EC2


# ============================================================
# 7. What we learned from `cdk synth`
# ============================================================

The important practical step was not only writing the CDK code.

We used:

npm run build

npx cdk synth > template.yaml

and then inspected the generated CloudFormation.

This allowed us to verify the relationships between:

Load Balancer
Listener
Target Group
EC2
Security Groups
Subnets


# ============================================================
# 8. CDK abstraction
# ============================================================

A relatively small amount of CDK code such as:

ApplicationLoadBalancer
        ↓
addListener()
        ↓
addTargets()

can generate several interconnected CloudFormation resources.

The important IaC workflow is:

Requirement
    ↓
Research the CDK API
    ↓
Write TypeScript
    ↓
Build
    ↓
cdk synth
    ↓
Inspect CloudFormation
    ↓
Understand the actual AWS resources and relationships


# ============================================================
# 9. Final mental model
# ============================================================

Application Load Balancer
        │
        ▼
     Listener
     HTTP :80
        │
        ▼
   Target Group
   HTTP :8080
        │
        ▼
     EC2 Instance
   Private subnet

Security Groups control which traffic is allowed.

Route Tables determine where traffic can go.

The ALB accepts the client request.

The Listener receives the request.

The Target Group identifies the backend target.

The EC2 instance receives the forwarded application traffic.