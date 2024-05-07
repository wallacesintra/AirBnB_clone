#!/usr/bin/python3
"""
Module for testing the FileStorage class
"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.storage = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Clean up after the doc test"""
        del cls.storage
        try:
            os.remove("file.json")
        except Exception:
            pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_all_returns_dict(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test that new adds an object to the storage dictionary."""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test that save properly saves objects to file.json."""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            obj_dict = json.load(f)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, obj_dict)

    def test_reload(self):
        """Test that reload correctly deserializes the JSON file to objects."""
        obj = BaseModel()
        obj_id = obj.id
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj_id}"
        self.assertIn(key, self.storage.all())

    def test_reload_empty(self):
        """Test that reload handles no file gracefully."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage.reload()
        self.assertIsInstance(self.storage.all(), dict)
        self.assertEqual(len(self.storage.all()), 0)

    def test_storage_instance(self):
        """Test storage type and the storage object is correctly set."""
        self.assertTrue(isinstance(self.storage, FileStorage))


if __name__ == '__main__':
    unittest.main()
