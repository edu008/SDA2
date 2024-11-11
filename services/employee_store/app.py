from flask import Flask, request, jsonify
from models import create_employee, get_employee, update_employee, delete_employee

app = Flask(__name__)

# CREATE
@app.route('/employee', methods=['POST'])
def create_employee_endpoint():
    data = request.json
    result = create_employee(data['first_name'], data['last_name'], data['email'], data['phone_number'], data['position'], data['salary'])
    return jsonify(result), 201 if "message" in result else 500

# READ
@app.route('/employee/<int:id>', methods=['GET'])
def get_employee_endpoint(id):
    result = get_employee(id)
    return jsonify(result), 200 if "id" in result else 404

# UPDATE
@app.route('/employee/<int:id>', methods=['PUT'])
def update_employee_endpoint(id):
    data = request.json
    result = update_employee(id, data['first_name'], data['last_name'], data['email'], data['phone_number'], data['position'], data['salary'])
    return jsonify(result), 200 if "message" in result else 404

# DELETE
@app.route('/employee/<int:id>', methods=['DELETE'])
def delete_employee_endpoint(id):
    result = delete_employee(id)
    return jsonify(result), 200 if "message" in result else 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
