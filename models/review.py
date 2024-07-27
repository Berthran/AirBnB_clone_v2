#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"

    place_id = Column(String(60), nullabel=False, foreign_key='places.id')
    user_id = Column(String(60), nullabel=False, foreign_key='users.id')
    text = Column(String(1024), nullabel=False)
