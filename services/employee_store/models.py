import mariadb
import sys

# Verbindung zur Datenbank herstellen
def get_db_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3306,
            database="employee"  # Passe dies an deinen DB-Namen an
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# CREATE
def create_employee(first_name, last_name, email, phone_number, customer_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO employee_info (first_name, last_name, email, phone_number, customer_id) VALUES (?, ?, ?, ?, ?, ?)",
            (first_name, last_name, email, phone_number, customer_id)
        )
        conn.commit()
        return {"message": "Employee created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# READ
def get_employee(employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT employee_id, first_name, last_name, email, phone_number, customer_id FROM employee_info WHERE employee_id = ?", (employee_id,))
        row = cur.fetchone()
        if row:
            return {
                "employee_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
                "phone_number": row[4],
                "customer_id": row[5]
            }
        else:
            return {"error": "Employee not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# UPDATE
def update_employee(employee_id, first_name, last_name, email, phone_number):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE employee_info SET first_name = ?, last_name = ?, email = ?, phone_number = ? WHERE employee_id = ?",
            (first_name, last_name, email, phone_number, employee_id)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Employee not found"}
        return {"message": "Employee updated successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# DELETE
def delete_employee(employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM employee_info WHERE employee_id = ?", (employee_id,))
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Employee not found"}
        return {"message": "Employee deleted successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
