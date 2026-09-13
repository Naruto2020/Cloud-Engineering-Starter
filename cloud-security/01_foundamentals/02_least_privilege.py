===================================================================

🔐 Lesson 3 — Principle of Least Privilege

===================================================================


This is one of the most important security principles for Cloud Engineers.

Definition

Give a user, application, or service only the permissions it actually needs — and nothing more.

For example, imagine an application only needs to read files from S3.

❌ Bad:

Application
    ↓
S3: *

The application can potentially:

Read       ✅
Write      ✅
Delete     ✅
Create     ✅
Modify     ✅

That's excessive privilege.

Better:

Application
    ↓
s3:GetObject

Now:

Read       ✅
Write      ❌
Delete     ❌
Create     ❌

This reduces the blast radius if the application is compromised.

☁️ Real Cloud Example

Imagine:

EC2
 ↓
IAM Role
 ↓
S3

The EC2 application only needs to download configuration files.

Its role should ideally allow something like:

s3:GetObject

on a specific bucket/path.

Not:

s3:*

and definitely not:

=======================================================================

*
🧪 Exercise 3

=======================================================================


You have a web application running on EC2.

The application needs to:

read images from an S3 bucket
not upload images
not delete images
not access other S3 buckets

Which permission is the best?

# A. s3:*

# B. s3:GetObject
# Resource: *

C. s3:GetObject
Resource: specific-bucket/images/*

# D. *


# And explain why you chose it.

Because C allow application just to read images from a s3 specific bucket

======================================================================

🔑 New concept: Blast Radius

======================================================================

This is an important Cloud Security term.

If an application is compromised:


Broad permissions
      ↓
Attacker gets many permissions
      ↓
💥 Large blast radius



With least privilege:

Limited permissions
      ↓
Attacker gets limited permissions
      ↓
💥 Smaller blast radius


So when designing AWS IAM, don't only ask:

"Does this permission make the application work?"

Also ask:

"What could an attacker do if this application were compromised?"

That's the security mindset we're building.

=======================================================================

Lesson 4
IAM Policies

=======================================================================

Now we move from the concepts to real AWS IAM policy structure.

An IAM policy answers:

Who can do what, on which resource?

A simplified policy looks like this:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::my-bucket/images/*"
}

Let's break it down.

1. Effect

Defines whether the action is:

Allow

or

Deny

Example:

"Effect": "Allow"

means:

This action is permitted.


2. Action


Defines what operation is allowed or denied.

Examples:

s3:GetObject
s3:PutObject
s3:DeleteObject

Meaning:

GetObject    → read an object
PutObject    → upload/write an object
DeleteObject → delete an object

You can also have multiple actions:

"Action": [
  "s3:GetObject",
  "s3:PutObject"
]


3. Resource

Defines which AWS resource the permission applies to.

For example:

"Resource": "arn:aws:s3:::my-bucket/images/*"

This means the permission applies to objects inside:

my-bucket/images/

Not necessarily everything in the account.

This is another application of least privilege.



4. Principal



Principal identifies who or what is making the request.

You'll see it particularly in resource-based policies, such as S3 bucket 
policies.

For example:

"Principal": {
  "AWS": "arn:aws:iam::123456789012:user/Steve"
}

means the policy applies to that IAM user.

🧠 The four things to remember

When looking at an IAM policy, ask:

Effect
  ↓
Allow or Deny?

Action
  ↓
What can they do?

Resource
  ↓
On what?

Principal
  ↓
Who?

A useful mental model:

Principal
    │
    │ can
    ▼
  Action
    │
    │ on
    ▼
 Resource

with Effect determining whether the action is allowed or denied.

=========================================================================

🧪 Exercise — IAM Policy Analysis

=========================================================================

Look at this policy:

{
  "Effect": "Allow",
  "Action": [
    "s3:GetObject",
    "s3:PutObject"
  ],
  "Resource": "arn:aws:s3:::company-data/reports/*"
}

Answer these questions:

# 1. Is the policy allowing or denying access?

The policy allowing acces

# 2. What can the principal do?

The principal can read and edit


# 3. Can it delete objects?

No it cannot


# 4. Can it access objects outside:  company-data/reports/*

No it cannot access object outside : company-data/reports/*


# 5. Does this policy follow the principle of least privilege
# better than giving: s3:*

Yes this policy follow the principle of least privilege better
then the given one: s3:*


# Explain your answer.
# 1. Is the policy allowing or denying access?

The policy allow acces

# 2. What can the principal do?

The principal can read and upload/write objects


# 3. Can it delete objects?

No it cannot


# 4. Can it access objects outside:  company-data/reports/*

No it cannot access object outside : company-data/reports/*


# 5. Does this policy follow the principle of least privilege
# better than giving: s3:*

Yes this policy follow the principle of least privilege better
then the given one: s3:*


# Explain your answer.

the policy target a s3 specific bucket data and grant only 
specific actions while the given one s3:* will grant all S3 actions
