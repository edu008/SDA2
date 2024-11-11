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
            database="order"  # Adjust if the database name is different
        )
        cur = conn.cursor()
        return conn, cur
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)

# CRUD for `product_inventory`
def create_product(brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO product_inventory (brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id)
        )
        conn.commit()
        return {"message": "Product created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_product(product_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT * FROM product_inventory WHERE product_id = ?", (product_id,))
        row = cur.fetchone()
        return dict(zip([desc[0] for desc in cur.description], row)) if row else {"error": "Product not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_product(product_id, brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE product_inventory SET brand = ?, description = ?, productName = ?, productType = ?, productSubType = ?, unit_price = ?, cost = ?, in_stock = ?, vendor_id = ? WHERE product_id = ?",
            (brand, description, productName, productType, productSubType, unit_price, cost, in_stock, vendor_id, product_id)
        )
        conn.commit()
        return {"message": "Product updated successfully"} if cur.rowcount else {"error": "Product not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_product(product_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM product_inventory WHERE product_id = ?", (product_id,))
        conn.commit()
        return {"message": "Product deleted successfully"} if cur.rowcount else {"error": "Product not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

# CRUD for `vendorinfo`
def create_vendor(company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "INSERT INTO vendorinfo (company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email)
        )
        conn.commit()
        return {"message": "Vendor created successfully"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def get_vendor(vendor_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("SELECT * FROM vendorinfo WHERE vendor_id = ?", (vendor_id,))
        row = cur.fetchone()
        return dict(zip([desc[0] for desc in cur.description], row)) if row else {"error": "Vendor not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def update_vendor(vendor_id, company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email):
    conn, cur = get_db_connection()
    try:
        cur.execute(
            "UPDATE vendorinfo SET company_name = ?, department = ?, street_address = ?, city = ?, state = ?, zip_code = ?, phone_number = ?, fax_number = ?, email = ? WHERE vendor_id = ?",
            (company_name, department, street_address, city, state, zip_code, phone_number, fax_number, email, vendor_id)
        )
        conn.commit()
        return {"message": "Vendor updated successfully"} if cur.rowcount else {"error": "Vendor not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()

def delete_vendor(vendor_id):
    conn, cur = get_db_connection()
    try:
        cur.execute("DELETE FROM vendorinfo WHERE vendor_id = ?", (vendor_id,))
        conn.commit()
        return {"message": "Vendor deleted successfully"} if cur.rowcount else {"error": "Vendor not found"}
    except mariadb.Error as e:
        return {"error": str(e)}
    finally:
        cur.close()
        conn.close()
