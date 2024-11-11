import mariadb
import sys

def get_db_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="example",
            host="localhost",
            port=3306,
            database="sda2_database"
        )
        print("Connection successful!")
        return conn
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
