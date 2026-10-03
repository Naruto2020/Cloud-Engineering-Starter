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
# 3. Connecting the EC2 to the Target Group
# ============================================================

The EC2 instance itself is represented by the CDK
ec2.Instance construct.

To use this EC2 as a Target Group target, we created an
InstanceTarget:

const instanceTarget =
  new elasticloadbalancingv2_targets.InstanceTarget(instance);

InstanceTarget adapts the EC2 instance so that it can be used
as a target by the Load Balancer Target Group.

The relationship is:

ec2.Instance
     │
     ▼
InstanceTarget
     │
     ▼
Target Group
     │
     ▼
ALB

Then the target is passed to addTargets():

listener.addTargets('ApplicationTarget', {
  port: 8080,
  targets: [instanceTarget],
});

This means that the Target Group uses our EC2 instance as its
backend target and sends traffic to it on port 8080.

The important distinction is:

instance

→ represents the EC2 resource.

InstanceTarget

→ represents that EC2 instance as a Load Balancer target.


# ============================================================
# 4. CloudFormation resources
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
# 5. Target Group verification
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

The important relationship is:

ALB
 ↓
Listener :80
 ↓
Target Group
 ↓
EC2 instance :8080


# ============================================================
# 6. Security Groups
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
# 7. Network placement
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
# 8. What we learned from `cdk synth`
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

We specifically verified that the Target Group uses the
EC2 instance as an instance target and that traffic is sent
to port 8080.


# ============================================================
# 9. CDK abstraction
# ============================================================

A relatively small amount of CDK code such as:

ApplicationLoadBalancer
        ↓
addListener()
        ↓
InstanceTarget
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
# 10. Final mental model
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
  InstanceTarget
        │
        ▼
   EC2 Instance
   Private subnet

Security Groups control which traffic is allowed.

Route Tables determine where traffic can go.

The ALB accepts the client request.

The Listener receives the request.

The Target Group identifies the backend target.

InstanceTarget represents the EC2 instance as a Target Group
target.

The Target Group forwards the request to the EC2 instance
on port 8080.