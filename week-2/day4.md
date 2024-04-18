# Lecture Plan

1. kubernetes



---

**Kubernetes or K8s**

- Manual deployment of containers is difficult to maintain and error prone.
- Kubernetes is an open source container orchestartion service.
- crash detection, autoscaling, load balancing are few features that are provided by kubernetes


**Architecture**


![kubernetes architecture](/week-2/images/kubernetes-cluster-architecture.svg)


**Pods(container):**

- smallest possible unit.
- conatins one or more containers that run applications.
- hosts one or more applications and their resources.
- created and managed by kubernetes


**Nodes:**

- physical or VM with certain hardware capacity. It hosts pods.

**1. Woker Mode:** 

- runs containers(pods)
- kubelet (monitors the pods)
- kube-proxy (incoming and outgoing traffic.)

**2. Master Node (Control plane):** contols and manages worker nodes.

- API Server: API for the kubelets to communicate
- Scheduler: watches pods for new pods. It selects worker nodes to run the pods.
- Kube control manager: watches and controls worker nodes, manages the no of pods.
- cloud control manager: KCM for a cloud provider like AWS EKS or Azure  AKS or GCP GKS or kubermatics.


**Cluster:** a set of nodes that run the containerized appplications(worker node) or control other nodes(master node).

1. kubectl : used to execute commands on  kubernetes cluster.

[kubernetes components](https://kubernetes.io/docs/concepts/overview/components/)
[kubernetes architecture](https://kubernetes.io/docs/concepts/architecture/)

**Steps for Intsallation:**

1. install chocolatey [windows ps](https://community.chocolatey.org/courses/installation/installingl)
2. install kubectl

```
choco install kubernetes-cli
```

3. minikube 

alternatives: microK8's and K3's

```
choco install  minikube
```


to start minikube


```
minikube start --driver=docker
```







