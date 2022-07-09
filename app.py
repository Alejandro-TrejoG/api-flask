from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "HOLA MUNDO"})


if __name__ == "__main__":
    app.run(threaded=True, port=5000)