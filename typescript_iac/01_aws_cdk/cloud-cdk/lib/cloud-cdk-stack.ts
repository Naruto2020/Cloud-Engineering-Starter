import * as cdk from 'aws-cdk-lib/core';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';
import {Tags} from 'aws-cdk-lib';
import * as ec2 from 'aws-cdk-lib/aws-ec2';


// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class CloudCdkStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, 'MyBucket', {
      versioned: true,
      encryption: s3.BucketEncryption.S3_MANAGED,
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      lifecycleRules: [
        {
          expiration: cdk.Duration.days(30),
        }
      ],
    });

    const tags = {
       Environment: "development",
       Project: "cloud-engineering-satrter",
       Owner: "steve"
    };

    for (const [key, value] of Object.entries(tags)) {
       Tags.of(this).add(key, value);
    }

    const vpc = new ec2.Vpc(this, 'TheVPC', {
       ipAddresses: ec2.IpAddresses.cidr('10.0.0.0/16'),
       maxAzs: 2,
       natGateways: 1,
    });
  }
}
