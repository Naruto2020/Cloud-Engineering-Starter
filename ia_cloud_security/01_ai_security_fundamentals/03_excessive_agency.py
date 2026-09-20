
==================================================================

🚀 Lesson 3 — Excessive Agency

==================================================================

Now we're going to move from:

"Can I manipulate the AI?"

to:

"What can the AI actually do if I manipulate it?"

This is a crucial AI security concept.

Imagine an AI assistant has these tools:

AI Agent
   │
   ├── read_email()
   ├── send_email()
   ├── read_s3()
   ├── delete_s3()
   ├── create_ec2()
   └── modify_iam()

That's a huge attack surface.

If the AI is manipulated, the attacker potentially gains access to
all those capabilities.

Compare that with:

AI Agent
   │
   └── read_specific_s3_objects()

Much safer.

This leads us to an important principle:

An AI agent should have the minimum capabilities necessary to
perform its task.

Next we'll distinguish prompt injection, excessive agency,
and privilege escalation, because these three concepts can easily
get mixed together.



The key question now is:

What happens if an attacker successfully manipulates an AI agent?

The answer depends heavily on what the agent is allowed to do.

1. What is an AI Agent?

A basic LLM mainly generates text:

User
 ↓
LLM
 ↓
Response

An AI agent can use tools:

User
 ↓
AI Agent
 ├── Email
 ├── Database
 ├── S3
 ├── APIs
 └── Cloud services

The agent can therefore take actions, not just generate answers.

2. What is Excessive Agency?

Excessive agency means giving an AI system more capabilities,
permissions, or autonomy than it needs for its intended task.

For example:

AI Agent
 │
 ├── read_email()
 ├── send_email()
 ├── read_s3()
 ├── delete_s3()
 ├── create_ec2()
 └── modify_iam()

Imagine the actual business requirement is only:

"Read invoices from one S3 bucket."

Then these permissions are unnecessary:

delete_s3()
create_ec2()
modify_iam()
send_email()

That's excessive agency.


==============================================================

3. Why is it dangerous?

Consider this attack chain:

Malicious document
       ↓
Indirect Prompt Injection
       ↓
LLM manipulated
       ↓
AI Agent
       ↓
Powerful tools
       ↓
Cloud damage

The prompt injection is the initial manipulation.

The excessive permissions determine what the manipulated agent can actually do.

This distinction is important.

4. Three concepts

==> " Prompt Injection "

Manipulation of the AI's instructions/context.

"Ignore previous instructions..."

↓

AI behavior may be manipulated.

==> " Excessive Agency "

The AI has too many capabilities or too much autonomy.

AI Agent
 ↓
10 powerful tools

when it only needs:

AI Agent
 ↓
1 read-only tool


==> " Privilege Escalation "

An attacker or compromised component gains privileges beyond what it should have.

For example:

AI Agent
 ↓
ReadOnlyRole
 ↓
somehow obtains
 ↓
AdministratorAccess

That's privilege escalation.


5. Connect this to AWS IAM

This should look familiar from your IAM Cross-Account Access project.

Suppose:

AI Agent
    ↓
IAM Role
    ↓
S3:GetObject
    ↓
arn:aws:s3:::company-documents/private/*

That's much more controlled than:

AI Agent
    ↓
IAM Role
    ↓
AdministratorAccess

And notice something important:

Least privilege applies at multiple levels.

AI Security
     │
     ├── Minimum AI capabilities
     │
     ├── Minimum tool access
     │
     └── Minimum IAM permissions


🧪 Exercise 3

Question 1  What is an AI agent?

==> An AI agent is an autonom AI system (ex: basic LLM) wich
    can use tools , take action to achieve a goal.


Question 2 An AI agent only needs to read files from:

s3://company-invoices/

But it has:

s3:GetObject
s3:PutObject
s3:DeleteObject
ec2:*
iam:*

Is this excessive agency? Why?

==> Yes this is an excessive agency, because 
    AI agent has too much capability than its really need.


Question 3 What's the difference between prompt injection and 
excessive agency?

==> prompt injesction is an attack where AI agent recieve malicious 
    instructions that can change its context.

    excessive agency is when an agent has too much capability
    or autonomy than it need.


Question 4 Consider:

Malicious document
       ↓
Prompt Injection
       ↓
AI Agent
       ↓
S3:GetObject
       ↓
company-documents/*

The AI agent is manipulated, but it only has s3:GetObject.

What limits the potential impact of the attack?

==> Principle of least privilege limit the impact because 
AI agent has only permission to read specific s3 object.

Question 5 Complete:

Prompt injection controls what the AI may __do___, while
excessive agency determines what the AI may __capable of doing____.


🧠 One thing I want you to retain

Imagine:

Prompt Injection
       ↓
"Delete all invoices!"
       ↓
AI Agent
       ↓
Does it have s3:DeleteObject?

If NO:

Attack attempted
      ↓
Permission denied
      ↓
Impact limited

If YES:

Attack attempted
      ↓
Permission allowed
      ↓
Potential damage


That is why your IAM / least-privilege knowledge is directly 
relevant to AI Security.

Next concept: AI Agent Security Architecture

We'll now combine the concepts you've learned:

Prompt Injection + RAG + IAM + Least Privilege + Tool permissions

and design a small secure AI agent architecture before moving into 
more advanced topics like tool poisoning and privilege escalation.
