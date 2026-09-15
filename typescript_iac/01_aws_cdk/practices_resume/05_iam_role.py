
============================================================
PART 5 — IAM ROLE FOR EC2
============================================================

GOAL

Give an EC2 instance permission to access AWS services
without storing AWS access keys inside the application
or server.

Example:

      EC2
       │
       │ assumes IAM Role
       ↓
   IAM Role
       │
       │ permission
       ↓
      S3


============================================================
IAM MENTAL MODEL
============================================================

IAM = Identity and Access Management.

IAM controls:

  WHO/WHAT can access AWS
      ↓
  WHICH ACTION
      ↓
  ON WHICH RESOURCE


Four fundamental IAM concepts:

1. USER
2. GROUP
3. ROLE
4. POLICY


------------------------------------------------------------
IAM USER
------------------------------------------------------------

Represents an identity in an AWS account.

Historically, IAM Users were commonly associated with
long-term credentials such as passwords and access keys.

Today, AWS generally recommends federation / IAM Identity
Center for human users when possible.

Mental model:

Human
  ↓
IAM User / federated identity
  ↓
AWS


------------------------------------------------------------
IAM GROUP
------------------------------------------------------------

A collection of IAM Users.

Example:

Developers
├── Alice
├── Bob
└── Steve

A policy can be attached to the group so that its users
receive the corresponding permissions.

IMPORTANT:

IAM Groups contain USERS.
They do not contain IAM Roles.


------------------------------------------------------------
IAM ROLE
------------------------------------------------------------

An IAM Role is an identity with permissions that can be
ASSUMED by another principal.

Roles commonly provide temporary credentials.

Example:

EC2
  ↓
assumes
  ↓
IAM Role
  ↓
permissions
  ↓
S3

This avoids storing permanent AWS access keys on the EC2
instance.


An IAM Role has two important aspects:

IAM Role
│
├── Trust Policy
│     → WHO can assume the role?
│     → Example: EC2
│
└── Permission Policy
      → WHAT can the role do?
      → Example: s3:GetObject


------------------------------------------------------------
IAM POLICY
------------------------------------------------------------

A policy defines permissions.

A typical policy specifies:

  Effect
  Action
  Resource

Example:

Effect:   Allow
Action:   s3:GetObject
Resource: arn:aws:s3:::my-company-data/*

Meaning:

Allow
  ↓
s3:GetObject
  ↓
on objects inside my-company-data

Policies can be attached to Users, Groups, and Roles.


============================================================
EXERCISE — EC2 ROLE WITH S3 ACCESS
============================================================

Requirement:

Create an IAM Role that:

- can be assumed by EC2
- allows s3:GetObject
- applies to S3 objects
- does NOT require an EC2 instance yet


CDK concepts used:

iam.Role
iam.ServicePrincipal
iam.PolicyStatement
iam.Effect


Example architecture:

             EC2
              │
              │ assume role
              ↓
         UserRole
              │
              │ Allow
              ↓
       s3:GetObject
              │
              ↓
    my-company-data/*


============================================================
SYNTHESIS VERIFICATION
============================================================

After writing the CDK code:

npm run build
npx cdk synth > template.yaml

Then inspect the generated CloudFormation.


Expected IAM Role:

Type:
  AWS::IAM::Role

Trust relationship:

Principal:
  Service: ec2.amazonaws.com

Meaning:

EC2 is allowed to assume the role.


Expected permission:

Action:
  s3:GetObject

Effect:
  Allow

Resource:
  arn:aws:s3:::my-company-data/*


============================================================
CDK CAN CREATE ADDITIONAL RESOURCES
============================================================

Important observation:

We explicitly created one IAM Role:

new iam.Role(...)

But CloudFormation can contain additional IAM Roles.

Example:

CustomVpcRestrictDefaultSGCustomResourceProviderRole

This role was generated automatically by CDK for an
internal/custom resource associated with the VPC.

Therefore:

Number of IAM Roles in template
      ≠
Number of IAM Roles explicitly written in our code

CDK high-level constructs can generate additional
underlying AWS resources.


============================================================
SECURITY GROUP vs IAM
============================================================

These two concepts solve DIFFERENT security problems.


SECURITY GROUP
----------------

Controls NETWORK TRAFFIC.

Main questions:

  Can traffic reach this resource?
  From where?
  On which port/protocol?

Example:

Internet
   │
   │ TCP 443
   ↓
Load Balancer


IAM
----------------

Controls AWS AUTHORIZATION.

Main questions:

  Who/what is making the request?
  What AWS action can it perform?
  On which AWS resource?

Example:

EC2
  ↓
IAM Role
  ↓
s3:GetObject
  ↓
S3 object


============================================================
IAM IDENTITY CENTER
============================================================

IAM Identity Center is mainly used for HUMAN access to
AWS accounts and applications.

Conceptually:

Human
  ↓
IAM Identity Center
  ↓
Permission Set
  ↓
IAM Role
  ↓
Temporary credentials
  ↓
AWS resources

It provides centralized/federated access instead of
relying on long-term IAM User credentials for humans.


============================================================
KEY MENTAL MODEL
============================================================

Security Group:

  "Can this NETWORK TRAFFIC reach the resource?"

IAM:

  "Is this IDENTITY authorized to perform this AWS ACTION
   on this RESOURCE?"


Example:

Internet
   │
   │ TCP 443
   ↓
Load Balancer
   │
   │ Security Group allows TCP 8080
   ↓
EC2
   │
   │ IAM Role
   ↓
S3
   │
   └── s3:GetObject


============================================================
KEY CLOUD ENGINEER LESSON
============================================================

Do not think:

  "EC2 has an S3 password."

Think:

  EC2
    ↓
  assumes Role
    ↓
  receives temporary credentials
    ↓
  IAM evaluates the request
    ↓
  Policy allows/denies the action

This is a fundamental AWS security pattern:

Prefer IAM Roles and temporary credentials for workloads
instead of embedding long-term AWS access keys in
applications or servers.
============================================================


