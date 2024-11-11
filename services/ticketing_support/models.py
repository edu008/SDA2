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
            database="order"  # Adjust if different
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# CRUD for `ticket_system`
def create_ticket(date, company_name, time, quantity, subtotal, total, cost, discount, tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO ticket_system (date, company_name, time, quantity, subtotal, total, cost, discount, tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (date, company_name, time, quantity, subtotal, total, cost, discount, tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id)
        )
        conn.commit()
        return {"message": "Ticket created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_ticket(ticket_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT * FROM ticket_system WHERE ticket_id = ?", (ticket_id,))
        row = cur.fetchone()
        return dict(zip([desc[0] for desc in cur.description], row)) if row else {"error": "Ticket not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_ticket(ticket_id, date, company_name, time, quantity, subtotal, total, cost, discount, tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE ticket_system SET date = ?, company_name = ?, time = ?, quantity = ?, subtotal = ?, total = ?, cost = ?, discount = ?, tax = ?, tax_rate = ?, cash = ?, credit = ?, cart_purchase = ?, customer_id = ?, employee_id = ? WHERE ticket_id = ?",
            (date, company_name, time, quantity, subtotal, total, cost, discount, tax, tax_rate, cash, credit, cart_purchase, customer_id, employee_id, ticket_id)
        )
        conn.commit()
        return {"message": "Ticket updated successfully"} if cur.rowcount else {"error": "Ticket not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_ticket(ticket_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM ticket_system WHERE ticket_id = ?", (ticket_id,))
        conn.commit()
        return {"message": "Ticket deleted successfully"} if cur.rowcount else {"error": "Ticket not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# CRUD for `ticket_history`
def create_ticket_history(ticket_id, change_date, status, priority, remarks):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO ticket_history (ticket_id, change_date, status, priority, remarks) VALUES (?, ?, ?, ?, ?)",
            (ticket_id, change_date, status, priority, remarks)
        )
        conn.commit()
        return {"message": "Ticket history created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_ticket_history(history_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT * FROM ticket_history WHERE history_id = ?", (history_id,))
        row = cur.fetchone()
        return dict(zip([desc[0] for desc in cur.description], row)) if row else {"error": "History not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_ticket_history(history_id, ticket_id, change_date, status, priority, remarks):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE ticket_history SET ticket_id = ?, change_date = ?, status = ?, priority = ?, remarks = ? WHERE history_id = ?",
            (ticket_id, change_date, status, priority, remarks, history_id)
        )
        conn.commit()
        return {"message": "Ticket history updated successfully"} if cur.rowcount else {"error": "History not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_ticket_history(history_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM ticket_history WHERE history_id = ?", (history_id,))
        conn.commit()
        return {"message": "History deleted successfully"} if cur.rowcount else {"error": "History not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# CRUD for `ticket_type`
def create_ticket_type(type_name, description):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO ticket_type (type_name, description) VALUES (?, ?)",
            (type_name, description)
        )
        conn.commit()
        return {"message": "Ticket type created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_ticket_type(type_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT * FROM ticket_type WHERE type_id = ?", (type_id,))
        row = cur.fetchone()
        return dict(zip([desc[0] for desc in cur.description], row)) if row else {"error": "Ticket type not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_ticket_type(type_id, type_name, description):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE ticket_type SET type_name = ?, description = ? WHERE type_id = ?",
            (type_name, description, type_id)
        )
        conn.commit()
        return {"message": "Ticket type updated successfully"} if cur.rowcount else {"error": "Ticket type not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_ticket_type(type_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM ticket_type WHERE type_id = ?", (type_id,))
        conn.commit()
        return {"message": "Ticket type deleted successfully"} if cur.rowcount else {"error": "Ticket type not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
