#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Integer, Column, Float
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "place"

    city_id = Column(String(60), nullable=False, foreign_key="cities.id")
    user_id =  Column(String(60), nullable=False, foreign_key="user.id")
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default_value=0)
    number_bathrooms = Column(Integer, nullable=False, default_value=0)
    max_guest =  Column(Integer, nullable=False, default_value=0)
    price_by_night = Column(Integer, nullable=False, default_value=0)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []

    if models.storage_t = 'db':
        reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """Getter method to return reviews with place_id equal to current Place.id"""
            list_of_reviews = []
            for review in models.storage.all(Reviews).values():
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

    from sqlalchemy import Table
    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
            Column('place_id', String(60), foreign_key="places.id", nullable=False, primary_key=True)
            Column('amenity_id', String(60), foreign_key="amenities.id", nullable=False, primary_key=True))

    if models.storage_t = 'db':
        pass

