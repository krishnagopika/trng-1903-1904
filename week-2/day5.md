

### Declerative approach


- info can be passed to kubectl in a mainifest file.
- yaml file or json file
- kubectl will convert this yaml file info to json or other supported format.


**apiVersion:** the version of the kubernetes API that is being used to crerate the object.

**kind:** what kind of object you are creating.


```
kubectl apply -f=file.yaml, file2.yaml
kubectl apply -f=file.yaml -f=file2.yaml
```


#### rollouts

create new rollout:

```
kubectl set image deployment/[name] container-name=new-images
```

status

```
kubectl rollout status deployment/[name]
```

undo the deployment

```
kubectl rollout undo deployment/[name] [--to-revision=n]
```

history

```
kubectl  rollout history deployment/[name] [--revision=n]
```

**labels:** labels are used select a set of objects


ex:

```
enviorment: dev
enviorment: test
enviorment: prod

service: user
service: job
service: application
service: auth
```

**label selectors** 

- not unique like names
- many objects have same labels
- using a label selector you can identify a set of objects.


**annoatations**

- metadata for object. not used for object selection

**names:** every object will have a name(unique in namespace) and UID (unique in cluster).

**namespaces:** 
- namespaces are used to provide isolated environment for multiple users in a single cluster.
- namespace will provide scope for object names.
- namespaces cant be nested.


**Initial Namespaces created for a cluster:**

1. **default**: default namespace where all the objects created without explicit namespace name are located.
2. **kube-public**: any resources in public  namespace is accessible throughout the cluster.
3. **kube-system**: The namespace for objects created by kubernetes systems.
4. **kubernetes-node-lease:** holds the lease objects of each node. lease allows to detect if the nodes are alive. 

list namespaces
```
kubectl get namespaces
```

list the objects
```
kubectl get <object> --namespace=name or -n dev
```

create objects
```
kubectl create <object> <name> -n <=namespace>
```

delete namespace

```
kubectl delete namespace <namespace>
```

#### Network policies


- control the traffic at the IP address kevel or port level.

- container to conatiner communications in a pod is done using `localhost`
- external communication is estblished using service
- pod-service communication is covered by services
- pod to pod communications are controlled using Networkpolicies 


**Ingress**: incomming requests
**Egress**: uoutgoing responses



