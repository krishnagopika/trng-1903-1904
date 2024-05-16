# Lecture plan

1. Serverless Introduction
2. Lambda functions
3. Cognito


---


# AWS Lambda

## Severless

- serverless is a new paradigm in which developers do not manage servers.
- code is deployed and functions are deployed
- Initially serverless == FaaS (Function as a service)
- Serverless was pionered by AWS lambda but now it also includes:
   - AWS Lambda
   - DynamoDB
   - AWS Cognito
   - API gateway
   - S3
   - SNS & SQS
   - Kenisis Data Firehose
   - Aurora Serverless
   - Step Functions
   - Fargate
- Severless doesnt mean there are no servers. It mean you just donot mange/provision/see the servers.

## Lambda

Comparision on EC2 vs Lambda:

**EC2** :

- Virtual servers in the cloud
- Limited by RAM and CPU
- Continiously running
- Scaling means intervention to add/remove servers.

**Lambda** :

- Virtual functions - no servers to manage
- Limited by time - short executions
- Run on-demend
- scaling is automated

**Benifits of Lambda:**

- Easy Pricing:
  - pay per requesr and compute
  - free tier 1M AWS lambda requests. `$0.20` per 1 million requests after exeeding the free tier(`$0.0000002` per request).
  - 400K GBs of compute time is free ie(400000 s if function is 1 GB RAM). $1.00 for 600,000 GB seconds.
- Integrated with the AWS suite of services(API gateway, Kenesis, DynamoDB, S3, CloudFront, CloudWatch Events EventBridge CloudWatch Logs, SNS, SQS, Cognito).
- Integrated with many programming languages:
   - Node.js
   - Python
   - java (Java8 compatible)
   - C#
   - GoLang
   - Ruby
   - Custom Runtime API (community supported, example rust)
   - Lambda Container image (must implement the lambda runtime API )
       - ECS/Fargate is preferred for running arbitary Docker images 
- Monitoring throug AWS CloudWatch.
- more resources per function(uo to 10GB of RAM)
- increasing RAM will also improve CPU and network 


### Synchronous Invocations 

Synchronous: CLI, SDK, API Gateway, ALB, ELB, Cloud Front, S3 batch, Cognito, step functions etc.(results are returned and errors are handled from client side)  ex: Client --> API Gateway --> Lambda.

AWS CLI Invocation:

```


# LINUX / MAC
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload '{"key1": "value1", "key2": "value2", "key3": "value3" }' --region us-east-1 response.json
```
```
# WINDOWS POWERSHELL
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload '{\"key1\": \"value1\", \"key2\": \"value2\", \"key3\": \"value3\" }' --region us-east-1 response.json
```
```
# WINDOWS CMD
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload "{""key1"":""value1"",""key2"":""value2"",""key3"":""value3""}" --region us-east-1 response.json
```

### Asynchronous Invocations

- S3, SNS, Cloudwatch events
- the events are placed in an Event Queue
- lambda attempts to retry on errors
  - 3 tries total
  - 1 min wait after 1st, then 2 min wait
- In case of retries make sure that the processing is idempotenet
- If the function is retries, the duplicate log entries are added to cloud watch logs
- Can define a DLQ (dead letter queue) - SNS or SQS - for failed processing (need correct permissions)
- Asynchronous invocations will speed up the processing. (if there is no waiting time for result)
- Services:
   - S3
   - SNS
   - CloudWatch Events/ EventBridge
   - CodeCommit
   - CodePipeline
   - CloudWatch Logs
   - SES
   - Cloud Formation
   - AWS config
   - AWS IOT and IOT events



```
# LINUX / MAC
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload '{"key1": "value1", "key2": "value2", "key3": "value3" }' --invocation-type Event --region us-east-1 response.json
```


```
# WINDOWS POWERSHELL
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload '{\"key1\": \"value1\", \"key2\": \"value2\", \"key3\": \"value3\" }' --invocation-type Event --region us-east-1 response.json

```


```
# WINDOWS CMD
aws lambda invoke --function-name demo-lambda --cli-binary-format raw-in-base64-out --payload "{""key1"":""value1"",""key2"":""value2"",""key3"":""value3""}" --invocation-type Event --region us-east-1 response.json

```
  
## Lambda Execution Enviorment

- Lambda invokes your function in an execution environment, which provides a secure and isolated runtime environment. 
- The execution environment manages the resources required to run your function.
-  The execution environment also provides lifecycle support for the function's runtime and any external extensions associated with your function.
-  The function's runtime communicates with Lambda using the Runtime API. Extensions communicate with Lambda using the Extensions API. Extensions can also receive log messages and other telemetry from the function by using the Telemetry API.

