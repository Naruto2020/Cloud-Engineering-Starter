# ============================================================
# Cloud Security — Lesson 1
# ============================================================


# ============================================================
# The CIA Triad
# ============================================================

# The CIA Triad is one of the fundamental concepts of
# cybersecurity.
#
# CIA stands for:
#
# C = Confidentiality
# I = Integrity
# A = Availability
#
# These three principles help us think about how to protect
# systems and data.


# ------------------------------------------------------------
# 1. Confidentiality
# ------------------------------------------------------------

# Confidentiality means protecting information from
# unauthorized access.
#
# Main question:
#
#     Who can see the data?
#
#
# Example:
#
#     AWS RDS
#        ↓
#     Database
#        ↓
#     User passwords
#     Customer data
#     Payment information
#
#
# We do NOT want:
#
#     Internet → Database ❌
#
# Instead, we want something like:
#
#     Application → Database ✅
#
#
# In cloud environments, confidentiality can be protected
# using mechanisms such as:
#
#     - IAM
#     - Encryption
#     - Private subnets
#     - Security groups
#     - Access control
#
#
# Example:
#
# If an S3 bucket containing customer data is publicly
# accessible:
#
#     Confidentiality is compromised.
#
#
# The problem is that unauthorized people may be able
# to see the data.


# ------------------------------------------------------------
# 2. Integrity
# ------------------------------------------------------------

# Integrity means making sure that data cannot be modified
# or deleted by unauthorized users.
#
# Main question:
#
#     Who can modify the data?
#
#
# Example:
#
#     Application
#         ↓
#     Database
#         ↓
#     User balance = $100
#
#
# If an attacker changes the value to:
#
#     User balance = $10,000
#
#
# Then the integrity of the data has been compromised.
#
#
# Typical mechanisms used to protect integrity include:
#
#     - IAM permissions
#     - Database permissions
#     - Checksums
#     - Digital signatures
#     - Audit logs
#     - Versioning
#
#
# The goal is to make sure that data remains accurate
# and that unauthorized changes can be detected or prevented.


# ------------------------------------------------------------
# 3. Availability
# ------------------------------------------------------------

# Availability means that systems and data remain accessible
# when users need them.
#
# Main question:
#
#     Can we use the system when we need it?
#
#
# Example:
#
#     Users
#       ↓
#     Load Balancer
#       ↓
#     Application
#       ↓
#     Database
#
#
# Imagine that one server crashes:
#
#     Server 1 ❌
#     Server 2 ✅
#     Server 3 ✅
#
#
# The application can continue working because other servers
# are still available.
#
#
# This is why cloud architectures often use:
#
#     - Multiple instances
#     - Load balancers
#     - Auto Scaling
#     - Backups
#     - Redundancy
#     - Multi-AZ architectures
#     - Disaster recovery
#
#
# The goal is to avoid a single failure making the entire
# service unavailable.


# ============================================================
# Quick Summary
# ============================================================

# Confidentiality
#     → Prevent unauthorized access.
#     → "Who can see it?"
#
# Integrity
#     → Prevent or detect unauthorized changes.
#     → "Who can modify it?"
#
# Availability
#     → Keep systems and data accessible.
#     → "Can we use it when needed?"
#
#
# A secure cloud environment should consider ALL THREE:
#
#     Confidentiality + Integrity + Availability
#
# These three principles form the CIA Triad.


# ============================================================
# Exercise 1 — The CIA Triad
# ============================================================

# For each situation, determine which principle of the CIA
# Triad is affected:
#
#     C = Confidentiality
#     I = Integrity
#     A = Availability
#
#
# Remember:
#
# Confidentiality
#     → Unauthorized people can access the data.
#     → "Who can see it?"
#
# Integrity
#     → Data is modified or deleted without authorization.
#     → "Who can modify it?"
#
# Availability
#     → Systems or data are no longer accessible when needed.
#     → "Can we use it when needed?"


# ------------------------------------------------------------
# 1.
# ------------------------------------------------------------

# An S3 bucket containing customer documents is accidentally
# made public.
#
# Question:
# Which CIA principle is affected?
#
C = Customer documents should be in private storage
# I = ?
# A = ?


# ------------------------------------------------------------
# 2.
# ------------------------------------------------------------

# An attacker changes the price of a product in the database
# from $20 to $1.
#
# Question:
# Which CIA principle is affected?
#
# C = ?
I = Data should be change by someone authenticate with authorization
# A = ?


# ------------------------------------------------------------
# 3.
# ------------------------------------------------------------

# An application server crashes and there is no backup server.
#
# Question:
# Which CIA principle is affected?
#
# C = ?
# I = ?
A = Data should stay avaiable at all


# ------------------------------------------------------------
# 4.
# ------------------------------------------------------------

# An employee who should only read data is given permission
# to delete database records.
#
# Question:
# Which CIA principle is affected?
#
# C = ?
I = employee without authorization should not edit or delete data
# A = ?


# ------------------------------------------------------------
# 5.
# ------------------------------------------------------------

