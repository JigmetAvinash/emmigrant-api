from flask import Flask, jsonify, request
import csv


filename = "data.csv"

def filter_csv_with_column(filename, column_name, value):
    results = []

    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row[column_name]== value:
                results.append(row)
                return results
            else:
                return "There seems like an error, 404 Not found! Please contact Avinash. (github.com/JigmetAvinash)"
                

    

app = Flask(__name__)

@app.route('/filter', methods=['GET'])
def filter_csv():
    column_name = request.args.get('column_name')
    value = request.args.get('value')

    if not column_name or not value:
        return jsonify({"error": "You forgot something lil bro, Provide both 'column' and 'value' as a query parameter"}), 400
    
    filename = "data.csv"

    try:
        results = filter_csv_with_column(filename, column_name, value)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
