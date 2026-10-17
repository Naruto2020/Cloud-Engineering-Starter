# ============================================================
# Exercise 14.1 — Create a Private ECR Repository with AWS CDK
# ============================================================

# Goal
# ============================================================

Create a private Amazon ECR repository using AWS CDK and
understand how Docker images are stored and accessed by AWS
container services.

We also learned why private repositories, image scanning,
versioning, and IAM permissions are important for security.

We used `cdk synth` to inspect the generated CloudFormation.
No infrastructure was deployed.


# ============================================================
# 1. Why ECS Cannot Access a Local Docker Image
# ============================================================

A Docker image built on a local computer exists only in the
local Docker environment unless it is uploaded elsewhere.

ECS/Fargate cannot directly access an image stored only on
our local machine.

The image must be stored in a container registry that AWS
can access.

The workflow is:

Build Docker image locally
          ↓
Push image to Amazon ECR
          ↓
Reference the image in an ECS Task Definition
          ↓
ECS starts a task using the image
          ↓
Fargate provides the compute capacity to run the container

Important distinction:

Docker builds the image.

ECR stores the image.

ECS orchestrates and manages the tasks.

Fargate runs the containers without requiring us to manage
the underlying EC2 instances.


# ============================================================
# 2. Why Use a Private ECR Repository?
# ============================================================

We chose a private ECR repository for security reasons.

A Docker image can contain proprietary application code and
details about the application's architecture.

A private repository allows us to control who can access
the images through IAM permissions and ECR repository policies.

The Principle of Least Privilege applies:

Each identity should receive only the permissions required
to perform its job.

A private repository does not automatically make an image
secure. We must also configure access controls, scan images
for vulnerabilities, and avoid embedding secrets in images.


# ============================================================
# 3. Research the AWS CDK API
# ============================================================

Before writing the code, we consulted the AWS CDK ECR
documentation.

We identified:

Module:
aws-cdk-lib/aws-ecr

Construct:
ecr.Repository

Property:
imageScanOnPush: true

The Repository construct creates an ECR repository.

The imageScanOnPush property enables image scanning when
images are pushed, subject to the supported scanning
configuration and AWS ECR capabilities.

This is an example of the workflow we follow when learning
a new AWS service through CDK:

Research the official documentation
          ↓
Identify the construct
          ↓
Find the required properties
          ↓
Implement the resource
          ↓
Synthesize and inspect CloudFormation


# ============================================================
# 4. Implement the ECR Repository
# ============================================================

First, we imported the ECR module:

import * as ecr from 'aws-cdk-lib/aws-ecr';

Then, inside the CDK Stack constructor, we created the
repository:

const repository = new ecr.Repository(this, 'TestRepository', {
  repositoryName: 'my-app',
  imageScanOnPush: true,
});

This creates a private ECR repository named `my-app` and
enables image scanning on push.

Important distinction:

'TestRepository'

→ CDK construct ID, used to identify the construct in the stack.

repositoryName: 'my-app'

→ Actual name of the ECR repository in AWS.

The construct ID and the AWS resource name do not have to
be identical.


# ============================================================
# 5. Build and Synthesize
# ============================================================

After implementing the code, we ran:

npm run build

npx cdk synth

The build checks the TypeScript code.

The synthesis step translates the CDK application into
CloudFormation.

We did not deploy the stack.

The generated template allows us to inspect the AWS resources
that CDK intends to create.


# ============================================================
# 6. Verify the Generated CloudFormation
# ============================================================

We inspected the synthesized template and found:

Type: AWS::ECR::Repository

Properties:
  ImageScanningConfiguration:
    ScanOnPush: true
  RepositoryName: my-app

This confirms that CDK generated an ECR repository with the
expected configuration.

The properties mean:

AWS::ECR::Repository

→ CloudFormation resource type for an ECR repository.

RepositoryName: my-app

→ Name assigned to the repository.

ScanOnPush: true

→ Enables scanning when an image is pushed, according to
  the configured ECR scanning capabilities.

We also observed:

