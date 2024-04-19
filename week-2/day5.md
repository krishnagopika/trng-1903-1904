


- info can be passed to kubectl in a mainifest file.
- yaml file or json file
- kubectl will convert this yaml file info to json or other supported format.


**apiVersion:** the version of the kubernetes API that is being used to crerate the object.

**kind:** what kind of object you are creating.


**labels**: labels are used select a set of objects

ex: type: dev


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


