from fastapi import fastapi
import sqlite3

def get_employee():
    connection = sqlite3.connect("employee.db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    connection.close()
    return employees

def get_products():
    connection = sqlite3.connect("products.db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    connection.close()
    return products

@app.get("/combined-data")
def get_combined_data():
    employee = get_employee()
    products = get_products()
    return {
        "employee": employee,
        "products": products
    }