#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class"""

    def test_instance_creation(self):
        """Tests creation of an Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Tests the attributes of Amenity"""
        amenity = Amenity()
        amenity.name = "Pool"
        self.assertEqual(amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
