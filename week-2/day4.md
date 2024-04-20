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
- Kube control manager: watches and controls worker nodes, manages the no of pods, jobs and ServiceAccounts for a namespace
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


```bash
minikube start --driver=docker

# or

minikube start --driver=hyperv

# or
minikube start --driver=virtualbox
```

for status:

```bash
minikube status
```

dashboard

```
minikube dashboard
```


**Kubernetes Objects**

1. pod: Kubernetes will start, stop and replece pods as needed. pods are ephemeral

<i><b>Note:</b></i> whenever a container crashes, the container state and all teh files that were created during the lifetime of container are lost. kubectl will restarct the container with a clean state.

2. deployment: used to manage the pods. Internally is a controler object

- set desired target state. which pods and containers whould run and also the no of instances
- can be paused, deleted and rolled back. 

3. volumes: volumes are used as data stores or pods.

- usefull when a shared filesystem is required.


to create a deployment:

```
kubectl create deployment [name] --image=image-name,image2,image3
```

list deployments

```
kubectl get deployments
```

list pods

```
kubectl get pods
```

delete deployment

```
kubectl delete deployments [name]
```

1. instructions are sent to control plane (master node)
2. scheduler analyzes pods that are currently running and finds the best node for new pods.
3. worker node: kubelet monitors the pods.
4. pods : one container with the image.


- cluster ip is internally  routed through the cluster network.
- service groups pods together and gves them a shared ip
- service allows you to access pods externally.
- without the service communication with pods is difficult internally and impossible to achieve externally.

creating a service:
```
kubectl expose deployment [deployment-name] --type=ClusterIp/NodePort/LoadBalancer
```

list the services

```
kubectl get services
```

```
minikube service [name]
```


to scale:

```
kubectl scale deployment/name --replicas=n
```












