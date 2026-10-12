
========================================================================

		🔐 Lesson 9 — AWS Data Security: Encryption

========================================================================


Now we move from "Who can access the resource?" to:

"What happens if someone gets access to the underlying data?"

This is where encryption becomes important.


1. What is encryption?

Encryption transforms readable data (plaintext) into unreadable data 
(ciphertext) using a cryptographic key.


Conceptually:

Plaintext
   │
   │ Encryption + Key
   ▼
Ciphertext


To recover the original data:

Ciphertext
   │
   │ Decryption + Key
   ▼
Plaintext


The goal is to make the data unusable to someone who does not have the 
necessary key/access.


2. Encryption at Rest

Data at rest means data stored somewhere.

Examples:

S3 objects
EBS volumes
RDS databases
backups
database snapshots

Example:

Application
    │
    ▼
    S3
    │
    ▼
Encrypted object

If someone obtains the underlying stored data, encryption helps protect
its contents.


Example

Without encryption:

S3
 └── customer-data.txt
       └── readable data

With encryption:

S3
 └── customer-data.txt
       └── encrypted data


3. Encryption in Transit

Data in transit means data moving between systems.

For example:

Browser
   │
   │ HTTPS / TLS
   ▼
Application
   │
   │ TLS
   ▼
Database

TLS protects data while it travels across the network.


For example:

HTTP  ❌
HTTPS ✅

HTTPS uses TLS to protect the communication.


4. At Rest vs In Transit

This distinction is fundamental.

Situation	Protection

Data stored in S3	Encryption at rest

Data stored on EBS	Encryption at rest

Data stored in RDS	Encryption at rest

Browser → API	Encryption in transit

EC2 → S3 over HTTPS	Encryption in transit

Application → Database over TLS	Encryption in transit


Real systems often need both.

                 HTTPS / TLS
User ───────────────────────────► Application
                                  │
                                  │ TLS
                                  ▼
                              Database
                                  │
                                  ▼
                            Encrypted at rest



5. AWS KMS

Now we introduce an important AWS security service:

AWS Key Management Service (KMS).

KMS is used to create and manage cryptographic keys that AWS services 
and applications can use for encryption.

Simplified:

              AWS KMS
                 │
                 │ encryption key
                 ▼
              S3 / EBS / RDS



You don't normally need to manually implement cryptographic algorithms yourself.

AWS services can integrate with KMS.

6. SSE-S3 vs SSE-KMS

For S3, you'll encounter two important server-side encryption approaches.

SSE-S3

AWS manages the encryption keys for you.

Conceptually:

S3
 │
 └── AWS-managed encryption

This is simple and requires less key-management responsibility.

SSE-KMS

S3 uses AWS KMS to manage the encryption key.

S3
 │
 └── AWS KMS
       │
       └── KMS key

This gives you additional control over key management and access to the 
keys.

For example, you can control who is allowed to use a KMS key through 
IAM/KMS policies.


7. Very important: Encryption ≠ Authorization

This is one of the most important concepts in this lesson.

Suppose an IAM role has:

s3:GetObject

but the S3 object is encrypted with a KMS key that the role cannot use.

The application may still fail to decrypt/read the object.

Conceptually:

IAM
 │
 └── Can access S3 object? ✅
              │
              ▼
         KMS encryption
              │
              └── Can use KMS key? ❌
                       │
                       ▼
                  Access fails

So when troubleshooting encrypted AWS data, you may need to check both:

1. Do I have permission to access the resource?
2. Do I have permission to use the encryption key?


🧠 Exercise

Answer in English and explain your reasoning.

Question 1

A customer database is stored on an encrypted EBS volume.

Is this:

A. Encryption at rest
B. Encryption in transit

==> A Encryption at rest

Question 2

A user accesses an application using HTTPS.

Is this:

A. Encryption at rest
B. Encryption in transit

==> B Encryption in transit

Question 3

What is the main purpose of AWS KMS?

A. Manage cryptographic keys

B. Manage Linux users

C. Manage VPC routing tables


==> A Manage cryptographic keys


Question 4

An S3 object is encrypted using SSE-KMS.

Which AWS service is involved in managing the encryption key?

A. IAM

B. KMS

C. EC2

==> B KMS

Question 5 — Important scenario

An EC2 application's IAM role has:
s3:GetObject

The application tries to read an S3 object encrypted with SSE-KMS.

However, the role does not have permission to use the relevant KMS key.

Can the application successfully read/decrypt the object?

A. Yes

B. No

Explain why.

==> B No , Because The role do not have permission to use the relevant
KMS key


Question 6 — Cloud Engineer thinking

Why is this statement incorrect?

"The data is encrypted, so we don't need IAM permissions."

Give me your reasoning rather than just saying 
"because encryption and IAM are different."

==> The statement is incorrect because encryption is different to 
authorization or permission : encryption protect data itself while 
permissions allow who can access this data 
