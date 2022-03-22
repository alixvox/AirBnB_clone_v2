#!/usr/bin/python3
""" This module starts a Flask web application. """
from flask import Flask, render_template
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

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text='is cool'):
    """ Displays "Python " with text <text> after.
    <text> default is "is cool". """
    return "Python {}".format(text.replace('_', ' '))

@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Displays number <int:n> followed by "is a number". """
    return "%d is a number" % n

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Displays the HTML template for <int:n>. """
    return render_template('5-number.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
