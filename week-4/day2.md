# Lecture Plan

- AWS Services
- Console, CLI, SDK's
- Compute
  - EC2
  - AMI
  - EBS
  - EFS
  - Security Groups
  - ASG
---

### AWS Services Overview

**Compute:**

- EC2
- Elastic beanstalk
- ECS, App Sevice, Fargate and EKS

**Storage:**

- S3
- EBS
- EFS

**Database:**

- RDS
- Aurora
- ElastiCache
- DynamoDB


**Networking:**

- VPC
- ELB, API gateway
- Cloud Font, Route53

### Console, CLI and SDKs


One can access AWS account using console, CLI and SDK. 

1. console: UI
2. CLI: aws cli and access keys
3. AWS SDK: boto 3 (python)


[AWS cli installation](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)


## Compute

- computational resources. processing power, storage, networking, memory etc. 

examples:

1. EC2
2. Elastic bean stalk
3. Containers: ECS, EKS, Fargate, App runnner
4. Serverless: Lambda

### EC2 (Elastic Compute Cloud)

#### Instance type:

General Purpose: balance of copute, memory and networking resources.

ex: to deploy web applications

Compute optimized: applicatios that require high performance procerrs.

ex: gaming, ML, batch processing.

Memory optimised: applications that require large ammounts of RAM.


Accelerated Computing: hardware accessors. 

ex: floating point number, graphics processing.

HPC Optimized: High perfomance computing

ex: complex simulations (fem), deep learning.

Storage Optimized: High read and write to local staoge. 

ex: big data and DWH.


**Features:**

1. fixed performce:
2. burstable performance



[instance type](https://aws.amazon.com/ec2/instance-types/)

#### pricing models


- on demand
- savings plan
- spot instances:
- reserved:
  - on-demand reservations
  - capacity blocks for ML
  - dedicated hosts

<i><b>Note</b>

- aws ec2, ebs are billed per seconds. 
- per sec billing is supported for AWS Linux, Redhat, ubuntu and Ubantu pro.
</i>

#### AMI

- Amazon Machine image is a supported image from AWS to launch and instance.
- AMI includes, EBS snapshots, launch permisions, block device mapping
- custom AMI can be created.
- AMIs can be sold and bought from the market place/

#### EBS

- Elastic Block Store is provides scalable and high performance storage for EC2.

- Volumes : attachable storage volumes for EC2.

**types:**

  - gp3
  - gp3 throughput
  - gp3  iops
  - gp2
  - io2 storage
  - io2 iops


- Snapshots : backup for EBS at a particular of time. 

  - standard
  - archive

- EBS benifits include, scalability, backup and recovery, availability, archiving and data protection.

#### ssh to ec2

#### Security Groups

**Inbound and outbound rules:**


#### ASG

**Auto Scaling:** 

- Auto Scaling Groups


### Policy creation





**pricing guide**



---

**Activities:**

1. creating ec2 using console (optional - cli/sdk).
2. creating the run script with the congiguration to deploy your project.
3. mounting ebs volume
4. configuring the security groups for specific ip range, specific ip and port ranges
5. creating the AMI and creating an instance from the custom AMI
6. Creating ASG and adding the policies.