
=======================================================================

		🔐 Lesson 7 — IAM Policy Evaluation

=======================================================================


So far, you've learned:

Authentication → Who are you?
Authorization → What are you allowed to do?
Least privilege → Give only the permissions required.
Permissions policy → What can the role do?
Trust policy → Who can assume the role?

Now we need to understand how AWS decides whether an action is 
actually allowed.

1. The basic rule

A useful simplified model is:

 Explicit Deny
     ↓
  overrides
     ↓
   Allow

In other words:

An explicit Deny overrides an Allow.

Example:

Policy 1:
Allow s3:GetObject

Policy 2:
Deny s3:GetObject

Result:

❌ Access denied

Even though there is an Allow.


2. Why is this important?

Imagine your company has a general policy:

{
  "Effect": "Allow",
  "Action": "s3:GetObject",
  "Resource": "*"
}

This gives broad read access.

But your security team wants to prevent access to a sensitive bucket:

{
  "Effect": "Deny",
  "Action": "s3:GetObject",
  "Resource": "arn:aws:s3:::company-secret/*"
}

Now:

Normal bucket
    ↓
Allow GetObject
    ↓
✅ Access



company-secret
    ↓
Allow GetObject
    +
Deny GetObject
    ↓
❌ Access denied


The Deny wins.



3. Explicit Deny vs no permission

This distinction is important.

Case A — No permission
Allow: nothing
Deny: nothing

Result:

❌ Access denied

Why?

Because AWS does not have an Allow.

Case B — Explicit Deny
Allow: s3:GetObject
Deny: s3:GetObject

Result:

❌ Access denied

Why?

Because the explicit Deny overrides the Allow.

So both situations can produce:

❌ Access denied

but for different reasons.



4. The simplified decision model

For our Cloud Security learning, use this mental model:

           AWS evaluates policies
                    │
                    ▼
          Is there an explicit Deny?
              /             \
            YES              NO
             │                │
             ▼                ▼
       ❌ DENY          Is there an Allow?
                            /       \
                          YES        NO
                           │          │
                           ▼          ▼
                       ✅ ALLOW    ❌ DENY

The key idea:

"Allow is required, but Deny has priority."


======================================================================

			✏️ Exercise

======================================================================


Question 1

A role has:

Allow: s3:GetObject

There is no Deny.

Can the role read the S3 object?

A. Yes
B. No

==> A

Question 2

A role has:

Allow: s3:GetObject
Deny:  s3:GetObject

Can the role read the S3 object?

A. Yes
B. No

==> B

Question 3

A role has:

Allow: s3:GetObject

But the resource is outside the scope of the policy.

Can the role read it?

A. Yes
B. No

==> B

Question 4

Which rule is correct?

A. Allow always wins over Deny
B. Deny always wins over Allow
C. The most recent policy wins

==> B

Question 5 — Cloud Engineer scenario

An application needs to read:

company-data/images/*

The IAM role has:

Allow: s3:GetObject
Resource: company-data/images/*

But another policy explicitly denies:

Deny: s3:GetObject
Resource: company-data/*

Can the application read the images?

==> No the application cannot read the image.

Explain why.

==> Because the second policy denies acces to all data
stored in company-data : "company-data/*"


🔑 Important takeaway

When troubleshooting AWS access, don't stop when you find an Allow.

You also need to ask:

"Is there an applicable explicit Deny somewhere?"

Your IAM foundation is now becoming quite strong:

Authentication
      ↓
Authorization
      ↓
Least Privilege
      ↓
IAM Policy
      ↓
IAM Role
      ↓
Trust Policy
      ↓
Policy Evaluation
      ↓
Explicit Deny
