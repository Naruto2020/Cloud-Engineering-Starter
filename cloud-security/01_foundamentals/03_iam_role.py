=======================================================================

	🔐 Cloud Security — Lesson 5 IAM Roles

=======================================================================


This is a very important AWS concept for a Cloud Engineer.

The problem we want to solve is:


" How can an AWS service access another AWS service securely "

" without storing long-term AWS credentials? "

1. The bad approach: access keys on the server

Imagine an EC2 instance needs to read from S3.

A beginner might do this:

EC2
 ↓
AWS Access Key
AWS Secret Key
 ↓
S3

For example, storing credentials in:

~/.aws/credentials

or:

AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

This is dangerous because if the server is compromised, the attacker
may obtain the credentials.

And if those credentials have excessive permissions:

Attacker
   ↓
Steals credentials
   ↓
AWS
   ↓
💥 Potentially large blast radius


2. The better approach: IAM Role

Instead, we attach an IAM Role to the EC2 instance.

        IAM Role
           │
           │
           ▼
         EC2
           │
           │ temporary credentials
           ▼
          S3

The EC2 instance receives temporary credentials that AWS manages.

You don't need to manually put a long-term AWS access key on the server.


3. Example

Suppose your application only needs to read:

s3://company-data/reports/*

You create an IAM Role with a policy such as:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::company-data/reports/*"
}

Then:

EC2
 ↓
IAM Role
 ↓
s3:GetObject
 ↓
company-data/reports/*

The application can read the required objects.
assuming no other permissions grant those actions.


4. Why this is better


Long-term access key


EC2
 ↓
Permanent credentials
 ↓
S3

Problems:

credentials can leak
credentials must be rotated
developers may accidentally commit them
difficult to manage at scale


IAM Role


EC2
 ↓
IAM Role
 ↓
Temporary credentials
 ↓
S3

Benefits:

no hard-coded long-term credentials
AWS manages temporary credentials
easier credential management
works well with least privilege
better suited to AWS services


🧠 Important distinction

An IAM User generally represents a person or long-lived identity.

An IAM Role is an identity that can be assumed by trusted entities such as:

EC2
Lambda
ECS
another AWS account
IAM users
CI/CD systems

For example:

EC2
 ↓
Assume IAM Role
 ↓
Temporary credentials
 ↓
S3

=======================================================================

		🧪 Exercise 5

=======================================================================


You have this architecture:

EC2 application
       ↓
       S3

The application needs to read objects from one specific S3 bucket.

A developer proposes two solutions.

Solution A

Store an AWS access key and secret key inside the EC2 server:

EC2
 ↓
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
 ↓
S3


Solution B

Create an IAM Role with:

s3:GetObject

for the specific S3 bucket/path and attach the role to EC2.

Questions

1. Which solution is more secure: A or B?

==> Solution B is more secure


2. Why?

==> Because the IAM Role ll provide temporary credentials to the EC2
instead of hard-coding an AWS access and secret key on the server
which can create a large blast radius in case one attacker catch them


3. What security principle should we apply when creating the role?

==> We should apply the princple of least privilege


4. If the application only needs to read objects, should we give it 
s3:*? Why or why not?

==> No we should not give it s3:*. Because in case of an attack,the
blast radius would not be limited


🔑 One important technical detail

There are actually two policies involved with an IAM Role that you need 
to distinguish.

1. Permissions policy

This answers:

What can the role do?

For example:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::company-data/reports/*"
}

Meaning:

Role
 ↓
CAN
 ↓
s3:GetObject
 ↓
company-data/reports/*


2. Trust policy

This answers:

Who is allowed to assume the role?

For example, conceptually:

EC2
 ↓
allowed to assume
 ↓
IAM Role

So remember:

IAM Role
   │
   ├── Permissions Policy
   │       ↓
   │   "What can I do?"
   │
   └── Trust Policy
           ↓
       "Who can assume me?"

This distinction is very important.
