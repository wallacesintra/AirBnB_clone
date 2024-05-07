#!/usr/bin/python3
"""
Module for testing the User class
"""
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test methods."""
        self.user_instance = User()
        self.user_instance.first_name = "John"
        self.user_instance.last_name = "Doe"
        self.user_instance.email = "john@example.com"
        self.user_instance.password = "password"

    def test_instance_creation(self):
        """Test creation of user instance."""
        self.assertIsInstance(self.user_instance, User)

    def test_inheritance(self):
        """Test if User correctly inherits from BaseModel."""
        self.assertIsInstance(self.user_instance, User)

    def test_attributes(self):
        """Test the attributes of User."""
        self.assertTrue(hasattr(self.user_instance, "first_name"))
        self.assertTrue(hasattr(self.user_instance, "last_name"))
        self.assertTrue(hasattr(self.user_instance, "email"))
        self.assertTrue(hasattr(self.user_instance, "password"))
        self.assertEqual(self.user_instance.first_name, "John")
        self.assertEqual(self.user_instance.last_name, "Doe")
        self.assertEqual(self.user_instance.email, "john@example.com")
        self.assertEqual(self.user_instance.password, "password")


if __name__ == '__main__':
    unittest.main()
