from flask import Flask, request, jsonify, g
import mariadb
import sys

app = Flask(__name__)

# Funktion für die Datenbankverbindung pro Anfrage
def get_db_connection():
    if 'conn' not in g:
        try:
            g.conn = mariadb.connect(
                user="root",
                password="example",
                host="localhost",
                port=3306,
                database="employee"  # Passe dies an deinen DB-Namen an
            )
            g.cur = g.conn.cursor()
            print("Connection successful!")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
    return g.conn, g.cur

# CREATE: Einen neuen Mitarbeiter hinzufügen
@app.route('/employee', methods=['POST'])
def create_employee():
    data = request.json
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO employee_info (first_name, last_name, email, phone_number, position, salary) VALUES (?, ?, ?, ?, ?, ?)",
            (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['position'], data['salary'])
        )
        conn.commit()
        return jsonify({"message": "Employee created successfully"}), 201
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# READ: Einen Mitarbeiter abrufen
@app.route('/employee/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT employee_id, first_name, last_name, email, phone_number, position, salary FROM employee_info WHERE employee_id = ?", (employee_id,))
        row = cur.fetchone()
        if row:
            result = {
                "employee_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "phone_number": row[4],
                "position": row[5],
                "salary": row[6]
            }
            return jsonify(result), 200
        else:
            return jsonify({"error": "Employee not found"}), 404
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# UPDATE: Einen Mitarbeiter aktualisieren
@app.route('/employee/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.json
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE employee_info SET first_name = ?, last_name = ?, email = ?, phone_number = ?, position = ?, salary = ? WHERE employee_id = ?",
            (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['position'], data['salary'], employee_id)
        )
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"error": "Employee not found"}), 404
        return jsonify({"message": "Employee updated successfully"}), 200
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# DELETE: Einen Mitarbeiter löschen
@app.route('/employee/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM employee_info WHERE employee_id = ?", (employee_id,))
        conn.commit()
        if cur.rowcount == 0:
            return jsonify({"error": "Employee not found"}), 404
        return jsonify({"message": "Employee deleted successfully"}), 200
    except mariadb.Error as e:
        return jsonify({"error": str(e)}), 500

# Schließt die Verbindung nach jeder Anfrage
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
    app.run(host='0.0.0.0', port=5002)
