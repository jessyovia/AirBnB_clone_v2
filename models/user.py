#!/usr/bin/python3
"""User Module for HBNB project"""

from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """User class representation for database"""
    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user",
                          cascade="all, delete, delete-orphan")

    reviews = relationship("Review", backref="user",
                           cascade="all, delete, delete-orphan")
