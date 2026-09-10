# ============================================================
# PART 1 — AWS CDK FUNDAMENTALS
# ============================================================
#
# AWS CDK = Infrastructure as Code (IaC) framework from AWS.
# It allows us to define AWS infrastructure using a programming
# language such as TypeScript instead of using the AWS Console.
#
# Flow:
#
# TypeScript
#     ↓
# AWS CDK
#     ↓
# CloudFormation
#     ↓
# AWS resources
#
# Important distinction:
# - TypeScript     → programming language
# - CDK            → IaC framework
# - CloudFormation → AWS infrastructure engine
#
# CDK hierarchy:
#
# App
#  ↓
# Stack
#  ↓
# Construct
#  ↓
# AWS Resource
#
# App:
#   Root of the CDK application.
#   Example: const app = new cdk.App()
#
# Stack:
#   Deployable unit containing infrastructure.
#   Example: CloudCdkStack
#
# Construct:
#   Building block representing an AWS resource or group
#   of resources.
#   Example: new s3.Bucket(...)
#
# Mental model:
#   App contains Stacks
#   Stacks contain Constructs/resources
#
#
# ============================================================
# CDK PROJECT
# ============================================================
#
# Project initialization:
#
# cdk init app --language typescript
#
# Important files:
#
# cloud-cdk/
# ├── bin/
# ├── lib/
# ├── node_modules/
# ├── package.json
# ├── cdk.json
# └── tsconfig.json
#
# Main infrastructure code:
#   lib/cloud-cdk-stack.ts
#
# Run CDK commands from the project root where cdk.json exists.
#
#
# ============================================================
# CDK SYNTH
# ============================================================
#
# npx cdk synth
#
# Does NOT deploy anything to AWS.
# It converts TypeScript/CDK code into a CloudFormation template.
#
# TypeScript
#     ↓
# cdk synth
#     ↓
# CloudFormation YAML
#
# Save the output:
#
# npx cdk synth > template.yaml
#
# ">"  → overwrites the file
# ">>" → appends to the file
#
#
# ============================================================
# CREATING AN S3 BUCKET
# ============================================================
#
# Example:
#
# const bucket = new s3.Bucket(this, 'MyBucket', {
#     versioned: true,
#     encryption: s3.BucketEncryption.S3_MANAGED,
#     blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
#     lifecycleRules: [
#         {
#             expiration: cdk.Duration.days(30),
#         }
#     ],
# });
#
# General CDK construct syntax:
#
# new SomeConstruct(scope, id, props)
#
# - scope → where the construct belongs, usually "this"
# - id    → logical identifier inside the CDK tree
# - props → configuration/properties
#
# Example:
#
# new s3.Bucket(this, 'MyBucket', {...})
#
#
# ============================================================
# S3 PROPERTIES
# ============================================================
#
# versioned: true
#   → enables S3 versioning
#
# encryption: s3.BucketEncryption.S3_MANAGED
#   → enables server-side encryption using S3-managed keys
#
# blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL
#   → blocks public access to the bucket
#
# lifecycleRules:
#   → defines automatic lifecycle/expiration rules for objects
#
# cdk.Duration.days(30)
#   → represents a duration of 30 days
#
# CDK properties describe the DESIRED STATE of the infrastructure.
#
# ============================================================
# TYPESCRIPT TYPE INFERENCE
# ============================================================
#
# lifecycleRules is typed by CDK as:
#
# LifecycleRule[]
#
# Because TypeScript knows that the object belongs to
# BucketProps, it can infer the type automatically.
#
# Therefore, we don't need:
#
# const rule: s3.LifecycleRule = ...
#
# for a simple inline configuration.
