import mariadb
import sys

# Datenbankverbindung herstellen
def get_db_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3307,
            database="customer"
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)


# Funktionen für CRUD-Operationen

def create_customer(name, email):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO customer_info (first_name, email) VALUES (?, ?)",
            (name, email)
        )
        conn.commit()
        return {"message": "Customer created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_customer(customer_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT customer_id, first_name, email FROM customer_info WHERE customer_id = ?", (customer_id,))
        row = cur.fetchone()
        if row:
            return {"id": row[0], "name": row[1], "email": row[2]}
        else:
            return {"error": "Customer not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_customer(customer_id, name, email):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE customer_info SET first_name = ?, email = ? WHERE customer_id = ?",
            (name, email, customer_id)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Customer not found"}
        return {"message": "Customer updated successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_customer(customer_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM customer_info WHERE customer_id = ?", (customer_id,))
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Customer not found"}
        return {"message": "Customer deleted successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
