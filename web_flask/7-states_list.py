#!/usr/bin/python3
""" This module starts a Flask web application. """
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays an HTML page with all State objects
    in DB storage sorted A-Z. """
    allstates=storage.all(State)
    return render_template('7-states_list.html', allstates=allstates)

@app.teardown_appcontext
def teardown(done):
    """ Removes the current SQAlchemy session. """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
