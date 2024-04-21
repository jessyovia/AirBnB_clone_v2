#!/usr/bin/python3
"""starts a Flask web application"""


from models.state import State
from models.amenity import Amenity
from models import storage
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """States template"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html",
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exception):
    """Removes the current Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
