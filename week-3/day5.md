### Alert manager


- Alert manager is used to handle the alerts sent by prometheus server. It routes the alerts to a correct reciever such as email and pagerduty etc


**Alerting stratergies**


**Grouping:** groups similar alerts into one single notification

ex: database is down for a MSA application

**Inhibition:** supressing notification for alerts if other alerts are already firing.

ex: An alert that the netire cluster is down is prioratized over other alerts.

**Silences:** mute alerts for a certial period of time. a matcher is used to filter the laerts and no notifications are sent if the condition is true for alert.


**Alerting rules**


- used to define the alert conditions based on a prometheus expresssions. 

ex: http requests per minute > 1000, cluster resource usage alerts like node memory usage goes beyond the threshold

**Alerting properties**

precession: accuracy of the positive predictions.

TP/(TP+FP)


recall: sensitivity

TP/(TP+FN)

detection time: time takes my the monitoring system to detect the issue. configuring optimal scrape intervals and alert evaluation interval will reduce the detection time.

reset time:

time taken to resolve the alert issue. automated actions and workflows in alert manager will reduce the reset time. 


**Recoding rules**

- recording rules are used to precompute the frequently needed or compex or computationally expensive expresssions and save their results.
ex: total http requests, cluster resouce utilization


---



Steps:

1. creating the rules: create prometheus_rules.yaml files. create a PrometheusRule obj.

```

kubectl apply -f prometheus_rules.yaml
```

2. add ruleSelector configuration to prometheus.yaml file

```yaml
ruleSelector:
    matchLabels:
      app: demo-app
```

```
kubectl apply -f prometheus.yaml
```

3. port forward to the prometheus

```
kubectl port-forward prometheus-applications-0 -n monitoring 9090
```


**prometheus operator**


**kube prometheus**