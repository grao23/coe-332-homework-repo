from flask import Flask, request, jsonify
import redis
import requests
import json

app = Flask(__name__)
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)
hgnc_data = "https://storage.googleapis.com/public-download-files/hgnc/json/json/hgnc_complete_set.json"

@app.route('/data', methods=['POST', 'GET', 'DELETE'])
def data():
    if request.method == 'POST':
        try:
            response = requests.get(hgnc_data)
            response.raise_for_status()
            data_in_hgnc = response.json()
            
            # Process and store each gene document
            for gene in data_in_hgnc["response"]["docs"]:
                id_hgnc = gene.get("hgnc_id")
                if id_hgnc:
                    # Serialize complex fields to JSON strings
                    serialized_gene = {
                        key: json.dumps(value) if isinstance(value, (list, dict)) else value
                        for key, value in gene.items()
                    }
                    redis_client.hset(id_hgnc, mapping=serialized_gene)
            
            return jsonify({"message": "HGNC data loaded into Redis"}), 201

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to fetch HGNC data: {e}"}), 500

    elif request.method == 'GET':
        try:
            all_keys = redis_client.keys()
            all_data = []
            for key in all_keys:
                gene_data = redis_client.hgetall(key)
                # Deserialize JSON strings back to original types
                deserialized_gene = {
                    k: json.loads(v) if v.startswith('[') or v.startswith('{') else v
                    for k, v in gene_data.items()
                }
                all_data.append(deserialized_gene)
            return jsonify(all_data), 200

        except redis.exceptions.RedisError as e:
            return jsonify({"error": f"Failed to retrieve data from Redis: {e}"}), 500

    elif request.method == 'DELETE':
        try:
            redis_client.flushdb()
            return jsonify({"message": "All HGNC data deleted from Redis"}), 200
        except redis.exceptions.RedisError as e:
            return jsonify({"error": f"Failed to delete data from Redis: {e}"}), 500

@app.route('/genes', methods=['GET'])
def genes():
    try:
        all_keys = redis_client.keys()
        return jsonify(all_keys), 200
    except redis.exceptions.RedisError as e:
        return jsonify({"error": f"Gene list is unable to print out: {e}"}), 500

@app.route('/genes/<hgnc_id>', methods=['GET'])
def gene_details(hgnc_id):
    try:
        gene_data = redis_client.hgetall(hgnc_id)
        if gene_data:
            # Deserialize JSON strings in the response
            deserialized_data = {
                k: json.loads(v) if v.startswith('[') or v.startswith('{') else v
                for k, v in gene_data.items()
            }
            return jsonify(deserialized_data), 200
        return jsonify({"error": f"No data found for HGNC ID {hgnc_id}"}), 404
    except redis.exceptions.RedisError as e:
        return jsonify({"error": f"Not able to get the gene data: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

