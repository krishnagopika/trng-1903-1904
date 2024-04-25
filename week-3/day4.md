
**Monitoring:** it is collecting the data from the applications or servers regularly. Monitoring is used to track  the health of your application or the server.



ex: 

1. resource usage: CPU, Memory and Disk Space
2. application: request rate, error rate and request latency


Methods:

1. **push:** application should send the metrics to  a particaulr endpoint.
ex: Graphite

2. **scrape:** the monitoring service will pull the metrics from an endpoint.
ex: prometheus


# Prometheus

- open source monitoring system with an alerting toolkit. It scrapes the metrics from the applications or server. highly reliable, standalone and easy to setup.


### Metrics


1. counter
2. gauge
3. histogram
4. summary



how does prometheus get the data from application?


1. metrics endpoints 


![prometheus architecture](./images/prometheus-architecture.png)



sample: timestap + value (flaot)

time series: list of sampels

TSDB: its stores the time series values



**Prometehus Server**

1. retreiver: retreives the metrics
2. TSDB: stores time series values
3. HTTP Server: to retreive the metrics using PromlQL or any observavility tool (ex: grafana)


- an application  is called an instance and a set of similar applications are considered as jobs.
- metrics are scraped from the instances.
- for short lived jobs, a push gateway is used.
- alert manager to trigger the allerts and send notifications to any communication channels like pager duty, email etc.


**Creating a metrics endpoint:**

1. install prometheus_client

```
pip install prometheus_client
```


**Setting up the prometheus Server**







