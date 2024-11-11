import os
import mariadb
import json

def handle(event, context):
    # Connect to the logs database
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3307,
            database="customer"
        )
        cur = conn.cursor()
    except mariadb.Error as e:
        return {"error": f"Error connecting to logs database: {e}"}
    
    # Parse incoming event data
    try:
        data = json.loads(event.body)
        action = data.get("action", "unknown")
        customer_id = data.get("customer_id")
        details = data.get("details", {})
        
        # Insert log entry into the logs database
        cur.execute(
            "INSERT INTO customer_logs (action, customer_id, details) VALUES (?, ?, ?)",
            (action, customer_id, json.dumps(details))
        )
        conn.commit()
        
        return {"status": "Log entry created successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
