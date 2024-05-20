# Lecture Plan


1. DynamoDB
2. CloudWatch
---

# Dynamo DB

**[SQL vs NoSQL](https://www.mongodb.com/ko-kr/resources/basics/databases/nosql-explained/nosql-vs-sql)**

- DynamoDb is fully managed NoSQL database service from AWS.

#### Tabels, items and attributes, Indexes

- a table is a collection of data.
- each table contains zero or more items. An item is a group of attributes that is uniquely identifiable among all of the other items.
- each item is composed of one or more attributes. An attribute is a fundamental data element, something that does not need to be broken down any further.
- table must have a primary key
- each item must have a partition key and optionally sort key
- settings on a per table basis

each item has two keys
- partition key - hash key
- sort key - range key


**Primary Key**

- simple primary key: partition key
- composite primary key: partition key + sort key

**Secondary Indexes**

- a secondary index lets you query the data in the table using an alternate key, in addition to queries against the primary key.
- a table can have one or more secondary keys

**DynamoDB supports two kinds of indexes**

1. **Global secondary index** –  index with a partition key and sort key that can be different from those on the table.

2. **Local secondary index** – index that has the same partition key as the table, but a different sort key.

- Query and Scan are used to retive the data from dynamodb
- Scan is scanning through the whole table looking for elements matching criteria, query is performing a direct lookup to a selected partition based on primary or secondary partition/hash key.

[DynamoBD data types](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html)




### Monitoring in AWS

1. AWS CloudWatch

- Metrics
- Logs
- Events
- Alarms

2. AWS X-Ray

- Application performance troubleshooting
- distributed tracing of microservices


3. AWS CloudTrail

- Internal monitoring and auditing using trails.


# CloudWatch

### Metrics

- metric is a variable like CPU utilization, requests per minute, error rate etc
- metric is associated with dimesions. dimenstion is an attribute for metric like id, environment etc.
- upto 30 dim per metric
- metric have timestamps


**Example**

EC2

- metrics for every 5 min
- detailed monitoring - per min
- AWS free tier allows 10 deatiled monitoring metrics

Note: Memory usage is not a default metric. a custom metric should be created for memeory and details must be pushed from the instance.


- agent
- logs and unified
- CPU (active, gest idle)
- Disk
- RAM
- Netstat
- Processes
- Swap Space


#### Custom Metrics

- to define and send your own custom metrics to CloudWatch

**Example**: memory (RAM) usage, disk space, number of logged in users.
- Use API call PutMetricData
- Ability to use dimensions (attributes) to segment metrics
  - Instance.id
  - Environment.name
- Metric resolution (StorageResolution API parameter – two possible value):
    - Standard: 1 minute (60 seconds)
    - High Resolution: 1/5/10/30 second(s) – Higher cost


```bash
aws cloudwatch put-metrics-data --metric-name Buffers --namespace Demo --unit Bytes --value 7463947324 --dimensions InstanceID=i-487aksdh80,InstanceType=t2.micro
```


#### Cloud Watch Logs

- Log groups: arbitrary name, usually representing an application
- Log stream: instances within application / log files / containers
- Can define log expiration policies (never expire, 1 day to 10 years)
- CloudWatch Logs can send logs to:
  - Amazon S3 (exports)
  - Kinesis Data Streams
  - Kinesis Data Firehose
  - AWS Lambda 
  - OpenSearch
  - Logs are encrypted by default
  - Can setup KMS-based encryption with your own keys

**sources**: SDK, CloudWatch Agents, EB, ECS, Lambda, VPC, API Gateway, and CloudTrail


#### Cloud Watch Agents

For virtual servers (EC2 instances, on-premise server)
1. CloudWatch Logs Agent
    - Old version of the agent
    - Can only send to CloudWatch Logs
2. CloudWatch Unified Agent
    - Collect additional system-level metrics such as RAM, processes, etc…
    - Collect logs to send to CloudWatch Logs
    - Centralized configuration using SSM Parameter Store

**CloudWatch Unified Agent – Metrics**

- Collected directly on your Linux server / EC2 instance
- CPU (active, guest, idle, system, user, steal)
- Disk metrics (free, used, total), Disk IO (writes, reads, bytes, iops)
- RAM (free, inactive, used, total, cached)
- Netstat (number of TCP and UDP connections, net packets, bytes)  -  Processes (total, dead, bloqued, idle, running, sleep)
- Swap Space (free, used %)


**Cloud Watch Alarms**

- alarms are used to trigger notifications for any metric
- various options (sampling, %, max, min, etc…)
- alarm States:OK, INSUFFICIENT_DATA, ALARM
- Period:
  - Length of time in seconds to evaluate the metric
  - High resolution custom metrics: 10 sec, 30 sec or multiples of 60 sec


**Cloud Watch Synthetics**

- configurable script that monitor your apis, urls.
- Reproduce what your customers do programmatically to find issues before customers
are impacted
- Checks the availability and latency of your endpoints and can store load time data and screenshots of the UI
- Integration with CloudWatch Alarms
- Scripts written in Node.js or Python
- Can run once or on a regular schedule


**Activities**

1. Creating DynamoDB table and CRUD using boto3
2. EventBridge Scheduler trigger to a lambda Function
3. Cloud watch Alarm for EC2 CPU utilization to SNS configured to an Email Service




