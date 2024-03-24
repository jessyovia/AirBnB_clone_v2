#!/usr/bin/python3
"""This defines unittests for user.py"""


import unittest
from models.user import User
from models.base_model import BaseModel
from sqlalchemy.orm.collections import InstrumentedList


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def test_user_inheritance(self):
        """Test that User class inherits from BaseModel"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_user_attributes(self):
        """Test User class attributes"""
        new_user = User()
        self.assertTrue(hasattr(new_user, 'username'))  # Modified attribute
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertTrue(hasattr(new_user, 'email'))     # Modified attribute
        self.assertTrue(hasattr(new_user, 'full_name')) # Added attribute

    def test_user_places_relationship(self):
        """Test User-Place relationship"""
        new_user = User()
        self.assertIsInstance(new_user.places, InstrumentedList)

    def test_user_messages_relationship(self):
        """Test User-Message relationship"""
        new_user = User()
        self.assertIsInstance(new_user.messages, InstrumentedList)  # Changed from reviews to messages


if __name__ == "__main__":
    unittest.main()
