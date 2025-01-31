from flask import Flask, jsonify, request
import csv
from datetime import datetime

app = Flask(__name__)

filename = "data.csv"
comments_filename = "comments.csv"

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

@app.route('/', methods=['GET'])
def main():
    return "Welcome to the Emigrant api! To use this, please check readme.md file."

# API Requests:
# GET /api/v1/filter?column=<column_name>&value=<value>
# Sample: curl "http://127.0.0.1:5000/api/v1/filter?column=Entity&value=India"
@app.route('/api/v1/filter', methods=['GET'])
def filter_csv():
    column_name = request.args.get('column')
    value = request.args.get('value')

    if not column_name or not value:
        return jsonify({"error": "Missing 'column' or 'value' parameter"}), 400

    results = filter_csv_with_column(filename, column_name, value)
    if isinstance(results, str):
        return jsonify({"error": results}), 404

    return jsonify(results), 200

# API Requests:
# GET /api/v1/unique_values?column=<column_name>
# Sample: curl "http://127.0.0.1:5000/api/v1/unique_values?column=Entity"
@app.route('/api/v1/unique_values', methods=['GET'])
def get_unique_values():
    column_name = request.args.get('column')

    if not column_name:
        return jsonify({"error": "Missing 'column' parameter"}), 400

    unique_values = set()
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            if column_name not in reader.fieldnames:
                return jsonify({"error": f"Column '{column_name}' does not exist in the CSV file."}), 404
            for row in reader:
                unique_values.add(row[column_name])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(list(unique_values)), 200

# API Requests:
# GET /api/v1/total_records
# Sample: curl "http://127.0.0.1:5000/api/v1/total_records"
@app.route('/api/v1/total_records', methods=['GET'])
def get_total_records():
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            total_records = sum(1 for row in reader)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"total_records": total_records}), 200

# API Requests:
# POST /api/v1/add_comment
# Body: { "User": "<user>", "Username": "<username>", "Comment": "<comment>", "Date": "<date>", "ExtraInfo": "<extra_info>" }
# Sample: curl -X POST -H "Content-Type: application/json" -d '{"User": "JohnDoe", "Username": "johndoe123", "Comment": "This is a test comment", "Date": "2023-10-10", "ExtraInfo": "Some extra info"}' "http://127.0.0.1:5000/api/v1/add_comment"
@app.route('/api/v1/add_comment', methods=['POST'])
def add_comment():
    user = request.json.get('User')
    username = request.json.get('Username')
    comment = request.json.get('Comment')
    date = datetime.now().strftime("%Y-%m-%d")
    extra_info = request.json.get('ExtraInfo')

    if not user or not username or not comment or not date or not extra_info:
        return jsonify({"error": "Missing 'User', 'Username', 'Comment', 'Date', or 'ExtraInfo' parameter"}), 400

    try:
        with open(comments_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user, username, comment, date, extra_info])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Comment added successfully"}), 201

# API Requests:
# GET /api/v1/comments
# Sample: curl "http://127.0.0.1:5000/api/v1/comments"
@app.route('/api/v1/comments', methods=['GET'])
def get_all_comments():
    comments = []
    try:
        with open(comments_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                comments.append(row)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(comments), 200

# API Requests:
# GET /api/v1/comments?username=<username>
# Sample: curl "http://127.0.0.1:5000/api/v1/comments?username=johndoe123"
@app.route('/api/v1/comments', methods=['GET'])
def get_comments_by_username():
    username = request.args.get('username')
    comments = []
    try:
        with open(comments_filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if username and row['Username'] == username:
                    comments.append(row)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify(comments), 200

if __name__ == '__main__':
    app.run(debug=True)
