#!/usr/bin/python3
"""Defines unittests for state.py"""


import unittest
from models.state import State
from models.city import City


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_state_name_type(self):
        """Test type of State name attribute"""
        new_state = State(name="Test State")
        self.assertIsInstance(new_state.name, str)

    def test_state_cities_property(self):
        """Test the cities property of the State class"""
        new_state = State()
        self.assertTrue(hasattr(new_state, 'cities'))
        self.assertEqual(type(new_state.cities), list)

    def test_state_cities_property_empty(self):
        """Test the cities property returns an empty list initially"""
        new_state = State()
        self.assertEqual(len(new_state.cities), 0)

    def test_state_cities_property_with_cities(self):
        """Test the cities property returns cities associated with the state"""
        new_state = State()
        new_city1 = City(name="City 1", state_id=new_state.id)
        new_city2 = City(name="City 2", state_id=new_state.id)
        new_state.save()
        new_city1.save()
        new_city2.save()
        self.assertIn(new_city1, new_state.cities)
        self.assertIn(new_city2, new_state.cities)


if __name__ == "__main__":
    unittest.main()

