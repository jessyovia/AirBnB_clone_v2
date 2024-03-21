#!/usr/bin/python3
"""Module for Amenity class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Class representing an Amenity."""
    __tablename__ = 'amenities'


    name = Column(String(128), nullable=False)


    # Define relationship with Place using place_amenities table
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
