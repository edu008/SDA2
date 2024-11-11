from flask import Flask, request, jsonify
from models import create_order, get_order, update_order, delete_order

app = Flask(__name__)

# CREATE Order
@app.route('/order', methods=['POST'])
def create_order_endpoint():
    data = request.json
    result = create_order(data['OTID'], data['stock_amount'], data['product_id'])
    return jsonify(result), 201 if "message" in result else 500

# READ Order
@app.route('/order/<int:OID>', methods=['GET'])
def get_order_endpoint(OID):
    result = get_order(OID)
    return jsonify(result), 200 if "OID" in result else 404

# UPDATE Order
@app.route('/order/<int:OID>', methods=['PUT'])
def update_order_endpoint(OID):
    data = request.json
    result = update_order(OID, data['OTID'], data['stock_amount'], data['product_id'])
    return jsonify(result), 200 if "message" in result else 404

# DELETE Order
@app.route('/order/<int:OID>', methods=['DELETE'])
def delete_order_endpoint(OID):
    result = delete_order(OID)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
