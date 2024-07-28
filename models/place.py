#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import String, Integer, Column, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id =  Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=True)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest =  Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if models.storage_t == 'db':
        reviews = relationship('Review', backref='place', cascade='all, delete-orphan')
    else:
        @property
        def reviews(self):
            """Getter method to return reviews with place_id equal to current Place.id"""
            list_of_reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    list_of_reviews.append(review)
            return list_of_reviews

    metadata = Base.metadata
    place_amenity = Table('place_amenity', metadata,
            Column('place_id', String(60), ForeignKey("places.id"), nullable=False, primary_key=True),
            Column('amenity_id', String(60), ForeignKey("amenities.id"), nullable=False, primary_key=True))

    if models.storage_t == 'db':
        pass

