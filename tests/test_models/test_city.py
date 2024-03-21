#!/usr/bin/python3
"""Unit tests for City class"""


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City class"""

    def test_name_not_nullable(self):
        """Test 'name' attribute is not nullable"""
        city = City(name="Test City")
        self.assertIsNotNone(city.name)

    def test_name_type(self):
        """Test type of the 'name' attribute"""
        city = City(name="Test City")
        self.assertIsInstance(city.name, str)

    def test_state_id_not_nullable(self):
        """Test 'state_id' attribute is not nullable"""
        city = City(state_id="test_state_id")
        self.assertIsNotNone(city.state_id)

    def test_state_id_type(self):
        """Test type of the 'state_id' attribute"""
        city = City(state_id="test_state_id")
        self.assertIsInstance(city.state_id, str)


if __name__ == '__main__':
    unittest.main()
