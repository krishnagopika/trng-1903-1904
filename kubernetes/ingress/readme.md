**Steps**

```
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx


helm search repo ingress-nginx --versions

helm install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --version 4.10.1 --namespace ingress-controller


kubectl port-forward -n ingress-controller svc/ingress-nginx-controller 443
```


ingress runs in two poets 80 and 443

creates a fake certificate which is served for default https traffic on port 443

CN Kubernetes Ingress controller fake certificate


```
helm upgrade --install ingress-nginx ingress-nginx --repo https://kubernetes.github.io/ingress-nginx  --version 4.10.1 --namespace ingress-controller --set-string controller.service.annotations."service\.beta\.kubernetes\.io/aws-load-balancer-type"="nlb"
```

with NLB


Ingress Class

Secrets





**reference**: [https://github.com/marcel-dempers/docker-development-youtube-series/tree/master/kubernetes/ingress/controller/nginx](https://github.com/marcel-dempers/docker-development-youtube-series/tree/master/kubernetes/ingress/controller/nginx)

