#!/usr/bin/python3
'''
A script that starts a Flask web application.

Defines routes for
/states_list
'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def c_by_s():
    '''Displays a HTML page'''
    states = storage.all(State).values()
    cities = storage.all(City).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    sorted_cities = sorted(cities, key=lambda x: x.name)
    return render_template('8-cities_by_states.html',
                           states=sorted_states,
                           cities=sorted_cities)


@app.teardown_appcontext
def teardown_db(exception=None):
    '''Removes the current SQLAlchemy Session'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=True)
