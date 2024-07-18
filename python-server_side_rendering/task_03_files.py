from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        return None, str(e)

def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            return [row for row in reader], None
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

