# Grafana

**Observability:** visualising the internal state of a system or application for tranparency.

- typically used or MSA, containers and clusters

Grafana:

- opensource software for observability. enabels o query, visulaze, alert and explore logs.


# Loki 


- Loki is the main server that stores logs and processes queries.
- Promtail is the agent that gathers logs and sends them to Loki.
- Grafana is used to query and display the logs.
- loki instance in kubernetes clutser or external
- to get kubelet logs promtail is required to get logs from all the pods and send it to loki instance
- to deploy promtain in every node.


steps to configure grafana:


1. navigate to grafana-dashboardDatasource.yaml

```yaml
"url": "http://prometheus-operated.monitoring.svc:9090",
```

2. delete the grafana pod deployed in monitoring namespace

```
kubectl get pods -n monitoring

kubectl delete pod <grafana-pod> -n monitoring
```

3. port forward to the grafana service

```
kubectl port-forward svc/grafana -n monitoring
```

4. test the prometheus datasource

5. daahboards --> datasource (prometehus) --> adding the metrics


[loki-promtail official docs](https://grafana.com/docs/loki/latest/get-started/)


