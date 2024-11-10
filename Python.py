import sys
import mariadb

try:
    conn = mariadb.connect(
        user="root",
        password="example",
        host="localhost",
        port=3306,
        database="sda2_database"
    )
    print("Connection successful!")
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()

query = "SELECT * FROM product_inventory"
try:
    cur.execute(query)
    output = cur.fetchall()
    print(output)
except mariadb.Error as e:
    print(f"Error executing query: {e}")
finally:
    cur.close()
    conn.close()
