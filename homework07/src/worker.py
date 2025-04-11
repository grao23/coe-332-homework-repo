import time
import os
from jobs import q, redis_db

@q.worker
def execute_job(job_id):
    job = redis_db.hgetall(f'job:{job_id}')
    if job:
        redis_db.hset(f'job:{job_id}', 'status', 'in progress')
        time.sleep(10)  # Simulate work
        redis_db.hset(f'job:{job_id}', 'status', 'complete')

if __name__ == '__main__':
    execute_job()

