# ============================================================
# PART 2 — CDK TAGS AND VPC
# ============================================================
#
# CDK TAGS
#
# Tags can be applied to a specific resource:
#
# Tags.of(bucket).add("Environment", "development")
#
# Or to the entire Stack:
#
# Tags.of(this).add("Environment", "development")
#
# A tag applied to a Stack can propagate to applicable
# taggable child resources.
#
# Scalable approach:
#
# tags = {
#     Environment: "development",
#     Project: "cloud-engineering-starter",
#     Owner: "steve"
# }
#
# for (const [key, value] of Object.entries(tags)) {
#     Tags.of(this).add(key, value);
# }
#
# Object.entries() converts an object into key/value pairs.
# This separates configuration (the tags) from the logic
# that applies them.
#
#
# ============================================================
# STACK STRUCTURE
# ============================================================
#
# CloudCdkStack
# │
# ├── S3 Bucket
# ├── VPC
# └── Stack-level Tags
#
# Tags are applied to the Stack and can propagate to children.
#
#
# ============================================================
# VPC
# ============================================================
#
# Import:
#
# import * as ec2 from 'aws-cdk-lib/aws-ec2';
#
# Example:
#
# const vpc = new ec2.Vpc(this, 'TheVPC', {
#     ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
#     maxAzs: 2,
#     natGateways: 1,
# });
#
#
# VPC CIDR:
#
# 10.0.0.0/16
#
# → Defines the IPv4 address range of the VPC.
# → A /16 contains 65,536 addresses.
#
# Subnets use smaller ranges carved from this VPC range.
#
#
# ============================================================
# AVAILABILITY ZONES
# ============================================================
#
# maxAzs: 2
#
# → CDK can use up to 2 Availability Zones for the VPC.
#
# Conceptually:
#
# AWS Region
# │
# ├── AZ-1
# └── AZ-2
#
# Multiple AZs improve availability and resilience.
#
#
# ============================================================
# HIGH-LEVEL CDK CONSTRUCT
# ============================================================
#
# Important:
#
# new ec2.Vpc(...)
#
# is a HIGH-LEVEL construct.
#
# One CDK construct can generate MANY CloudFormation resources.
#
# Example with 2 AZs:
#
# 2 AZs
# ×
# 2 subnet types (Public + Private)
# =
# 4 Subnets
#
# Default configuration can also create:
#
# 2 NAT Gateways
# 4 Route Tables
# etc.
#
# Key concept:
#
# One high-level CDK construct
#          ↓
# Multiple CloudFormation resources
#
#
# ============================================================
# NAT GATEWAYS
# ============================================================
#
# The number of NAT Gateways is controlled by:
#
# natGateways
#
# Example:
#
# natGateways: 1
# → creates exactly 1 NAT Gateway
#
# natGateways: 0
# → creates no NAT Gateway
#
# IMPORTANT:
#
# natGateways: 1
#
# does NOT mean one NAT Gateway per AZ.
#
#
# ============================================================
# NAT GATEWAY — ARCHITECTURE / COST
# ============================================================
#
# NAT Gateways have a cost, so the configuration is an
# architecture + availability + cost decision.
#
# 2 NAT Gateways
# → better AZ-level resilience
# → higher cost
#
# 1 NAT Gateway
# → lower cost
# → less resilient to an AZ failure
#
#
# ============================================================
# CURRENT INFRASTRUCTURE
# ============================================================
#
# CloudCdkStack
# │
# ├── S3 Bucket
# │   ├── Versioning
# │   ├── Encryption
# │   ├── Block public access
# │   └── 30-day lifecycle rule
# │
# ├── VPC
# │   ├── CIDR: 10.0.0.0/16
# │   ├── maxAzs: 2
# │   └── natGateways: 1
# │
# └── Tags
#     ├── Environment = development
#     ├── Project = cloud-engineering-starter
#     └── Owner = steve
#
#
# ============================================================
# CDK WORKFLOW
# ============================================================
#
# 1. Requirement
#       ↓
# 2. Choose CDK construct/API
#       ↓
# 3. Write TypeScript IaC
#       ↓
# 4. npm run build
#       ↓
# 5. npx cdk synth
#       ↓
# 6. Inspect CloudFormation
#       ↓
# 7. Understand generated resources
#       ↓
# 8. Adjust configuration
#       ↓
# 9. Synth again
#
# So far:
#
# TypeScript
#     ↓
# AWS CDK
#     ↓
# cdk synth
#     ↓
# CloudFormation template
#
# We have NOT deployed anything to AWS yet.
#
# Key mindset:
# Don't just memorize CDK syntax.
# Understand what infrastructure the code actually creates.
# ============================================================
