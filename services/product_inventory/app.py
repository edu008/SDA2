from flask import Flask, request, jsonify
from models import (
    create_product, get_product, update_product, delete_product,
    create_vendor, get_vendor, update_vendor, delete_vendor
)

app = Flask(__name__)

# CRUD operations for `product_inventory`
@app.route('/product', methods=['POST'])
def create_product_endpoint():
    data = request.json
    result = create_product(
        data['brand'], data['description'], data['productName'], data['productType'],
        data['productSubType'], data['unit_price'], data['cost'], data['in_stock'], data['vendor_id']
    )
    return jsonify(result), 201 if "message" in result else 500

@app.route('/product/<int:product_id>', methods=['GET'])
def get_product_endpoint(product_id):
    result = get_product(product_id)
    return jsonify(result), 200 if "product_id" in result else 404

@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product_endpoint(product_id):
    data = request.json
    result = update_product(
        product_id, data['brand'], data['description'], data['productName'], 
        data['productType'], data['productSubType'], data['unit_price'], 
        data['cost'], data['in_stock'], data['vendor_id']
    )
    return jsonify(result), 200 if "message" in result else 404

@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product_endpoint(product_id):
    result = delete_product(product_id)
    return jsonify(result), 200 if "message" in result else 404

# CRUD operations for `vendorinfo`
@app.route('/vendor', methods=['POST'])
def create_vendor_endpoint():
    data = request.json
    result = create_vendor(
        data['company_name'], data['department'], data['street_address'], 
        data['city'], data['state'], data['zip_code'], data['phone_number'], 
        data['fax_number'], data['email']
    )
    return jsonify(result), 201 if "message" in result else 500

@app.route('/vendor/<int:vendor_id>', methods=['GET'])
def get_vendor_endpoint(vendor_id):
    result = get_vendor(vendor_id)
    return jsonify(result), 200 if "vendor_id" in result else 404

@app.route('/vendor/<int:vendor_id>', methods=['PUT'])
def update_vendor_endpoint(vendor_id):
    data = request.json
    result = update_vendor(
        vendor_id, data['company_name'], data['department'], data['street_address'], 
        data['city'], data['state'], data['zip_code'], data['phone_number'], 
        data['fax_number'], data['email']
    )
    return jsonify(result), 200 if "message" in result else 404

@app.route('/vendor/<int:vendor_id>', methods=['DELETE'])
def delete_vendor_endpoint(vendor_id):
    result = delete_vendor(vendor_id)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)
