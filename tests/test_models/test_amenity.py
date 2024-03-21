#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""


import os
import unittest
from datetime import datetime
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up test environment"""
        # Remove any existing JSON file before each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test environment"""
        # Remove the created JSON file after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test creation of Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_id_is_string(self):
        """Test id attribute is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)

    def test_created_at_is_datetime(self):
        """Test created_at attribute is a datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at attribute is a datetime"""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_save_method(self):
        """Test save method updates updated_at"""
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns dictionary"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)

    def test_to_dict_contains_classname(self):
        """Test to_dict method contains __class__ key with class name"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_to_dict_datetime_format(self):
        """Test to_dict method returns correct datetime format"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity.created_at.isoformat(), amenity_dict["created_at"])
        self.assertEqual(amenity.updated_at.isoformat(), amenity_dict["updated_at"])


if __name__ == '__main__':
    unittest.main()
