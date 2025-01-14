#!/usr/bin/python3
""" This module starts a Flask web application. """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ Displays "Hello HBNB!" on the main page. """
    return "Helo HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """" Displays "HBNB". """
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Displas "C" followed by text <text>.
    Underscores are replaced with whitespace. """
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
