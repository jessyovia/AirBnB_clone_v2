#!/usr/bin/python3
"""State Module for HBNB project"""

import models
from models.base_model import BaseModel
from models.city import City
from os import getenv

class State(BaseModel):
    """State class representation for database"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
        cities = relationship("City",  backref="state", cascade="all, delete")
    else:
        name = ""
        cities = []

        @property
        def cities(self):
            """Get method for cities"""
            from models import storage
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
