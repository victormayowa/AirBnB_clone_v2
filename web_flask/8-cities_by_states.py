#!/usr/bin/python3
"""
Display a list of all states with their associated cities
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = {}

    if storage.__class__.__name__ == 'DBStorage':
        for state in states:
            cities[state.id] = sorted(state.cities, key=lambda x: x.name)
    else:
        for state in states:
            cities[state.id] = sorted(state.cities(), key=lambda x: x.name)

    return render_template('8-cities_by_states.html', states=states, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
