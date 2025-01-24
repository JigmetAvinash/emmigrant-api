from flask import Flask, jsonify, request
import csv

app = Flask(__name__)

filename = "data.csv"

def filter_csv_with_column(filename, column_name, value):
    results = []

    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            if column_name not in reader.fieldnames:
                return f"Column '{column_name}' does not exist in the CSV file."
            for row in reader:
                if row[column_name] == value:
                    results.append(row)
    except Exception as e:
        return str(e)

    if results:
        return results
    else:
        return "No matching records found."

@app.route('/filter', methods=['GET'])
def filter_csv():
    column_name = request.args.get('column')
    value = request.args.get('value')

    if not column_name or not value:
        return jsonify({"error": "Missing 'column' or 'value' parameter"}), 400

    results = filter_csv_with_column(filename, column_name, value)
    if isinstance(results, str):
        return jsonify({"error": results}), 404
    return jsonify(results), 200

if __name__ == '__main__':
    app.run(debug=True)
