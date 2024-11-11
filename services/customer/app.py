from flask import Flask, request, jsonify
from models import create_customer, get_customer, update_customer, delete_customer

app = Flask(__name__)

# Create customer (CREATE)
@app.route('/customer', methods=['POST'])
def create_customer_endpoint():
    data = request.json
    result = create_customer(data['name'], data['email'])
    return jsonify(result), 201 if "message" in result else 500

# Get customer (READ)
@app.route('/customer/<int:id>', methods=['GET'])
def get_customer_endpoint(id):
    result = get_customer(id)
    return jsonify(result), 200 if "id" in result else 404

# Update customer (UPDATE)
@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer_endpoint(id):
    data = request.json
    result = update_customer(id, data['name'], data['email'])
    return jsonify(result), 200 if "message" in result else 404

# Delete customer (DELETE)
@app.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer_endpoint(id):
    result = delete_customer(id)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
