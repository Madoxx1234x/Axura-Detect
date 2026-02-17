from flask import Flask, request, jsonify
from flask_cors import CORS

from wildfire_ai import predict_wildfire
from flood_ai import predict_flood
from tornado_ai import predict_tornado
from earthquake_ai import predict_earthquake

app = Flask(__name__)
CORS(app)

@app.route("/predict/wildfire", methods=["POST"])
def wildfire():
    data = request.json
    risk = predict_wildfire(data)
    return jsonify({"disaster": "wildfire", "risk": risk, "status": "success"})

@app.route("/predict/flood", methods=["POST"])
def flood():
    data = request.json
    risk = predict_flood(data)
    return jsonify({"disaster": "flood", "risk": risk, "status": "success"})

@app.route("/predict/tornado", methods=["POST"])
def tornado():
    data = request.json
    risk = predict_tornado(data)
    return jsonify({"disaster": "tornado", "risk": risk, "status": "success"})

@app.route("/predict/earthquake", methods=["POST"])
def earthquake():
    data = request.json
    risk = predict_earthquake(data)
    return jsonify({"disaster": "earthquake", "risk": risk, "status": "success"})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    host = os.environ.get("HOST", "0.0.0.0")
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host=host, port=port, debug=debug)
