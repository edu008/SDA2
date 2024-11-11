from flask import Flask, request, jsonify
from models import (
    create_ticket, get_ticket, update_ticket, delete_ticket,
    create_ticket_history, get_ticket_history, update_ticket_history, delete_ticket_history,
    create_ticket_type, get_ticket_type, update_ticket_type, delete_ticket_type
)

app = Flask(__name__)

# CRUD operations for `ticket_system`
@app.route('/ticket', methods=['POST'])
def create_ticket_endpoint():
    data = request.json
    result = create_ticket(
        data['date'], data.get('company_name'), data['time'], data['quantity'], 
        data['subtotal'], data['total'], data['cost'], data.get('discount'), 
        data['tax'], data['tax_rate'], data['cash'], data['credit'], 
        data['cart_purchase'], data.get('customer_id'), data['employee_id']
    )
    return jsonify(result), 201 if "message" in result else 500

@app.route('/ticket/<int:ticket_id>', methods=['GET'])
def get_ticket_endpoint(ticket_id):
    result = get_ticket(ticket_id)
    return jsonify(result), 200 if "ticket_id" in result else 404

@app.route('/ticket/<int:ticket_id>', methods=['PUT'])
def update_ticket_endpoint(ticket_id):
    data = request.json
    result = update_ticket(
        ticket_id, data['date'], data.get('company_name'), data['time'], 
        data['quantity'], data['subtotal'], data['total'], data['cost'], 
        data.get('discount'), data['tax'], data['tax_rate'], 
        data['cash'], data['credit'], data['cart_purchase'], 
        data.get('customer_id'), data['employee_id']
    )
    return jsonify(result), 200 if "message" in result else 404

@app.route('/ticket/<int:ticket_id>', methods=['DELETE'])
def delete_ticket_endpoint(ticket_id):
    result = delete_ticket(ticket_id)
    return jsonify(result), 200 if "message" in result else 404

# CRUD operations for `ticket_history`
@app.route('/ticket_history', methods=['POST'])
def create_ticket_history_endpoint():
    data = request.json
    result = create_ticket_history(data['ticket_id'], data['change_date'], data['status'], data['priority'], data.get('remarks'))
    return jsonify(result), 201 if "message" in result else 500

@app.route('/ticket_history/<int:history_id>', methods=['GET'])
def get_ticket_history_endpoint(history_id):
    result = get_ticket_history(history_id)
    return jsonify(result), 200 if "history_id" in result else 404

@app.route('/ticket_history/<int:history_id>', methods=['PUT'])
def update_ticket_history_endpoint(history_id):
    data = request.json
    result = update_ticket_history(history_id, data['ticket_id'], data['change_date'], data['status'], data['priority'], data.get('remarks'))
    return jsonify(result), 200 if "message" in result else 404

@app.route('/ticket_history/<int:history_id>', methods=['DELETE'])
def delete_ticket_history_endpoint(history_id):
    result = delete_ticket_history(history_id)
    return jsonify(result), 200 if "message" in result else 404

# CRUD operations for `ticket_type`
@app.route('/ticket_type', methods=['POST'])
def create_ticket_type_endpoint():
    data = request.json
    result = create_ticket_type(data['type_name'], data.get('description'))
    return jsonify(result), 201 if "message" in result else 500

@app.route('/ticket_type/<int:type_id>', methods=['GET'])
def get_ticket_type_endpoint(type_id):
    result = get_ticket_type(type_id)
    return jsonify(result), 200 if "type_id" in result else 404

@app.route('/ticket_type/<int:type_id>', methods=['PUT'])
def update_ticket_type_endpoint(type_id):
    data = request.json
    result = update_ticket_type(type_id, data['type_name'], data.get('description'))
    return jsonify(result), 200 if "message" in result else 404

@app.route('/ticket_type/<int:type_id>', methods=['DELETE'])
def delete_ticket_type_endpoint(type_id):
    result = delete_ticket_type(type_id)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)
