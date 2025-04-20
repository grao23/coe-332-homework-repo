import pytest
import jobs from add_job, get_job, get_all_jobs
import redis
import json


@pytest.fixture(autouse=True)
def flush_redis():
    redis_db = redis.StrictRedis(host='redis', port=6379, db=0)
    redis_db.flushdb()

def test_add_job():
    params = {'gene_group': 'test', 'symbol_prefix': 'T'}
    job_id = add_job(params)
    assert isinstance(job_id, str)
    assert len(job_id) == 36

def test_get_job():
    params = {'gene_group': 'test', 'symbol_prefix': 'T'}
    job_id = add_job(params)
    job = get_job(job_id)
    assert job['status'] == 'submitted'
    assert json.loads(job['params']) == params

def test_get_all_jobs():
    params = {'gene_group': 'test', 'symbol_prefix': 'T'}
    add_job(params)
    jobs = get_all_jobs()
    assert len(jobs) == 1
