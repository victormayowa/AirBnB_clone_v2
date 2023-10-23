#!/usr/bin/python3
"""
Display a HTML page with filters for AirBnB listings
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda x: x.name)
    places = sorted(storage.all(Place).values(), key=lambda x: x.name)
    return render_template('100-hbnb.html',
                           states=states, cities=cities,
                           amenities=amenities, places=places)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
