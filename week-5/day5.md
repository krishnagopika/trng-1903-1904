# Lecture Plan

1. SQS 
2. SNS

### SQS


#### Messaging


Producers send messages to Queue and the Consumers poll the messages.

**SQS - Simple Queue Service**


- Oldest offering
- Fully managed service used to decouple the applications
- unlimited throughput, unlimited no of messages in the queue
- Retention: Max - 14days, Default - 4 days
- less than 10 ms latency
- message - 256kb limit
- can contain duplicates


**Producers**

- SDK SendMessage API
- message is persisted until a consumer deletes it

**Consumers**

- applications running in AWS or non AWS respurces
- poll/recievs the messages from the Queue
- DeleteMessage API to delete messages after polling


**Security**

- Encryption inflight using HTTPS API
- At rest encryption using KMS
- cliend side encryption
- IAM access contol for SQS API
- SQS Access Policies

#### Queue Access Policy

- Policy for Producer and Consumer
- Basic & Advanced(Custom Policy)

ex: Cross account access and publishing s3 event notifications to sqs queue


#### Message visibility timeout

- When a message is polled by a consumer it becomes ivisible for other comsumers for certail duration
- default: 30 sec
- ChangeMessageVisibility API is used to increase the visibility timeout.


#### Dead Letter Queues

- If consumer fails to process a message within the visibility timeout the message goes back to the queue.
- a `MaximumRecieves` threshold can be set for how many times the message can be sent back to the queue.
- If the threshold is met the message is sent to DLQ.
- The messages are processed in DLQ before they expire
- default expiration time is 14 days.
- The message can redrived to source once the issue is fixed.

#### Delay Queues

- Delay the message for certain period of time.
- max 15 min
- default at queue level can be overriden when message is sent using the `DelaySeconds` parameter.


#### FIFO Queues

- First in First out
- throughput is limited: 300msg/s and batching- 3000msg/s
- exactly-once - no duplicates
- deduplication time can be set 

```
.fifo
```

### SNS

- Pub/Sub Model
- event producer sends message to the SNS topic -> event listerns listen to the SNS topic
- upto 12,500,000 sub per topic
- 100,000 topics
- SNS Access policies
- SNS Can have a message filtering policy to filter the messages
- supports FIFO

**Security**

- Encryption inflight using HTTPS API
- At rest encryption using KMS
- cliend side encryption
- IAM access contol for SNS API


#### SNS & SQS Fanout Pattern

- push to SNS and all SQS queues are subscribed to SNS topic.
- decoupled and no data loss
- Cross region delivery


[SQS pricing](https://aws.amazon.com/sqs/pricing/)
[SNS Pricing](https://aws.amazon.com/sns/pricing/)