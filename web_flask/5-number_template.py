#!/usr/bin/python3
'''
A script that starts a Flask web application.

Defines routes for:
/, /hbnb, /c/<text>, /python, /python/, /python/<text>, /number/<n>,
/number_template/<n>
'''

from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    '''Displays 'Python' followed by the value of the text variable'''
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    '''Displays the value of n only if it is integer'''
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_n_template(n):
    '''Display a HTML page only if n is an integer'''
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
