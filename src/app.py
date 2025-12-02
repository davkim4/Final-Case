from flask import Flask, jsonify
from .etl import run_etl
import json
from pathlib import Path

app = Flask(__name__)

@app.route("/run", methods=["GET"])
def run():
    run_etl()
    return jsonify({"status": "ETL complete"}), 200

@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(json.loads(Path("src/processed.json").read_text()))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)