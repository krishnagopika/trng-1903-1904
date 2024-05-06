# Lecture Plan

1. Cloud Computing
2. IAM


### Cloud Computing

- IaaS
- PaaS 
- SaaS 


![IaaS, PaaS, SaaS](./images/iaas-paas-saas.png)


**Public Cloud**
- Cloud resources and services are hosted and managed by a third-party cloud provider (ex: Amazon Web Services (AWS), Microsoft Azure, Google Cloud Platform).
- Users access these resources over the internet on a pay-as-you-go or subscription basis.

**Private Cloud**
- A cloud computing environment hosted and managed within an organization's own data center.
- Provides more control and privacy but requires more resources and maintenance.

### AWS

**Budget Alerts**
- AWS provides budgeting tools to monitor and control costs.
- you can set custom budgets and receive alerts when your actual or forecasted costs exceed the budgeted amount.

#### IAM (Identity and Access Management)

**Users**
- an IAM user is an individual identity with specific permissions to access and manage AWS resources.
- each user has unique security credentials (access key ID and secret access key).

**User Groups**
- a collection of IAM users.
- permissions can be assigned to groups instead of individual users for easier management.

**Roles**
- an IAM role is an identity with specific permissions that can be assumed by AWS services.
- roles are used to grant temporary, limited privileges instead of creating and managing long-term credentials.