# Lecture Plan


1. Cognito
2. API-Gateway


---


# AWS Cognito


- Cognito is a User Identity provider service from AWS.


### User Pools


- used to create a user directory. 
- Can be integrated with web or mobile app or to a third party IDP.
- Supports email and sms using SES, cognito noreplyemail and SNS.
- Supports multiple app client(applications) intergartions.
- supports MFA, custom fields, custom user creation and verification.
- supports authentication tokens and provides a JWT token. 
- supports 3rd party IDP assertions.
- users can can be created, verified, grouped and managed by admin.


**Authentication flow**

- verification of a users identity using password and other configurations.
- Public Authentication
- Client side authentication
- Server side authntication


**[JWT](https://jwt.io/introduction)**


**Optional**

### Cognito Identity Pools (Federated Identities):

- used to get identities for "users" so they obtain temporary AWS creantials.
- your identity pool can include:
  - Public providers(Login with Amazon, Facebook, Google, Apple)
  - uders in an cognito user pool
  - OpenID Connect Providers & SAML Identity providers
  - Developer Authenticated Identities (custom login users) 
  - Cognito Identity Pools allow for unauthenticated (guest) access.
- users can access AWS services directly using the API_Gateway

**IAM Roles:**

- Default IAM roles for authenticated and guest users
- Define rules to choose the role for each iser based on theuser ID
- partition your users access using **policy variables**
- IAM credentials are obtained by Cognito Identity Pools through STS
- The roles must have a trust policy of cognito identity pool to work.



# AWS API Gateway

Amazon API Gateway is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.

## Benifits of AWS Api Gateway

API Gateway in AWS provides several benefits when it comes to API management and design. Here are some key benefits of using API Gateway, including JSON rewriting and REST API design:

1. Centralized API Management: API Gateway acts as a central entry point for all your APIs. It simplifies the management of your APIs by providing a single interface to handle authentication, authorization, rate limiting, caching, request/response transformations, and more.

2. Scalability and High Availability: API Gateway is designed to handle high traffic loads and automatically scales to accommodate increased demand. It ensures high availability and reliability by distributing traffic across multiple availability zones.

3. Security and Access Control: API Gateway allows you to secure your APIs by integrating with AWS Identity and Access Management (IAM) and other authentication providers. It supports various authentication mechanisms such as API keys, IAM roles, OAuth, and custom authorizers, ensuring that only authorized clients can access your APIs.

4. Request/Response Transformation: API Gateway enables you to transform the request and response payloads using JSON rewriting. This feature allows you to modify the structure of incoming or outgoing JSON payloads without changing the backend services. It helps in aggregating data from multiple services, mapping between different data models, or hiding sensitive data from responses.

5. Caching and Performance Optimization: API Gateway provides built-in caching capabilities that can significantly improve the performance of your APIs. You can configure caching settings at different levels, such as stage, method, or individual endpoints. Caching reduces the load on your backend services and improves response times for frequently accessed data.

6. API Versioning and Deployment Management: API Gateway supports versioning of APIs, allowing you to roll out changes and new features without disrupting existing clients. You can manage different versions of your APIs and control the deployment of updates through stage management.

7. Monitoring and Analytics: API Gateway integrates with AWS CloudWatch, allowing you to monitor the performance and health of your APIs in real-time. You can  set up custom metrics, alarms, and logs to track important API metrics, identify issues, and troubleshoot problems.

8. Developer Portal and Documentation: API Gateway provides a developer portal where you can publish documentation, SDKs, and interactive API documentation. It allows developers to explore and understand your APIs, test endpoints, and generate client code snippets.

9. Integration with AWS Services: API Gateway seamlessly integrates with other AWS services, such as AWS Lambda, AWS Step Functions, Amazon Cognito, Amazon S3, and more. This enables you to build serverless architectures, implement custom logic, and leverage existing AWS services within your APIs.


### API Gateway - Endpoint Types

1. Edge-Optimized (default): For global clients
   - Requests are routed through the CloudFront Edge locations (improves latency)
   - API Gateway still lives in only one region

2. Regional:
   - For clients within the same region
   - Could manually combine with CloudFront (more control over the caching
strategies and the distribution)


3. Private:
   - Can only be accessed from your VPC using an interface VPC endpoint (ENI)
   - Use a resource policy to define access



**optional**


### Json rewriting

JSON rewriting in API gateway refers to the process of modifying or transforming JSON payloads as they pass through the gateway. API gateways act as intermediaries between clients and backend services, allowing them to manage and control API traffic. JSON rewriting provides the ability to manipulate the structure or content of JSON data during this process.

Few common scenarios where JSON rewriting in API gateways is useful:

1. **Request/Response Transformation**: API gateways can rewrite JSON payloads in both request and response flows. This enables them to convert data between different formats, such as translating JSON to XML or vice versa, before forwarding the request to the backend service or returning the response to the client.

2. **Data Filtering**: API gateways can selectively filter out or include specific fields from JSON payloads. This is often done to reduce the amount of data transferred over the network, improving performance and minimizing bandwidth consumption.

3. **Data Mapping**: JSON rewriting allows for mapping fields from the client's request to the backend service's expected format. It enables modifying field names, reordering fields, or even splitting or merging fields to match the target data structure.

4. **Data Validation**: API gateways can enforce data validation rules by examining JSON payloads. They can reject or modify requests that don't adhere to predefined validation criteria, such as data types, field constraints, or mandatory fields.

5. **Security Enhancements**: JSON rewriting can be used to add security-related elements to JSON payloads. This includes injecting authentication or authorization tokens, encrypting or decrypting sensitive data, or adding digital signatures for integrity and authenticity.


Steps to integrate API gateway with lambda


1. Create a REST API gateway
2. Create a post method with resource as lambda
lambda code:

```python
import json

def lambda_handler(event, context):
    name = event['name']
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps(f'hey {name}!'.format(name))
    }

```

3. Create a model

```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title" : "Demo Schema",
  "type" : "object",
  "properties":{
      "name":{
          "type":"string"
      }
  },
  "required":["name"]
}
```
4. edit the method and configure the request body model.

5. Create Authorization. configure the cognito user pool with Authroization key. enable validation for request header. 

6. edit the method and configure the authorizer

7. Create a deployment with a new stage (dev, test, prod)
7. Login to cognito app client and pass the id_token while invoking the api gateway with deployment url.





