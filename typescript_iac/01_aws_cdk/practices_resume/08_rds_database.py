
=========================================================================

			Exercise 13 — RDS Database

=========================================================================


Now we'll add the database layer to the architecture you've already 
built.


🎯 Objective

Extend the architecture to:

Internet
   │
   │ :80
   ▼
  ALB
   │
   │ :8080
   ▼
  EC2
   │
   │ :5432
   ▼
  RDS PostgreSQL

The important security principle is:

Internet
   X
   │
   └──── RDS

The database should remain private.


Only the application layer (EC2 / ApplicationSG) should be allowed to connect to the database.

# Step 1 — Create the Database Security Group

Before implementing the RDS database, create a dedicated Security Group for the database.

This is important because the database needs its own network access rules.

The Database Security Group controls:

- who can connect to the database
- which protocol/port can be used
- where the traffic is coming from

The Security Group is created separately first:

const databaseSG = new ec2.SecurityGroup(this, 'DatabaseSG', {
  vpc,
  description: 'Database Security Group',
  allowAllOutbound: true,
});

# Step 2 — Add the Database ingress rule

The database should only accept PostgreSQL traffic from the application Security Group.

databaseSG.addIngressRule(
  applicationSG,
  ec2.Port.tcp(5432),
  'Allow PostgreSQL traffic from application'
);

This means:

ApplicationSG
    │
    │ TCP :5432
    ▼
DatabaseSG
    │
    ▼
RDS

The Internet is not allowed to connect directly to the database.

The important idea is that the ingress rule is attached to DatabaseSG, but the source is ApplicationSG.

# Important CDK pattern

When implementing AWS resources with CDK, some configuration is prepared first and then passed to the resource as a property.

For example, we create the Database Security Group first:

const databaseSG = new ec2.SecurityGroup(...);

Then we configure its ingress rule:

databaseSG.addIngressRule(...);

Then, when creating the RDS instance, we attach the Security Group:

securityGroups: [databaseSG]

So the RDS resource uses the Security Group that was already configured.

This pattern is useful because the security configuration is separated from the database definition.

# Step 3 — Research the CDK API

Before writing the RDS code, we identify the appropriate CDK module and high-level construct.

Module:

aws-cdk-lib/aws-rds

Main construct:

rds.DatabaseInstance

Other APIs used:

- rds.DatabaseInstance
- rds.DatabaseInstanceEngine
- rds.PostgresEngineVersion
- rds.Credentials
- securityGroups
- storageEncrypted
- publiclyAccessible
- vpc
- vpcSubnets

The objective is not only to copy an example, but to understand which CDK properties correspond to the infrastructure requirements.

# Step 4 — Create the PostgreSQL RDS instance

The database is created inside the existing VPC.

Important configuration:

- PostgreSQL engine
- small development instance
- private subnets
- not publicly accessible
- encryption enabled
- dedicated Database Security Group
- credentials managed through Secrets Manager

Conceptually:

const database = new rds.DatabaseInstance(this, 'Database', {
  engine: rds.DatabaseInstanceEngine.postgres(...),
  vpc,
  vpcSubnets: {
    subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
  },
  securityGroups: [databaseSG],
  publiclyAccessible: false,
  storageEncrypted: true,
  ...
});

# Step 5 — Database credentials

We do not hard-code a plaintext database password in the CDK code.

RDS/CDK can generate the credentials and store them in AWS Secrets Manager.

The resulting architecture is conceptually:

Secrets Manager
    │
    │ username + generated password
    ▼
RDS PostgreSQL

This avoids putting the database password directly in the source code.

# Step 6 — Database encryption

storageEncrypted: true

This enables encryption at rest for the RDS storage.

It protects data stored on the database infrastructure, including things such as:

- database data
- indexes
- automated backups
- snapshots
- transaction logs

This is different from encryption in transit.

storageEncrypted protects data at rest.

It does not mean that every connection to PostgreSQL is automatically encrypted in transit.

# Step 7 — Keep the database private

publiclyAccessible: false

The database should remain inside the private part of the VPC.

The intended traffic path is:

Internet
    │
    ▼
ALB
    │
    ▼
EC2
    │
    ▼
RDS

Not:

Internet
    │
    └──────────► RDS

The application is the component that needs database access.

# Step 8 — Security model

The architecture now has multiple Security Groups:

