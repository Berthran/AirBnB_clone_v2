#!/usr/bin/python3
'''
A script that starts a Flask web application.

Defines routes for / and /hbnb
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
