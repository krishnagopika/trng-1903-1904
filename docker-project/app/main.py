from fastapi import FastAPI, HTTPException, Response, Header
# from fastapi.responses import PlainTextResponse

import logging
import os
import signal
import time
import prometheus_client
from prometheus_client.core import CollectorRegistry
from prometheus_client import Counter, Histogram, Gauge, Summary
logging.basicConfig(filename="user_controller.log", encoding='utf-8', filemode='a', level=logging.INFO)

logger=logging.getLogger(__name__)

app = FastAPI()


graphs = {}

graphs['users_counter'] = Counter('users_c', 'Counter for get_users_request_operations_total')
graphs['users_gauge'] = Gauge('users_g', 'Gauges for no of user requests')
graphs['users_error_counter'] = Counter('users_error', 'Counter for get_users_request_error_operations_total')
graphs['home_counter'] = Counter('home_c', 'Counter for home_request_operations_total')
graphs['get_job_counter'] = Counter('jobs_c', 'Counter for get_jobs_request_operations_total')
graphs['kill_counter'] = Counter('kill_c','Counter for kill_request_operations_total')
graphs['users_histogram'] = Histogram('users','get_users_duration_seconds', buckets={1,2,3,5,7,float('inf')})
graphs['users_summary'] = Summary('users_summary','get_users_duration_seconds')
graphs['jobs_histogram'] = Histogram('jobs_h','get_jobs_duration_seconds', buckets={1,2,3,5,7,float('inf')})
graphs['home_histogram'] = Histogram('home_h','home_duration_seconds', buckets={1,2,3,5,7,float('inf')})
graphs['kill_histogram'] = Histogram('kill_h','kill_duration_seconds', buckets={1,2,3,5,7,float('inf')})

@app.get("/users")
def get_users():
    try:
        start = time.time()

        return {"users" :[
            {"id": 1, "name": "Jane Smith", "email": "jane.doe@email.com", "password": "1234"},
        ]}
    
    except Exception as e:
        logger.error(e)
        print("Error")
        graphs['users_error_counter'].inc()
        raise HTTPException(500)
    finally:
        graphs['users_counter'].inc()
        graphs['users_gauge'].set(1)
        graphs['users_summary'].observe(time.time() - start)
        graphs['users_histogram'].observe(time.time() - start)

@app.get("/")
def get_home():
    try:
        start = time.time()
    
        return "welcome to revhire"
    
    finally:
        graphs['home_counter'].inc()
        graphs['home_histogram'].observe(time.time() - start)


@app.get("/jobs")
def get_jobs():

    try:
        start = time.time()
    
        return { "jobs": [
            {"id": 1, "name": "DevOps Eng"},
            {"id": 2, "name": "Gen AI Eng"},
        ]
        }
    except Exception as e:
        logger.error(e)
        print("Error")
        raise HTTPException(500)
    
    finally:
        graphs['get_job_counter'].inc()
        graphs['jobs_histogram'].observe(time.time() - start)




@app.get("/kill")

def shutdown():
    try:
        start = time.time()
        os.kill(os.getpid(), signal.SIGTERM)
    finally:
        graphs['kill_counter'].inc()
        graphs['kill_histogram'].observe(time.time() - start)


@app.get("/metrics")
def metrics():
    
    result = []
    header = {'Content-Type': 'text/plain'}
    for k,v in graphs.items():
        result.append(prometheus_client.generate_latest(v).decode('utf-8'))
    return Response(''.join(result), headers=header)