# Logback

### Logback Introduction

- logback is fast logging system.
- it is a successor of log4j
- logback requires slf4j

### Root

- specifies the root logging level

    - TRACE
    - DEBUG
    - INFO
    - WARN
    - ERROR


### Apenders

- log events are written into appenders

1. console appender
2. file appender


### Encoders

- used to format log events


### MDC Implementation

- In a multi threaded application, additional context related to client could help with better categorization of logs. Mapped Diagnostic Contexts are used to add additonal info to log.

ex: user Id


**Reference**

[logback official docs](https://logback.qos.ch/manual/index.html)