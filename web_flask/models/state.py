#!/usr/bin/python3
"""
State module.
"""
from models.base_model import BaseModel
from models.city import City
from models import storage

class State(BaseModel):
    """State class."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes State object."""
        super().__init__(*args, **kwargs)

    if storage_type != "db":
        @property
        def cities(self):
            """Getter method that returns a list of City instances with
            state_id equals to the current State.id."""
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list

