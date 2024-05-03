# Lecture Plan

1. ElastiCache
2. S3
3. CloudFront

---

### ElastiCache

- memcached and redis
- cluster (shards (Primary + replica nodes))
- serverless


![ElastiCache](./images/ElastiCache-Cluster-Redis.png)

**Stratergies**

- caching necessity, data for caching.

**Design Pattern**
- Lazy Loading/ Cache aside/ Lazy Polulation
- Write-through
- TTL

![lazy loading](./images/lazy-loading.png)

**Write through**

![write through](./images/writethrough.png)


requirements

ec2:


```bash

sudo yum install -y python3-pip

pip install sqlalchemy python-dotenv redis pymysql
```


[ElastiCache pricing](https://aws.amazon.com/elasticache/pricing/)


### S3 (Simple Storage Service)

- Amazon S3 is one of the main building blocks of AWS
- Its advertised as "Infinite scalling" storage
- Many websites use S3 as backbone and many services use s3 as an intergration.


**Use Cases**

- Backup and storage
- Disaster recovery
- Archive
- Hybrid Cloud storage
- Application hosting
- Media hosting
- Data lakes & big data analytics
- Software delivery
- Static website


Buckets (Directories, unique name(across all regions and all accounts))
  - objects(files)

- Buckets are defined at the region level (S3 looks like a global service but the buckets are region specific )
- Naming Convention
   - No uppercase, no underscore
   - 3-63 char long
   - lowercase letters, numbers, dots (.), and hyphens (-) are allowed.
   - Not an IP
   - Must start with lowecase letter or nummber
   - must not start with prefix xn--
   - must not end with suffic -s3alias

Objects:

- objects have a key
- key is the full path 
    ex: s3://my-bucket/*my_file.txt*
        s3://my-bucket/*my_folder/my_file.txt*
    - Key = prefix + object name
- There is no concepts of directories within buckets. Just keys with very long names.
- Objects values are content of the body
- Max Object size is 5TB (5000GB)
- if uploading more than 5GB multi-part upload is must
- Metadata (list of key/value pairs - system or user metadata)
- Tags (Unicode key/value pair) - usefull for security /lifecycle
- Version ID (if versioning is enabled) 


#### S3 Security

- User based: IAM policies- which API calls should be allowed for a specific user from IAM
- Resource Based: 
    -  Bucket Policies: bucket wide rules from S3 console - allows cross account
    -  Object Access Control List (ACL) - finer grain (can be disabled)
    -  Bucket Access Control List (ACL) - less common (can be disabled)  

- If IAM policies are allowed or resource policy is allowed and if there is no expilict deny an IAM Principle can access the bucket
- Encryption :encrypt objects in AWS S3 using encryption keys


#### S3 bukcet policies:

- Json based policies:
    - Resource: buckets and objects
    - Effect : allow or deny
    - Actions : get, put, and delete etc.
    - Principal: Aws account user, role and root user
- S3 bucket policy can be used to:
    - grant public access to the bucket
    - force objects to be encrypted at upload
    - grant cross access to another account 

- Bucket setting to block public access take priity over the bucket policies
- Used to avoid data leaks
- Can be set at te account level

## Static Web Hosting

- S3 can host static websites and have them accessible on the internet
- The website url will be based on the url (http://bucket-name.s3-website.aws-region.amazomaws.com or  http://bucket-name.s3-website-aws-region.amazomaws.com)

- enable the static webhosting in properties and add the index.html file

#### Versioning

- you can version your files in AWS S3
- It is enabled in bucket level
- same key overwrite will chnage the version: 1,2,3,4...
- The files can be protected against the unintended dletes and easy to roll back to previous version.

Note: Any file that is not versioned prior to enabling will have version null



### Cloud Front

- Content Delivey Network. Improves the read performance, content is cached at the edge locations(600+).

**Cloud Front Origin**

1. S3 Bucket

   - for distributing files and caching then at edge
   - Origin Access contriol
   - ingress to upload files to S3

2. Custom Origin (HTTP)

   - Application Load balancer
   - EC2 Instance
   - S3 website 

s3 website (S3 bucket with blocked public access)using cloud front

- disble the web security

#### Caching and Caching Policies


- the cache is  stored at CloudFront edge location.
- cache key is used to identify the cache object. 
- by default cache key = hostname+ resource portion of the url.
- 
**ex:** 
host name: revhire.com

GET request portion: /index.html

- the goal is to maximize the cache hit and reduce the requests to origin
- CacheInvalidation API is used to invalidate the part of the cache.



**Cache Policies**

- Cache Based on:

  - HTTP Headers
  - Cookies
  - Query Strings
- Control the TTL (0 sec to 1 year) by  the origin using Cache control header and expires header   
- custom and predefined policies can be use.

**Origin Request Policies**

- values to be included in origin request without including them in the cache key.
- values can be HTTP headers, cookies and query strings


ex:

cache policy

- hostname
- path
- header: authorization

origin policy:

- headers: User-Agent
- Cookies: session_id
- Query Strings: ref

#### Caching Invalidations & Behavior

**Invalidate**

- The cache will be refreshed when after the TTL has expired.
- A partial or full cache refresh can be performed using CloudFront Invalidation

**Behavior**

- configure settings like routing to different orgins based on the content type and path pattern


ex: /images/* , /api/*, /* (default cache behavior)

- custon cacge behaviors take precedence over the default cache behavior.

use case:  

1. access to S3 after signin by using signin cookies.
2. static content - no cache rules. dynamic content requires cache rules based on headers and cookie.



#### Geo Restriction


- Allow and block lists can be set up specific to countries.
- Based on user ip the Geo location of user is identified.
- Dist --> Security --> Geo Restrictions


#### Signed Url/Cookies

- Used to share content to specific users for a specific period of time.
- Signed URL includes:
   - URL Expiration
   - IP ranges to access the data from
   - Trusted signers (AWS accounts that can create signed URLs)
- Validity:
  - Shared content: short - few minutes  
  - Private content : long - last for years
- Signed URL : one per file
- Signed Cookies: one for multiple files.



![Signed URL](./images/cf-signed-url.png)


**Process:**

- trusted key group (recommended)
- aws account that contains cloud front key pair (root account + console for key management)

trusted key groups

- one or more trusted key groups
- public/private key. pub - cloud front. private key - application.


#### Real Time Logs


- store real-time requests recived by cloud front to kenisis data streams
- monitoring and analyzing
- sample rate (% of requests , specific fields and chache behavior)