UpdateReplacePolicy: Retain
DeletionPolicy: Retain

These policies tell CloudFormation to retain the repository
if the resource is replaced or the stack is deleted.

This is important because an ECR repository may contain
images we do not want to lose automatically.

Retaining a repository can also leave resources behind that
must be managed separately.


# ============================================================
# 7. Understanding an ECR Image URI
# ============================================================

An ECS Task Definition needs to identify the image to run.

An image URI can look like:

123456789012.dkr.ecr.eu-west-1.amazonaws.com/my-app:v1

Its components are:

123456789012
→ AWS account ID.

dkr.ecr.eu-west-1.amazonaws.com
→ ECR registry endpoint for the region.

my-app
→ Repository name.

v1
→ Image tag identifying a version of the image.

The complete image URI identifies the repository and the
image version that the task should use.

The account ID and region must correspond to the intended
ECR registry.


# ============================================================
# 8. Image Tags and Versioning
# ============================================================

One repository can contain multiple versions of an image:

my-app:v1
my-app:v2
my-app:v3

An ECS Task Definition can reference a specific tag to
indicate which image version should be used.

Tags make it easier to distinguish application releases.

However, a tag is not necessarily immutable.

For example, `latest` can point to different images over time.

For more reliable deployments, an image digest can identify
the exact image content.

This helps ensure that a deployment uses the intended image
rather than a different image later assigned to the same tag.


# ============================================================
# 9. ECR Permissions and Least Privilege
# ============================================================

Permission to pull an image does not automatically grant
permission to push an image.

Pull and push operations require different IAM permissions.

Examples of permissions used to pull images include:

ecr:BatchGetImage
ecr:GetDownloadUrlForLayer
ecr:BatchCheckLayerAvailability

Examples of permissions used to push images include:

ecr:InitiateLayerUpload
ecr:UploadLayerPart
ecr:CompleteLayerUpload
ecr:PutImage

The exact permissions depend on the operation and workflow.

We can control access using IAM policies and ECR repository
policies.

The Principle of Least Privilege means:

A user or role that only needs to download images should not
automatically receive permission to publish new images.

This reduces the risk of unauthorized image modifications
or malicious images being introduced into the repository.


# ============================================================
# 10. ECR Security Considerations
# ============================================================

We learned three important security concepts.

Private repository:

Controls who can access the images.

Image scanning:

Helps identify vulnerabilities in container images.

IAM permissions:

Control which identities can pull or push images.

These controls serve different purposes.

Image scanning does not automatically prevent every
vulnerable image from being deployed.

Access controls do not guarantee that an image is free
from vulnerabilities.

We must combine access control, image scanning, secure
image-building practices, and appropriate deployment policies.


# ============================================================
# 11. What We Practiced
# ============================================================

We practiced how to:

- Research the official AWS CDK documentation.
- Identify the ecr.Repository construct.
- Configure imageScanOnPush.
- Create a private ECR repository in CDK.
- Build the TypeScript project.
- Synthesize the CDK stack into CloudFormation.
- Verify the generated AWS::ECR::Repository resource.
- Distinguish a CDK construct ID from an AWS resource name.
- Understand CloudFormation retention policies.
- Understand ECR image URIs and image tags.
- Distinguish image storage from container execution.
- Apply the Principle of Least Privilege to image access.
- Understand the role of image scanning in container security.

No deployment was performed.


# ============================================================
# 12. Final Mental Model
# ============================================================

Developer
    │
    │ Build
    ▼
Docker Image
    │
    │ Push
    ▼
Private Amazon ECR Repository
    │
    │ Pull image
    ▼
ECS Task Definition
    │
    │ Specifies how to run the container
    ▼
ECS Service
    │
    │ Maintains the desired number of tasks
    ▼
AWS Fargate
    │
    ▼
Running Container

ECR stores the image.

ECS manages and orchestrates the tasks.

The Task Definition specifies the image and container
configuration.

Fargate provides the managed compute capacity.

IAM controls who can access or modify the images.

Image scanning helps identify vulnerabilities before
or during the image lifecycle.