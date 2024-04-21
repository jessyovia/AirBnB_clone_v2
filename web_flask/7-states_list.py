#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """HTML page and states listed in alphabetical order"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", sorted_states=sorted_states)


@app.teardown_appcontext
def teardown(self):
    """Closes the session after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
