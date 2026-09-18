
======================================================================

		🔐 Lesson 6 — IAM Role Trust Policy

======================================================================


Imagine you create this role:

S3ReadOnlyRole

You give it:

s3:GetObject

But then you need to answer:

Who can use this role?

You don't want just anyone to assume it.

The trust policy establishes that relationship.

Conceptually:


             Trust Policy
                  │
                  ▼
              ┌───────┐
              │ Role  │
              └───────┘
                  ▲
                  │
                EC2


So there are "two separate security questions":

Question 1:
What can the role do?
        ↓
Permissions Policy


Question 2:
Who can assume the role?
        ↓
Trust Policy


===================================================================

			🧪 Exercise 6

===================================================================


You have this situation:

EC2
 ↓
S3ReadRole
 ↓
s3:GetObject

The role has:

Permission:
s3:GetObject

And its trust policy allows:

EC2

to assume the role.

Now answer:

1. The permissions policy answers which question?

A. Who can assume the role?

B. What can the role do?

==> The permissions policy answers : B. what can the role do ?

2. The trust policy answers which question?

A. Who can assume the role?

B. What can the role do?

==> The trust policy answers : A. who can assume the role ?


3. If the role allows s3:GetObject but the trust policy does not allow
EC2 to assume the role, can this EC2 instance use the role?

==> No this EC2 instance cannot use it.


4. If the trust policy allows EC2 to assume the role, but the permissions
policy contains no S3 permission, can the EC2 instance read the S3 objects?

==> No, it cannot because the role has no S3 permissions.
