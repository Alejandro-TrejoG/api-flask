from urllib import response
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=["GET"])
def home():
    file = open("./spam_ham.txt", "r")
    spam = file.read(3)
    ham = file.read(3)
    response = jsonify({"spam": str(spam), "ham": str(ham)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/prediccion", methods=["GET"])
def prediction():
    file = open("./accuracy.txt", "r")
    prediccion = file.read()
    response = jsonify({"prediction": str(prediccion)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


@app.route("/send-file", methods=["GET"])
def file():
    response = send_file("./correos.jpg", attachment_filename="correos.jpg")
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response


if __name__ == "__main__":
    app.run(threaded=True, port=5000)