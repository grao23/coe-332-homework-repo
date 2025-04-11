import redis
import uuid
import json
import os
from hotqueue import HotQueue


redis_host = os.environ.get('REDIS_HOST', 'localhost')
redis_db = redis.StrictRedis(host=redis_host, port=6379, db=0, decode_responses=True)
q = HotQueue("job_queue", host=redis_host, port=6379, db=1)

def add_job(params):
    job_id = str(uuid.uuid4())
    job_data = {
        'id': job_id,
        'status': 'submitted',
        'params': json.dumps(params)
        }
    redis_db.hset(f'job:{job_id}', mapping=job_data)
    q.put(job_id)
    return job_id

def get_job(job_id):
     job = redis_db.hgetall(f'job:{job_id}')
     if job and 'params' in job:
         job['params'] = json.loads(job['params'])
         return job
    
def get_all_jobs():
    return [get_job(job_id) for job_id in redis_db.keys('job:*')]
