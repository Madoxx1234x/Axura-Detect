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

if __name__ == "__main__":
    app.run(debug=True)
