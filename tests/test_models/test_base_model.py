#!/usr/bin/python3
"""Defines unittests for models/base_model.py"""


import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        """Test creation of BaseModel instance"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_is_string(self):
        """Test id attribute is a string"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_created_at_is_datetime(self):
        """Test created_at attribute is a datetime"""
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test updated_at attribute is a datetime"""
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_save_method(self):
        """Test save method updates updated_at"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method returns dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_classname(self):
        """Test to_dict method contains __class__ key with class name"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIn("__class__", model_dict)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_to_dict_datetime_format(self):
        """Test to_dict method returns correct datetime format"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model.created_at.isoformat(),
                         model_dict["created_at"])
        self.assertEqual(model.updated_at.isoformat(),
                         model_dict["updated_at"])

    def test_to_dict_method_excludes_sa_instance_state(self):
        """Test to_dict method excludes _sa_instance_state key"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertNotIn("_sa_instance_state", model_dict)

    def test_to_dict_method_includes_custom_attributes(self):
        """Test to_dict method includes custom attributes"""
        model = BaseModel()
        model.name = "Test"
        model.number = 123
        model_dict = model.to_dict()
        self.assertIn("name", model_dict)
        self.assertIn("number", model_dict)
        self.assertEqual(model_dict["name"], "Test")
        self.assertEqual(model_dict["number"], 123)


if __name__ == '__main__':
    unittest.main()