![Execution Enviorment](./images/lambda-execution-enviorment.PNG)

**Runtime API:** an HTTP API for custom runtimes to receive invocation events from Lambda and send response data back within the Lambda execution environment.

**Extentions API:** Lambda function authors use extensions to integrate Lambda with their preferred tools for monitoring, observability, security, and governance.c

**Telemetry API**: Using the Lambda Telemetry API, your extensions can directly receive telemetry data from Lambda. During function initialization and invocation, Lambda automatically captures telemetry, such as logs, platform metrics, and platform traces.


# Function Handler (Python Handler)

- Function handler is a method in the lambda function code that processes the evnets. When the lambda function is invoded, Lambda runs the handler method. Handler method returs a response, which can be used to handle another event.

Naming:

- The name of the file in which the handler function is created.
- The name of the Python handler function

A function handler can be any name; however, the default name in the Lambda console is lambda_function.lambda_handler.

# Event and Context Objects

**Event:** Event is the data passed to the lambda function upon execution. It contains data about where its emiitied from, and the other parameters that are passed in the event.

**Context:**  context is a Python objects that implements methods and has attributes. It's main role is to provide information about the current execution environment. Unlike event, the methods and properties of the context object remain the same regardless of the lambda was invoked or triggered.


## Cloud Watch

- AWS CloudWatch is a monitoring and mangement service that collects and visualize the execution logs, metrics, and event data in automaed dashboards.


## Lambda Layers


- a .zip file archive that contains supplementary code or data. 
- layers contain library dependencies, configuration files.
-  used to reduce the size of your deployment packages, separate core function logic from dependencies. update function dependencies independent of the function code.
-  to share dependencies across multiple functions layers can be used.

### thumbnail code


1. Install python

```
sudo yum install -y python3.9-pip
```

2. create a venv

```
python3.9 -m venv .venv
```

3. activate the venv

```
source .venv/bin/activate
```

4. install the dependencies

```
pip install boto3 pillow
```

5. zip the contentes of venv

```
mkdir python
cp ./venv/lib/ python
```

path

```
python/lib/python3.11/site-packages
```

6. create the zip file

```
zip -r dependencies.zip python
```

7. assign a role to ec2 with s3 `PutObject` access for the bucket


8. copy the zip file to s3

```
aws s3 cp dependencies.zip bucket-url
```

9. create a layer with python 3.9 and add the dependencies.zip object as source.

10. create two buckets. one for source images and other for compresed img.


11. create a lambda function with the the below policy attached to the lambda role

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:CreateLogGroup",
                "logs:CreateLogStream"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::source-s3-bucket/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::dest-s3-bucket/*"
        }
    ]
}
```

12. add the layer to the lambda function

13. lambda function code

``` python
import boto3
import os
import sys
import uuid
from urllib.parse import unquote_plus
import PIL.Image

s3_client = boto3.client('s3')

def resize_image(image_path, resized_path):
    print(image_path)
    with PIL.Image.open(image_path) as image:
        image.thumbnail(tuple(x // 2 for x in image.size))
        image.save(resized_path)

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        tmpkey = key.replace('/', '')
        download_path = f"/tmp/{uuid.uuid4()}{tmpkey}"
        upload_path = f"/tmp/resized-{tmpkey}"

        s3_client.download_file(bucket, key, download_path)
        resize_image(download_path, upload_path)
        bucket_target="dest-s3-bucket"
        s3_client.upload_file(upload_path, f"{bucket_target}", f"resized-{key}")
```

14. add a trigger in s3 bucket and configire it to the lambda function.
15. upload the image objects in source bucket. the compressed images will be stored in destination bucket.
# Lambda@Edge

- customization at edge
- Lambda@Edge is a feature of Amazon CloudFront that lets you run code closer to users of your application, which improves performance and reduces latency. With Lambda@Edge, you don't have to provision or manage infrastructure in multiple locations around the world. You pay only for the compute time you consume - there is no charge when your code is not running.
- CloudFront : Amazon CloudFront is a content delivery network (CDN) service built for high performance, security, and developer convenience.


## SDK (Software development Kit)

- AWS SDK is used to perform actions n AWS directly from application code (without using CLI).
- Python SDK is boto 3, AWS CLI is written in boto 3.
- If a region is not specified or configured "us-east-1" is choosen by default.

**[SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html#what-is-sam-overview)**

**Activities**

1. rock-paper-scissors lambda function in python.
2. img compression for images in s3 - event trigger to lambda.
