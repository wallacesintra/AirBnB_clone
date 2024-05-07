#!/usr/bin/python3
"""
Module for testing the State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up test methods."""
        self.state_instance = State()
        self.state_instance.name = "California"

    def test_instance_creation(self):
        """Test creation of state instance."""
        self.assertIsInstance(self.state_instance, State)

    def test_inheritance(self):
        """Test if State correctly inherits from BaseModel."""
        self.assertIsInstance(self.state_instance, State)

    def test_attributes(self):
        """Test the attributes of State."""
        self.assertTrue(hasattr(self.state_instance, "name"))
        self.assertEqual(self.state_instance.name, "California")


if __name__ == '__main__':
    unittest.main()
