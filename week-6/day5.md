# Lecture Plan

1. AWS X-ray
2. Kenisis
3. CodePipeline


---


# X Ray


- Troubleshooting performance (bottlenecks)
- Understand dependencies in a microservice architecture
- Pinpoint service issues
- Review request behavior
- Find errors and exceptions
- Are we meeting time SLA?
- Where I am throttled?
- Identify users that are impacted


### Tracing


- Tracing is an end to end way to following a “request”
- Each component dealing with the request adds its own “trace”
- Tracing is made of segments (+ sub segments)
- Annotations can be added to traces to provide extra-information
- Ability to trace:
  - Every request
  - Sample request (as a % for example or a rate per minute)
- X-Ray Security:
  - IAM for authorization
  - KMS for encryption at rest


- Segments: each application / service will send them
- Subsegments: if you need more details in your segment
- Trace: segments collected together to form an end-to-end trace
- Sampling: decrease the amount of requests sent to X-Ray, reduce cost
- Annotations: Key Value pairs used to index traces and use with filters
- Metadata: Key Value pairs, not indexed, not used for searching
- The X-Ray daemon / agent has a config to send traces cross account:
- make sure the IAM permissions are correct – the agent will assume the role
- This allows to have a central account for all your application tracing



### Sampling Rules

- With sampling rules, you control the amount of data that you record
- You can modify sampling rules without changing your code
- By default, the X-Ray SDK records the first request each second, and
five percent of any additional requests.
- One request per second is the reservoir, which ensures that at least
one trace is recorded each second as long the service is serving
requests.
- Five percent is the rate at which additional requests beyond the
reservoir size are sampled.



### API's

**Write**


- PutTraceSegments: Uploads segment documents to AWS X-Ray
- PutTelemetryRecords: Used by the AWS
    - X-Ray daemon to upload telemetry.
    - SegmentsReceivedCount,
    - SegmentsRejectedCounts,
    - BackendConnectionErrors…
- GetSamplingRules: Retrieve all sampling rules (to know what/when to send)
- GetSamplingTargets & GetSamplingStatisticSummaries: advanced
- The X-Ray daemon needs to have an IAM policy authorizing the correct API calls tofunction correctly

**Read**

- GetServiceGraph: main graph
- BatchGetTraces: Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request.
- GetTraceSummaries: Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. To get the full traces,pass the trace IDs to BatchGetTraces.
- GetTraceGraph: Retrieves a service graph for one or more specific traceIDs.


### Kenisis

- Makes it easy to collect, process, and analyze streaming data in real-time
- Ingest real-time data such as: Application logs, Metrics, Website clickstreams, IoT telemetry data
- Kinesis Data Streams: capture, process, and store data streams
- Kinesis Data Firehose: load data streams into AWS data stores
- Kinesis Data Analytics: analyze data streams with SQL or Apache Flink
- Kinesis Video Streams: capture, process, and store video streams

#### Data Streams


- Kinesis Data Streams
- Retention between 1 day to 365 days
- Ability to reprocess (replay) data
- Once data is inserted in Kinesis, it can’t be deleted (immutability)
- Data that shares the same partition goes to the same shard (ordering)
- Producers: AWS SDK, Kinesis Producer Library (KPL), Kinesis Agent
- Consumers:
  - Write your own: Kinesis Client Library (KCL), AWS SDK
  - Managed: AWS Lambda, Kinesis Data Firehose, Kinesis Data Analytics,

**Kinesis Producers**
- Puts data records into data streams
- Data record consists of:
- Sequence number (unique per partition-key within shard)
- Partition key (must specify while put records into stream)
- Data blob (up to 1 MB)
- Producers:
  - AWS SDK: simple producer
  - Kinesis Producer Library (KPL): C++, Java, batch, compression, retries
  - Kinesis Agent: monitor log files
  - Write throughput: 1 MB/sec or 1000 records/sec per shard
  - PutRecord API
  - Use batching with PutRecords API to reduce costs & increase throughput


# AWS CodePipeline



### CodeCommit

- Version control is the ability to understand the various changes that
happened to the code over time (and possibly roll back)
- All these are enabled by using a version control system such as Git
- A Git repository can be synchronized on your computer, but it usually is
uploaded on a central online repository
- Benefits are:
- Collaborate with other developers
- Make sure the code is backed-up somewhere
- Make sure it’s fully viewable and auditable

1. create a repo in code commit


2. create service specific credentials

```
aws iam create-service-specific-credential --user-name name --service-name codecommit.amazonaws.com
```

3. clone the repository


4. create manifests file and deployment.yaml to it

5. implement push commands for revhire-user-service and revhire-job-service



### CodePipeline
- Visual Workflow to orchestrate your CICD
- Source – CodeCommit, ECR, S3, Bitbucket, GitHub
- Build – CodeBuild, Jenkins, CloudBees, TeamCity
- Test – CodeBuild, AWS Device Farm, 3rd party tools, …
- Deploy – CodeDeploy, Elastic Beanstalk, CloudFormation, ECS, S3, …
- Invoke – Lambda, Step Functions
- Consists of stages:
- Each stage can have sequential actions and/or parallel actions
- Example: Build è Test è Deploy è Load Testing è …
- Manual approval can be defined at any stage

### Code Build


- A fully managed continuous integration (CI) service
- Continuous scaling (no servers to manage or provision – no build queue)
- Compile source code, run tests, produce software packages, …
- Alternative to other build tools (e.g., Jenkins)
- Charged per minute for compute resources (time it takes to complete the builds)
- Leverages Docker under the hood for reproducible builds
- Use prepackaged Docker images or create your own custom Docker image
- Security:
- Integration with KMS for encryption of build artifacts
- IAM for CodeBuild permissions, and VPC for network security
- AWS CloudTrail for API calls logging

1. add `AmazonEKSClusterPolicy`, `AmazonElasticContainerRegistryPublicFullAccess` to the code build service role

2. add the buildspec.yaml file to the repo 

3. Configure Environment variables: REPOSITORY_URI	, ACCESS_KEY, SECRET_ACCESS_KEY, EKS_CLUSTERNAME

4.  trigger the pipeline


### CodeDeploy

- Deployment service that automates application deployment
- Deploy new applications versions to EC2 Instances, On-premises servers, Lambda functions, ECS Services
- Automated Rollback capability in case of failed deployments, or trigger CloudWatchAlarm
- Gradual deployment control
- A file named appspec.yml defines how the deployment happens


**Activities**


1. CodePipleine for deploying an MSa application in EKS.











