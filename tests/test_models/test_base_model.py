#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import models


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

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

    def test_all_method(self):
        """Test all method returns dictionary"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        """Test new method adds object to __objects"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        self.assertIn("BaseModel." + model.id, storage.all().keys())

    def test_save_method(self):
        """Test save method saves objects to file"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_method(self):
        """Test reload method loads objects from file"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.save()
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel." + model.id, all_objs.keys())

    def test_save_and_reload(self):
        """Test save and reload methods together"""
        storage1 = FileStorage()
        model1 = BaseModel()
        storage1.new(model1)
        storage1.save()

        storage2 = FileStorage()
        storage2.reload()
        all_objs = storage2.all()
        self.assertIn("BaseModel." + model1.id, all_objs.keys())

    def test_delete_method(self):
        """Test delete method deletes object from __objects"""
        storage = FileStorage()
        model = BaseModel()
        storage.new(model)
        storage.delete(model)
        self.assertNotIn("BaseModel." + model.id, storage.all().keys())


if __name__ == '__main__':
    unittest.main()
