#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def flask_hello():
    """Return string response"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return response"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Replace underscores with spaces in the text"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