# A ransomware attack encrypts the company's files and users
# can no longer access them.
#
# Question:
# Which CIA principle is affected?
#
# C = ?
I = Only profil with authorization should manage data
A = Data should always avaiable to users


# ============================================================
# Goal
# ============================================================

# For each situation, identify the CIA principle that is
# primarily affected.
#
# Some situations can affect more than one principle.
# Try to identify the MAIN security property affected first.


# ============================================================
# Cloud Security — Lesson 2
# Authentication vs Authorization
# ============================================================

# Authentication and Authorization are two fundamental
# concepts in cybersecurity and AWS IAM.
#
# They are related, but they answer two different questions:
#
#     Authentication → "Who are you?"
#     Authorization  → "What are you allowed to do?"


# ------------------------------------------------------------
# 1. Authentication — "Who are you?"
# ------------------------------------------------------------

# Authentication is the process of verifying your identity.
#
# In other words:
#
#     The system checks whether you really are who you claim
#     to be.
#
#
# Examples of authentication mechanisms:
#
#     - Username + Password
#     - SSH Key
#     - MFA (Multi-Factor Authentication)
#     - Access Key
#     - Certificate
#
#
# Example:
#
#     Steve
#       ↓
#     Username + Password
#       ↓
#     Identity verified ✅
#
#
# At this point, the system knows:
#
#     "This person is Steve."
#
# But authentication does NOT tell us what Steve is allowed
# to do.
#
# It only establishes his identity.


# ------------------------------------------------------------
# 2. Authorization — "What are you allowed to do?"
# ------------------------------------------------------------

# After authentication, the system checks the permissions
# associated with the authenticated identity.
#
# In other words:
#
#     The system asks:
#
#         "What can Steve do?"
#
#
# Example:
#
#     Steve
#       ↓
#     Authenticated
#       ↓
#     What can Steve do?
#       ↓
#     S3:ReadObject   ✅
#     S3:DeleteObject ❌
#
#
# Steve is authenticated, so the system knows who he is.
#
# Then authorization determines which actions he is allowed
# or not allowed to perform.
#
#
# In this example:
#
#     ReadObject  → allowed
#     DeleteObject → denied
#
#
# This is where permissions and access policies become
# important in AWS IAM.


# ============================================================
# Quick Summary
# ============================================================

# Authentication
#     → Verifies your identity.
#     → "Who are you?"
#     → Identity
#
#
# Authorization
#     → Determines what you are allowed to do.
#     → "What are you allowed to do?"
#     → Permissions
#
#
# Easy way to remember:
#
#     Authentication = WHO you are
#     Authorization  = WHAT you can do
#
#
# Example:
#
#     Steve logs in
#          ↓
#     Authentication
#          ↓
#     "This is Steve." ✅
#          ↓
#     Authorization
#          ↓
#     "Steve can read S3 objects,
#      but cannot delete them." ✅


# ============================================================
# Exercise 2 — Authentication vs Authorization
# ============================================================

# Classify each situation as:
#
#     AUTHENTICATION
#     or
#     AUTHORIZATION
#
#
# Remember:
#
# Authentication
#     → "Who are you?"
#     → Verifies your identity.
#
# Authorization
#     → "What are you allowed to do?"
#     → Checks your permissions.


# ------------------------------------------------------------
# 1.
# ------------------------------------------------------------

# You enter your username and password to access AWS.
#
# Question:
# Is this AUTHENTICATION or AUTHORIZATION?
#
Answer:
AUTHENTICATION


# ------------------------------------------------------------
# 2.
# ------------------------------------------------------------

# AWS checks whether you have permission to delete an S3
# object.
#
# Question:
# Is this AUTHENTICATION or AUTHORIZATION?
#
Answer:
AUTHORIZATION


# ------------------------------------------------------------
# 3.
# ------------------------------------------------------------

# You use MFA to prove your identity.
#
# Question:
# Is this AUTHENTICATION or AUTHORIZATION?
#
Answer:
AUTHENTICATION


# ------------------------------------------------------------
# 4.
# ------------------------------------------------------------

# An IAM policy allows a Lambda function to read from
# DynamoDB.
#
# Question:
# Is this AUTHENTICATION or AUTHORIZATION?
#
Answer:
AUTHORIZATION


# ------------------------------------------------------------
# 5.
# ------------------------------------------------------------

# You use an SSH key to prove that you are allowed to connect
# to a server.
#
# Question:
# Is this AUTHENTICATION or AUTHORIZATION?
#
Answer:
AUTHENTICATION


# ============================================================
# Goal
# ============================================================

# For each situation, identify whether the system is:
#
#     1. Verifying WHO someone is
#        → AUTHENTICATION
#
#     2. Checking WHAT someone is allowed to do
#        → AUTHORIZATION
#
#
# Quick reminder:
#
#     Username + Password → Authentication
#     MFA                 → Authentication
#     SSH Key             → Authentication
#
#     IAM Policy          → Authorization
#     Permission to delete → Authorization
