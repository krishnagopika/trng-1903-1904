# SRE

### SRE Intro


- SRE is pioneered by google. it is focused on ensuring the reliability, availability and performance of large scale applications and services.

- Site Reliability Engineering is the practice of using tools to automate the tasks like system management and application monitoring.

- SRE describes the stability & quality of service offered by an application.




#### Service level Indicator

- its a quantitative measure of some aspect of service.

1. request latency
2. error rate
3. system throughput
4. availability

ex:

**user facing:** availability, latency and throughput

**storage systems:** latency, availability and durability

**big data systems:** throughput and end-to-end latency


#### Service level objective

- target or range for the SLI

ex:

1. throughput: queries per sec QPS
2. request latency in millisecinds


#### Service level Agreement


- explicit or implicit contacts that define the consequences of meeting or missing the SLO's.
- concequence can be financial(rebate or penality)
- SRE's dont define SLA's. They make sure that SLO's are met. They help with defining SLI's.


#### Error budget & maintainance window

- ammount of error a service can accumilate over a certain period of time before its noticible and causes issues.

- maintainace window is a period of time designated for prevative maintance for a service( this can cause disruption)

ex: os updates and software upgrades etc.



- never pick a target based on the current perfromace.
- Keep them simple
- few SLO's
- perfection can wait


**reference:**

[Google SRE](https://sre.google/sre-book/table-of-contents/)