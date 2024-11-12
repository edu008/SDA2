import mariadb
import sys

# Establish database connection
def get_db_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3311,
            database="tax"  # Adjust this if the database name for taxes is different
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# CRUD operations for the `tax_table`
def create_tax(tax_year, state_tax, county_tax, city_rate, tax_rate):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO tax_table (tax_year, state_tax, county_tax, city_rate, tax_rate) VALUES (?, ?, ?, ?, ?)",
            (tax_year, state_tax, county_tax, city_rate, tax_rate)
        )
        conn.commit()
        return {"message": "Tax record created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_tax(TTID):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT TTID, tax_year, state_tax, county_tax, city_rate, tax_rate FROM tax_table WHERE TTID = ?", (TTID,))
        row = cur.fetchone()
        if row:
            return {
                "TTID": row[0],
                "tax_year": row[1],
                "state_tax": row[2],
                "county_tax": row[3],
                "city_rate": row[4],
                "tax_rate": row[5]
            }
        else:
            return {"error": "Tax record not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_tax(TTID, tax_year, state_tax, county_tax, city_rate, tax_rate):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE tax_table SET tax_year = ?, state_tax = ?, county_tax = ?, city_rate = ?, tax_rate = ? WHERE TTID = ?",
            (tax_year, state_tax, county_tax, city_rate, tax_rate, TTID)
        )
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Tax record not found"}
        return {"message": "Tax record updated successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_tax(TTID):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM tax_table WHERE TTID = ?", (TTID,))
        conn.commit()
        if cur.rowcount == 0:
            return {"error": "Tax record not found"}
        return {"message": "Tax record deleted successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
