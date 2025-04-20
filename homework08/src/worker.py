"""
Worker process for HGNC Gene Analysis Web App
"""

import os
import json
import logging
from redis import Redis
from hotqueue import HotQueue
from collections import defaultdict
from typing import Dict, Any

LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
redis_db = Redis(host=REDIS_HOST, port=6379, db=0, decode_responses=True)
results_db = Redis(host=REDIS_HOST, port=6379, db=3, decode_responses=True)
q = HotQueue("job_queue", host=REDIS_HOST, port=6379, db=1)

def analyze_genes(gene_group: str, symbol_prefix: str) -> Dict[str, Any]:
    """
    Analyze HGNC genes by group and symbol prefix.
    Returns summary statistics.
    """
    keys = redis_db.keys()
    matches = []
    chromosome_dist = defaultdict(int)
    status_dist = defaultdict(int)
    locus_dist = defaultdict(int)

    for key in keys:
        gene = redis_db.hgetall(key)
        try:
            if (gene.get('gene_group', '').lower() == gene_group.lower() and
                gene.get('symbol', '').startswith(symbol_prefix.upper())):
                matches.append(gene)
                chromosome_dist[gene.get('location', 'unknown')] += 1
                status_dist[gene.get('status', 'unknown')] += 1
                locus_dist[gene.get('locus_type', 'unknown')] += 1
        except AttributeError as e:
            logger.warning(f"Error processing gene {key}: {str(e)}")
            continue

    return {
        'count': len(matches),
        'chromosome_distribution': dict(chromosome_dist),
        'status_distribution': dict(status_dist),
        'locus_type_distribution': dict(locus_dist),
        'status': 'complete'
    }

@q.worker
def execute_job(job_id: str):
    """
    Worker function to process a job from the queue.
    """
    logger.info(f"Starting job {job_id}")
    try:
        job = redis_db.hgetall(f'job:{job_id}')
        if not job:
            logger.error(f"Job {job_id} not found")
            return

        redis_db.hset(f'job:{job_id}', 'status', 'in progress')
        params = json.loads(job['params'])

        results = analyze_genes(params['gene_group'], params['symbol_prefix'])
        results_db.set(job_id, json.dumps(results))
        redis_db.hset(f'job:{job_id}', 'status', 'complete')
        logger.info(f"Completed job {job_id}")

    except Exception as e:
        logger.error(f"Job {job_id} failed: {str(e)}")
        redis_db.hset(f'job:{job_id}', 'status', 'failed')

if __name__ == '__main__':
    execute_job()


