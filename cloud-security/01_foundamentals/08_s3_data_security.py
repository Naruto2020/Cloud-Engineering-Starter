
========================================================================

		Lesson 10 — S3 Data Security

========================================================================

Imagine you're deploying an application that stores customer documents in an S3 bucket.

The bucket has encryption enabled, but someone accidentally makes it public.

Is the customer data secure just because it's encrypted at rest?

No. Encryption alone doesn't guarantee that the bucket is properly protected.

We'll explore how to secure the bucket through access controls and protective configuration.
Your first question
An S3 bucket contains private customer documents. Which configuration is the safest starting point?


A. Enable encryption and allow public access.


B. Enable encryption, block public access, and grant only the required permissions.


C. Block public access, but give every application s3:* permissions.


Check my answer
Choose the best answer and explain why in your own words.

==> B.  Enable encryption, block public access, and grant only the
required permissions.


This combines three important security controls.
1. Encryption

Protects stored data from unauthorized disclosure if someone obtains the underlying encrypted data.

2. Block Public Access

Helps prevent public exposure of S3 buckets and objects through public access policies or ACLs.

3. Least Privilege

Ensures that applications and users receive only the S3 permissions they actually need.

Why not the other options?

- A: Encryption doesn't make public access safe. Public access can expose
customer data.

- C: Blocking public access is good, but s3:* grants excessive
permissions and increases the blast radius of compromised credentials.




2. S3 Block Public Access

S3 provides a feature called Block Public Access.

It has four settings:

Setting	Purpose

BlockPublicAcls	Blocks new public ACLs
IgnorePublicAcls	Ignores existing public ACLs
BlockPublicPolicy	Blocks public bucket policies
RestrictPublicBuckets	Restricts access to buckets with public policies

You can configure these settings at two levels:
- AWS account level
- Individual bucket level
For private customer data, a common secure starting point is to enable 
all four settings at both levels where appropriate.



3. S3 Bucket Policy

Remember that an IAM permissions policy answers:
What can this identity do?

An S3 bucket policy is a resource-based policy. It answers:
Which principals can access this bucket, and under what conditions?

Example:
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/AppRole"
      },
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::company-private-data/*"
    }
  ]
}


This policy allows the specified IAM role to read objects in the bucket.

Notice three important fields:

- Principal: who receives access.
- Action: what they can do.
- Resource: which objects they can access.
The account ID and role ARN above are illustrative.



4. S3 Versioning

Another important security feature is Versioning.

Imagine your application stores:
customer-report.pdf


Someone accidentally overwrites it.

Without versioning, recovering the previous version may be difficult or 
impossible.

With versioning:

customer-report.pdf
    │
    ├── Version 1
    ├── Version 2
    └── Version 3 (current)


Important: Versioning helps with recovery, but it is not a complete 
backup strategy. A user with sufficient permissions can permanently 
delete object versions.



5. S3 Security: Putting everything together
