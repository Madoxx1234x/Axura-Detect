from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


def random_response(disaster):
    data = request.get_json() or {}
    # return a pseudo-random risk between 0 and 1
    risk = round(random.random(), 4)
    return jsonify({"disaster": disaster, "risk": risk, "status": "success"})


@app.route("/predict/wildfire", methods=["POST"])
def wildfire():
    return random_response("wildfire")


@app.route("/predict/flood", methods=["POST"])
def flood():
    return random_response("flood")


@app.route("/predict/tornado", methods=["POST"])
def tornado():
    return random_response("tornado")


@app.route("/predict/earthquake", methods=["POST"])
def earthquake():
    return random_response("earthquake")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
