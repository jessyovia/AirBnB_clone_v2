#!/usr/bin/python3
"""Defines unittests for models/place.py."""


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    def test_instance_creation(self):
        """Test instantiation of Place class."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test attributes of Place class."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))

    def test_relationships(self):
        """Test relationships of Place class."""
        place = Place()
        self.assertTrue(hasattr(place, 'reviews'))
        self.assertTrue(hasattr(place, 'amenities'))

    def test_amenities_property(self):
        """Test amenities property of Place class."""
        place = Place()
        self.assertTrue(hasattr(place, 'amenities'))
        self.assertIsInstance(place.amenities, list)

    def test_reviews_property(self):
        """Test reviews property of Place class."""
        place = Place()
        self.assertTrue(hasattr(place, 'reviews'))
        self.assertIsInstance(place.reviews, list)


if __name__ == '__main__':
    unittest.main()
