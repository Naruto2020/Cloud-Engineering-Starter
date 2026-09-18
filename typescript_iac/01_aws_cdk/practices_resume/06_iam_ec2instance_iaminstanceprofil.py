# ============================================================
# Exercise 11 — EC2 Instance + IAM Instance Profile
# ============================================================

# Goal
# ============================================================

Connect an EC2 instance to an existing IAM Role and understand
what CDK creates underneath the high-level `ec2.Instance` construct.


# ============================================================
# 1. IAM Instance Profile
# ============================================================

The correct AWS term is:

IAM Instance Profile

It is the mechanism that associates an IAM Role with an EC2 instance.

Conceptually:

EC2 Instance
     ↓
IAM Instance Profile
     ↓
IAM Role
     ↓
IAM Policy
     ↓
AWS Services


# ============================================================
# 2. What we discovered in CDK
# ============================================================

The CDK class is:

iam.InstanceProfile

It can explicitly associate a Role:

const instanceProfile = new iam.InstanceProfile(this, 'InstanceProfile', {
  role,
});

But with the high-level EC2 construct, we don't need to create
the Instance Profile ourselves.

We simply write:

const instance = new ec2.Instance(this, 'Instance', {
  vpc,
  instanceType: ...,
  machineImage: ...,
  role: userRole,
});


# ============================================================
# 3. What CDK does under the hood
# ============================================================

When we specify:

role: userRole

CDK automatically creates and connects the IAM Instance Profile
required by the EC2 instance.

The synthesized CloudFormation showed:

AWS::EC2::Instance
        │
        │ IamInstanceProfile
        ▼
AWS::IAM::InstanceProfile
        │
        │ Roles
        ▼
AWS::IAM::Role
        │
        ▼
AWS::IAM::Policy


# ============================================================
# 4. Our practical example
# ============================================================

We created:

IAM Role
→ trusted by `ec2.amazonaws.com`

IAM Policy
→ `s3:GetObject`

EC2 Instance
→ `t3.micro`
→ Amazon Linux 2023
→ private subnet
→ `role: userRole`


# ============================================================
# 5. What we wanted to discover
# ============================================================

The main lesson was not simply how to create an EC2 instance.

We wanted to understand what happens underneath:

High-level CDK:

new ec2.Instance(..., {
  role: userRole
})

↓

CDK generates the underlying CloudFormation resources:

EC2 Instance
IAM Instance Profile
IAM Role
IAM Policy


# ============================================================
# 6. Key lesson
# ============================================================

IAM Role
→ Identity and permissions.

IAM Instance Profile
→ Connects the Role to EC2.

EC2 Instance
→ Uses the Role through the Instance Profile.

CDK
→ Hides this implementation detail when using `ec2.Instance`.

The important mental model is:

EC2
 ↓
Instance Profile
 ↓
IAM Role
 ↓
Permissions
