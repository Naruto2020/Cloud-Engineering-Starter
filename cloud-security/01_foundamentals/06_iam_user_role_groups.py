
==================================================================

🔐 Lesson 8 — IAM Users vs Roles vs Groups

==================================================================

Before moving beyond IAM, we need to clearly distinguish Users, 
Groups, and Roles.

This matters because in real Cloud Engineering work, you'll
constantly decide:

Who needs access, and what identity mechanism should they use?


1. IAM User

An IAM User represents a specific identity that can authenticate to
AWS.

Conceptually:

Steve
  ↓
IAM User
  ↓
AWS

A user can have credentials such as:

Password for AWS Console
Access keys for programmatic access

However, for human users, AWS generally recommends using federated
identities / IAM Identity Center rather than creating individual
long-lived IAM users for everyday access.

For our learning model, think:

User = a specific human identity in IAM


2. IAM Group

A Group is a collection of IAM users.

For example:

Developers
├── Alice
├── Bob
└── Steve

You can attach permissions to the group:

Developers
     ↓
Allow:
s3:GetObject

Then the users in the group receive those permissions through their
group membership.

This is useful when several users need the same permissions.

Important:

A group is not an identity that assumes roles.

Think:

User → belongs to → Group

not:

Group → logs into AWS

===================================================================

3. IAM Role

A Role is different.

A role does not represent a permanent person.

It is an identity that can be assumed by a trusted principal.

For example:

EC2
  ↓
assumes
  ↓
IAM Role
  ↓
S3

Or:

GitHub Actions
       ↓
   assumes
       ↓
   IAM Role
       ↓
 AWS resources

Or:

Account A
    ↓
assumes
    ↓
Role in Account B
    ↓
S3

This is why roles are extremely important in Cloud Engineering.

4. Compare them
IAM component	Main purpose
User	Represents an identity, traditionally a specific person
Group	Organizes users and applies shared permissions
Role	Provides temporary permissions to a trusted principal

A useful mental model:

USER
  │
  └── belongs to → GROUP
                     │
                     └── shared permissions


ROLE
  │
  ├── Trust Policy
  │       ↓
  │   Who can assume me?
  │
  └── Permissions Policy
          ↓
      What can I do?


==================================================================


🧠 Exercise

Question 1

Which IAM component represents a collection of users?

A. User
B. Group
C. Role

==> B

Question 2

Which IAM component is designed to be assumed by EC2?

A. User
B. Group
C. Role

==> C

Question 3

An application running on EC2 needs to read objects from S3.

Which approach is preferable?

A. Store an AWS access key and secret key on the EC2 instance.

B. Attach an IAM role to the EC2 instance with the required S3 
permissions.

==> B

Question 4

What is the main purpose of an IAM Group?

A. Allow EC2 to assume an identity.

B. Organize users and apply shared permissions.

C. Provide temporary credentials to Lambda.

==> B


Question 5 — Cloud Engineer scenario

You have:

20 developers

All of them need:

Read-only access to a specific S3 bucket

Would you create 20 separate permission policies, or would an IAM
Group be useful?

==> just one IAM group is need

Explain why.

Because is more  efficient to create one IAM group and then add all developers .if i ll want to edit permisions i ll do it just 
once

Question 6 — Important distinction

Complete this:

Trust Policy = Who ll assume IAM Role

Permissions Policy = what is allow , and on which ressouces
