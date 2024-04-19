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


@app.route("/python", strict_slashes=False)
def python_text1():
    """python page """
    return "Python is cool"


@app.route("/python/", strict_slashes=False)
def python_text2():
    """ redirects if slash is provided """
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """ python page display """
    text = escape(text.replace("_", " "))
    return "Python {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
