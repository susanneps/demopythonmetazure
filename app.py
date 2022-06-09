from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/voorstellen/<voornaam>")
def regelen(voornaam):
    return "Hallo ik ben " + voornaam