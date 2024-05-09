# Lecture Plan

1. EKS

---

### Elastic Kubernetes Service

### Cluster & Cluster Management

Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided by Amazon Web Services (AWS). It simplifies the deployment, management, and scaling of Kubernetes clusters.

To manage your EKS cluster, you can use the AWS Command Line Interface (CLI). Here's an example command to update the kubeconfig file for accessing the cluster named "revhire" in the us-east-1 region:

```
aws eks --region us-east-1 update-kubeconfig --name cluster-name
```

### Nodes

In an EKS cluster, nodes are the underlying EC2 instances responsible for running your containerized applications. These nodes can have different roles and permissions. For example:

- **Role**: Service-EC2
- **Permissions**: EC2 Worker node, CNI (Container Network Interface) for networking between containers and ECR (Elastic Container Registry) readonly access for pulling container images.

### Storage

EKS supports various storage options for your Kubernetes workloads, Amazon Elastic File System (EFS), and third-party storage solutions.

### Networking

Networking in EKS is managed through integration with AWS networking services like Amazon VPC (Virtual Private Cloud) and AWS Load Balancers. You can configure networking policies, ingress, and egress rules to control traffic flow within your cluster.

### Workloads

EKS allows you to deploy and manage containerized workloads using Kubernetes. You can run various types of applications, including microservices, batch processing jobs, and machine learning workloads, on your EKS cluster.

### Cluster Authentication

Authentication in EKS is handled through integration with AWS IAM (Identity and Access Management). You can grant users or services access to your EKS cluster by assigning IAM roles and permissions.

### Security & Observability

EKS provides built-in security features such as encryption at rest and in transit, IAM integration for access control, and network policies for fine-grained security controls. For observability, you can use tools like Amazon CloudWatch and AWS X-Ray to monitor and troubleshoot your EKS cluster and for monitoring EKS supports prometheus.


---

1. Create a cluster

- EKS--> Cluster
- Cluster role permissions: EKS Cluster Role
- VPC:  use cloudformation stack to create public or private or public-private VPC, subnets, IG and NAT gateway

s3 url for public private: `https://s3.us-west-2.amazonaws.com/amazon-eks/cloudformation/2020-10-29/amazon-eks-vpc-private-subnets.yaml`


[VPC CF template](https://docs.aws.amazon.com/eks/latest/userguide/creating-a-vpc.html)

2. Create a Node group

- Cluster --> Compute --> add node group
- WorkerNode role
  - **Role**: EC2
  - **Permissions**: EC2 Worker node, CNI (Container Network Interface) for networking between containers and ECR (Elastic Container Registry) readonly access for pulling container images.
- configure ASG (min, desired and max resources)
- Instance type: t2.micro


3. kubctl configuration

```
aws eks --region us-east-1 update-kubeconfig --name cluster-name
```

4. IAM User Access

- Cluster --> Access --> Create Access entry --> select the user --> Permission (ClusterAdmin)


5. Deploying the application

- cd to `revhire-eks`

```
kubectl apply -f job.yaml,user.yaml
```

```
kubectl get svs
```

use the lb dns to access the application.