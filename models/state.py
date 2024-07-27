#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models

class State(BaseModel, Base):
    """ State class """
    __table__name = "states"

    name = Column(String(128), nullable=False)

    if models.storage_t == 'db':
        cities = relationship('City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Getter method to return cities with state_id equal to current State.id"""
            list_of_cities = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities




