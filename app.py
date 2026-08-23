from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

@app.route("/api", methods=["GET"])
def get_data():
    # Read data from backend file
    data_path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(data_path, "r") as file:
        data = json.load(file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
