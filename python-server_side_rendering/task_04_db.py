from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f), None
    except Exception as e:
        return None, str(e)

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader], None
    except Exception as e:
        return None, str(e)

def read_sqlite_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
        conn.close()
        return products, None
    except Exception as e:
        return None, str(e)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    products = []
    error = None

    if source == 'json':
        products, error = read_json_file('products.json')
    elif source == 'csv':
        products, error = read_csv_file('products.csv')
    elif source == 'sql':
        products, error = read_sqlite_db()
    else:
        error = "Wrong source"

    if products is not None and product_id is not None:
        products = [p for p in products if int(p['id']) == product_id]
        if not products:
            error = "Product not found"
    elif products is None:
        error = "Error reading the data file"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

