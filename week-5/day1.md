# Lecture Plan

1. Elastic Beanstalk
---

### Introduction

- managed service for deploying the applications. 
- application code is the responsibility of the developer and the underlying architecture is managed by Elastic Beanstack (ELB, ASGs, health monitoring etc)
- charged for underlying resources

**Elastic Benastalk Components:**

1. Application: collection of components (environment, version and configuration)
2. Application Version: iteration of application code.


**Environment**

aws resources running a specifc application version. 
   - Tiers: Web Server and Worker
   - ex: dev, test, prod.

**supported platforms**

- Java SE
- Java with Tomcat
- Go
- .NET core / windows server
- Node.js
- PHP
- Python
- Ruby
- Docker containers

**Deploying an application using elastic beanstalk**


1. Navigate to elastic beanstalk
2. Create an application
3. Create an environment

**config**

1. tier: web server
2. java 17
3. presets: single instance
4. create a role for eb
5. select a key pair (create one if not available)
6. create a role for ec2 with permissions `AWSElasticBeanstalkMulticontainerDocker`, `AWSElasticBeanstalkWebTier`, `AWSElasticBeanstalkWorkerTier`
7. skip steps
8. select t2.micro
9. add an env varible `SERVER_PORT=5000`
10. create


### Elastic Beanstalk CLI

[eb cli](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)


1. clone 

```
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup
```

2. install eb cli

```
python .\aws-elastic-beanstalk-cli-setup\scripts\ebcli_installer.py
```


### Deployment & Deployment modes

1. All at once

   - Fastest deployment
   - has downtime
   - no additional cost

2. Rolling
   - applications are updated based on the bucket size.
   - no additional cost

3. Rolling with additional batches
   -  a bucket size is specified to roll out the updates.
   -  runs in full capacity
   -  additional cost based on the bucket size.
  
4. Immutable

   - New code is deployed in new ASG
   - High cost
   - quick rollback 
5. Blue Gren
   - new enviorment with new deployment. Route53 to redirect the traffic.
   - not a feature in Elastic Beanstack
6. Traffic Splitting (canary)

   - temp ASG with same capacity.
   - small % is routed to temp ASG.
   - temp ASG health is monitored.
   - no downtime
   - option to rollback
   - zero downtime.

[elastic beanstalk deployments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.deploy-existing-version.html)



### Lifecycle policy

- upto 1000 app versions are stored.
- old application versions are phased out using the lifecycle policies.
    - time
    - space
- versions in use will not be deleted and there is an option to not to delete the source code in S3.

### Extensions

- .extensions/ dir is the root source for eb extensions.
- yaml/json format. file extension is `.config`
- `option_settings` to modify the default settings, adding additional config related to RDS, ElastiCache and DynamoDB.
- resouces managed by `.ebextensions` get deleted if env is deleted.

### Cloning

- used to clone the existing env.
- all config is preserved
- swap enviorment is used to swap an existing env to other.

### Migration


- an ELB cant be modified from one type to other using the clone.   
- To migrate an ELB a new enviorment with new ELB configuration should be created.
- For RDS, creating a new RDS with the backup snapshot is the right approach for database migration.
- Route53 or CNAME swap is used to swap the env along with a deployment startergy after testing the new env.

**Activities:**

1. Deploy a springboot app  using eb console or cli.