#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state')

    if os.getenv('HBNB_TYPE_STORAGE') == 'file':
            """ Getter method to return the list of City instances
            """
            from models import storage
            city_objs = storage.all('City')
            return [
                    city for city in city_objs.values()
                    if city.state_id == self.id
                    ]
