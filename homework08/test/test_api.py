import pytest
from api import app
import redis
import json

@pytest.fixture()
def client(): 
    app.config['TESTING'] = True
    with app.test_client() as client: 
        yield client


def test_data_endpoints(client):
    response = client.post('/data')
    assert response.status_code in [201, 500]

    response = client.get('/data')
    assert response.status_code == 200

    response = client.delete('/data')
    assert response.status_code == 200

def test_genes_endpoints(client):
    response = client.get('/genes')
    assert response.status_code == 200

    response = client.get('/genes/HGNC:5')
    assert response.status_code in [200, 404]

def test_jobs_endpoints(client):
    response = client.post('/jobs', json={
        'gene_group': 'test',
        'symbol_prefix': 'T'
    })
    assert response.status_code == 201

    response = client.get('/jobs')
    assert response.status_code == 200

    response = client.get('/jobs/invalid_id')
    assert response.status_code == 404



