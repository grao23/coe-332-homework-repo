import pytest 
from worker import execute_job
from jobs import add_job, redis_db
import time

def test_worker_job_processing():
    params = {'gene_group': 'test', 'symbol_prefix': 'T'}
    job_id = add_job(params)

    execute_job(job_id)

    job = redis_db.hgetall(f'job:{job_id}')
    assert job['status'] == 'complete'