LoadBalancerSG
    │
    │ HTTP :80/:443
    ▼
Load Balancer

ApplicationSG
    │
    │ HTTP :8080
    ▼
EC2

DatabaseSG
    │
    │ PostgreSQL :5432
    ▼
RDS

The important security relationship is:

ApplicationSG → DatabaseSG :5432

This means the database trusts traffic coming from the application Security Group, rather than allowing the entire Internet.

# Step 9 — Build and synthesize

As with the previous exercises, we do not deploy the infrastructure.

First:

npm run build

Then:

npx cdk synth > template.yaml

The objective is to inspect the CloudFormation generated by CDK.

This allows us to verify that our TypeScript configuration actually produces the infrastructure we intended.

# Step 10 — Inspect the generated CloudFormation

The synthesized template confirms several important things.

RDS:

Type: AWS::RDS::DBInstance

Engine:

postgres

Instance class:

db.t3.small

Private configuration:

PubliclyAccessible: false

Encryption:

StorageEncrypted: true

Security Group:

VPCSecurityGroups:
  - DatabaseSG

Database subnet:

The DBSubnetGroup references the private application/database subnets.

Credentials:

MasterUserPassword resolves through Secrets Manager rather than being stored as plaintext in the CDK source.

# Step 11 — Verify the Database Security Group

The synthesized template also shows the Database Security Group and its ingress rule.

The important relationship is:

DatabaseSG
    │
    └── TCP 5432
          Source: ApplicationSG

This confirms that only the application Security Group is authorized to initiate PostgreSQL connections to the database.

# Important lesson about CDK abstractions

The TypeScript code is a high-level description of the infrastructure.

CDK then generates several CloudFormation resources behind the scenes.

For example:

DatabaseInstance
      │
      ├── AWS::RDS::DBInstance
      ├── DB Subnet Group
      ├── Security Group association
      ├── Secrets Manager resources
      └── other supporting resources/configuration

Therefore, one high-level CDK construct can result in several CloudFormation resources.

This is why `cdk synth` is important: it lets us understand what CDK is actually creating.

# Practical workflow

For each AWS component, the workflow is:

Requirement
    ↓
Research the CDK API
    ↓
Identify the required construct
    ↓
Create supporting resources
    ↓
Configure relationships
    ↓
Implement the main resource
    ↓
npm run build
    ↓
npx cdk synth
    ↓
Inspect CloudFormation
    ↓
Verify that the generated infrastructure matches the requirement

For RDS specifically:

1. Create DatabaseSG
2. Add ingress rule from ApplicationSG on TCP 5432
3. Research aws-rds APIs
4. Create DatabaseInstance
5. Attach DatabaseSG through securityGroups
6. Place RDS in private subnets
7. Disable public accessibility
8. Enable storage encryption
9. Use managed credentials
10. Build
11. Synthesize
12. Inspect the generated CloudFormation

# Final architecture

                         Internet
                            │
                         HTTP :80
                            ▼
                  ┌──────────────────┐
                  │       ALB        │
                  │  LoadBalancerSG  │
                  │      Public      │
                  └────────┬─────────┘
                           │
                       HTTP :8080
                           ▼
                  ┌──────────────────┐
                  │       EC2        │
                  │  ApplicationSG   │
                  │     Private      │
                  └────────┬─────────┘
                           │
                     PostgreSQL :5432
                           ▼
                  ┌──────────────────┐
                  │       RDS        │
                  │   DatabaseSG     │
                  │    PostgreSQL    │
                  │     Private      │
                  │     Encrypted    │
                  └──────────────────┘

Security flow:

Internet → ALB
ALB → EC2
EC2 → RDS

No direct Internet → RDS access.

# Main concepts practiced

- Creating a dedicated Security Group for a database
- Defining ingress rules between Security Groups
- Allowing PostgreSQL only on TCP 5432
- Connecting application and database layers through Security Groups
- Using RDS PostgreSQL with CDK
- Placing RDS in private subnets
- Disabling public database access
- Managing credentials through Secrets Manager
- Enabling encryption at rest
- Understanding the difference between network security and data encryption
- Understanding high-level CDK constructs
- Using `npm run build` to validate TypeScript
- Using `cdk synth` to inspect generated CloudFormation
- Verifying that the generated infrastructure matches the intended architecture