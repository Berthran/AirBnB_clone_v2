#!/usr/bin/python3
'''
A script that starts a Flask web application.

Defines routes for /, /hbnb and /c/<text>
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def show_homepage():
    '''Handles the logic for the home page'''
    return f"Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    '''Displays the text HBNB'''
    return f"HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    '''Displays 'C' followed by the value of the text variable'''
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
