#!/usr/bin/python3
"""
flask app
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ the root homepage """
    return("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hello_sec():
    """ for route /hbnb """
    return("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def arg_input(text):
    """dispalying the text arg in browser"""
    text = escape(text.replace("_", " "))
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
