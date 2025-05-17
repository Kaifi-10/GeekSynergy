from fastapi import FastAPI
import sqlite3

app = FastAPI()
def get_employee():
    connection = sqlite3.connect("employee.db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    connection.close()
    return [{"id": r[0], "name": r[1], "position": r[2], "department": r[3]} for r in rows]

def get_products():
    connection = sqlite3.connect("products.db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    connection.close()
    return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]} for r in rows]

@app.get("/combined-data")
def get_combined_data():
    employee = get_employee()
    products = get_products()
    return {
        "employee": employee,
        "products": products
    }