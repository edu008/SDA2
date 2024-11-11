import mariadb
import sys

# Establish database connection
def get_db_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3306,
            database="order"
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# CRUD operations for the `orders` table
def create_order(OTID, stock_amount, product_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO orders (OTID, stock_amount, product_id) VALUES (?, ?, ?)",
            (OTID, stock_amount, product_id)
        )
        conn.commit()
        return {"message": "Order created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_order(OID):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT OID, OTID, stock_amount, product_id FROM orders WHERE OID = ?", (OID,))
        row = cur.fetchone()
        if row:
            return {
                "OID": row[0],
                "OTID": row[1],
                "stock_amount": row[2],
                "product_id": row[3]
            }
        else:
            return {"error": "Order not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_order(OID, OTID, stock_amount, product_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE orders SET OTID = ?, stock_amount = ?, product_id = ? WHERE OID = ?",
            (OTID, stock_amount, product_id, OID)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Order not found"}
        return {"message": "Order updated successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_order(OID):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM orders WHERE OID = ?", (OID,))
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Order not found"}
        return {"message": "Order deleted successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
