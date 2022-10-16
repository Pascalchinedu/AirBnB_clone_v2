#!/usr/bin/python3
""" This module defines route in flask. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ This method returns Hello HBNB page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_page():
    """ This method returns HBNB page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_page(text):
    """ This method returns C page """
    return "C %s" % text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)