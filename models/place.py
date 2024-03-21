#!/usr/bin/python3
"""Place Module for HBNB project"""

from os import getenv
from sqlalchemy import Column, Float, ForeignKey
from sqlalchemy import Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity

# Association table for many-to-many relationship between Place and Amenity
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             nullable=False, primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """Place class for HBNB project"""
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # Relationship with Review model
    reviews = relationship("Review", backref="place", cascade="delete")

    # Relationship with Amenity model using association table
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def amenities(self):
            """Getter method for amenities"""
            from models import storage
            am_list = []
            for am in storage.all(Amenity).values():
                if am.id in self.amenity_ids:
                    am_list.append(am)
            return am_list

        @amenities.setter
        def amenities(self, value):
            """Setter method for amenities"""
            if isinstance(value, Amenity):
                if value.id not in self.amenity_ids:
                    self.amenity_ids.append(value.id)

        @property
        def reviews(self):
            """Getter method for reviews"""
            from models import storage
            rev_list = []
            for rev in storage.all(Review).values():
                if rev.place_id == self.id:
                    rev_list.append(rev)
            return rev_list
