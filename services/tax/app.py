from flask import Flask, request, jsonify
from models import create_tax, get_tax, update_tax, delete_tax

app = Flask(__name__)

# CREATE Tax Record
@app.route('/tax', methods=['POST'])
def create_tax_endpoint():
    data = request.json
    result = create_tax(data['tax_year'], data['state_tax'], data['county_tax'], data['city_rate'], data['tax_rate'])
    return jsonify(result), 201 if "message" in result else 500

# READ Tax Record
@app.route('/tax/<int:TTID>', methods=['GET'])
def get_tax_endpoint(TTID):
    result = get_tax(TTID)
    return jsonify(result), 200 if "TTID" in result else 404

# UPDATE Tax Record
@app.route('/tax/<int:TTID>', methods=['PUT'])
def update_tax_endpoint(TTID):
    data = request.json
    result = update_tax(TTID, data['tax_year'], data['state_tax'], data['county_tax'], data['city_rate'], data['tax_rate'])
    return jsonify(result), 200 if "message" in result else 404

# DELETE Tax Record
@app.route('/tax/<int:TTID>', methods=['DELETE'])
def delete_tax_endpoint(TTID):
    result = delete_tax(TTID)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
