from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

metrics = {
    "invocations": 0,
    "http_status_codes": {
        "200": 0,
        "500": 0
    }
}

@app.route('/')
def home():
    metrics["invocations"] += 1
    status_code = random.choice([200, 500])
    metrics["http_status_codes"][str(status_code)] += 1
    return jsonify({"message": "Hello, Flask!", "status_code": status_code}), status_code

@app.route('/metrics')
def prometheus_metrics():
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)