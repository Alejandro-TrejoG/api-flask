from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    file = open("./spam_ham.txt", "r")
    spam = file.read(3)
    ham = file.read(3)
    return jsonify({"spam": str(spam), "ham": str(ham)})


@app.route("/prediccion", methods=["GET"])
def prediction():
    file = open("./accuracy.txt", "r")
    prediccion = file.read()
    return jsonify({"prediction": str(prediccion)})


@app.route("/send-file", methods=["GET"])
def file():
    return send_file("./correos.jpg", attachment_filename="correos.jpg")


if __name__ == "__main__":
    app.run(threaded=True, port=5000)