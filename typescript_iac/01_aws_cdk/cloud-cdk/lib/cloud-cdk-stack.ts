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
      subnetConfiguration: [
        {
          cidrMask: 24,
          name: 'ingress',
          subnetType: ec2.SubnetType.PUBLIC,
        },
        {
          cidrMask: 24,
          name: 'application',
          subnetType: ec2.SubnetType.PRIVATE_WITH_EGRESS,
        },
      ]
    });

    const loadBalancerSG = new ec2.SecurityGroup(this, 'LoadBalancerSG', {
      vpc: vpc,
      description: 'Load Balancer Security Group',
      allowAllOutbound: false,
    });

    
    loadBalancerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(443),
      'Allow HTTPS traffic'
    )

    loadBalancerSG.addIngressRule(
      ec2.Peer.anyIpv4(),
      ec2.Port.tcp(80),
      'Allow HTTP traffic'
    )
    
    const applicationSG = new ec2.SecurityGroup(this, 'ApplicationSG', {
      vpc: vpc,
      description: 'Application Security Group',
      allowAllOutbound: true,
    });

    applicationSG.addIngressRule(
      loadBalancerSG,
      ec2.Port.tcp(8080),
      'Allow HTTP traffic from LB'
    )

  }
}

