from flask import Flask, jsonify
from .etl import run_etl
import json

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run():
    run_etl()
    return jsonify({"status": "ETL complete"}), 200

@app.route("/data", methods=["GET"])
def get_data():
    with open("src/processed.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)