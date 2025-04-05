from flask import Flask, request, jsonify
import redis
import requests

app = Flask(__name__)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

hgnc_data = "https://storage.googleapis.com/public-download-files/hgnc/json/json/hgnc_complete_set.json"


@app.route('/data', methods = ['POST', 'GET', 'DELETE'])
def data():
    if request.method == 'POST': 
        try: 
            response = requests.get(hgnc_data)
            response.raise_for_status()
            data_in_hgnc = response.json()
            for gene in data_in_hgnc: 
                id_hgnc = gene.get("hgnc_id")
                if id_hgnc:
                    redis_client.hset(id_hgnc, mapping = gene)
            return jsonify({"message": "HGNC data loaded into Redis"}), 201

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to fetch HGNC data: {e}"}), 500

    elif request.method == 'GET': 
        try:
            all_keys = redis_client.keys()
            all_data = [redis_client.hgetall(key) for key in all_keys]
            return jsonify(all_data), 200

        except requests.exceptions.RequestException as e:
            return jsonify({"error": f"Failed to retreive data from Redis {e}"}), 500

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
        return jsonify({"error": f"Gene list is unable to print out str{e}"}), 500


@app.route('/genes/<hgnc_id>', methods=['GET'])
def gene_details(hgnc_id):
    try:
        gene_data = redis_client.hgetall(hgnc_id)
        if gene_data:
            return jsonify(gene_data), 200
        else: 
            return jsonify({"error": f"No data found for HGNC ID {hgnc_id}"}), 404
    except redis.exceptions.RedisError as e:                                                                  return jsonify({"error": f"Not able to get the gene data str{e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

