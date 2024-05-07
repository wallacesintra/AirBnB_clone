#!/usr/bin/python3
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def test_instance(self):
        """Test creation of City instance."""
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        """Test City attributes."""
        my_city = City()
        my_city.name = "San Francisco"
        my_city.state_id = "CA_001"
        self.assertTrue(hasattr(my_city, 'name'))
        self.assertTrue(hasattr(my_city, 'state_id'))
        self.assertEqual(my_city.name, "San Francisco")
        self.assertEqual(my_city.state_id, "CA_001")


if __name__ == "__main__":
    unittest.main()
