from flask import Flask, request, jsonify, g
import mariadb
import sys

app = Flask(__name__)

# Establish a new connection for each request
def get_db_connection():
    if 'conn' not in g:
        try:
            g.conn = mariadb.connect(
                user="root",
                password="example",
                host="localhost",
                port=3306,
                database="customer"
            )
            g.cur = g.conn.cursor()
            print("Connection successful!")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    return g.conn, g.cur

# Create customer (CREATE)
@app.route('/customer', methods=['POST'])
def create_customer():
    data = request.json
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO customer_info (name, email) VALUES (?, ?)",
            (data['name'], data['email'])
        )
        conn.commit()
        return jsonify({"message": "Customer created successfully"}), 201
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# Get customer (READ)
@app.route('/customer/<int:id>', methods=['GET'])
def get_customer(id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT customer_id, first_name, email FROM customer_info WHERE customer_id = ?", (id,))
        row = cur.fetchone()
        if row:
            result = {"id": row[0], "name": row[1], "email": row[2]}
            return jsonify(result), 200
        else:
            return jsonify({"error": "Customer not found"}), 404
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# Update customer (UPDATE)
@app.route('/customer/<int:id>', methods=['PUT'])
def update_customer(id):
    data = request.json
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE customer_info SET name = ?, email = ? WHERE customer_id  = ?",
            (data['name'], data['email'], id)
        )
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer updated successfully"}), 200
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# Delete customer (DELETE)
@app.route('/customer/<int:id>', methods=['DELETE'])
def delete_customer(id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM customer_info WHERE customer_id = ?", (id,))
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"error": "Customer not found"}), 404
        return jsonify({"message": "Customer deleted successfully"}), 200
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# Close connection after each request
@app.teardown_appcontext
def close_connection(exception):
    conn = g.pop('conn', None)
    cur = g.pop('cur', None)
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
        print("Database connection closed")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
