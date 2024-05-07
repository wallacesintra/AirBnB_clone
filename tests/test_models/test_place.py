#!/usr/bin/python3
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def test_instance(self):
        """Test creation of Place instance."""
        my_place = Place()
        self.assertIsInstance(my_place, Place)

    def test_attributes(self):
        """Test attributes for Place."""
        my_place = Place()
        my_place.name = "My Little House"
        my_place.description = "A cozy cottage in the woods."
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guest = 4
        my_place.price_by_night = 120
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        self.assertEqual(my_place.name, "My Little House")
        self.assertEqual(my_place.description, "A cozy cottage in the woods.")
        self.assertEqual(my_place.number_rooms, 2)
        self.assertEqual(my_place.number_bathrooms, 1)
        self.assertEqual(my_place.max_guest, 4)
        self.assertEqual(my_place.price_by_night, 120)
        self.assertEqual(my_place.latitude, 37.7749)
        self.assertEqual(my_place.longitude, -122.4194)


if __name__ == "__main__":
    unittest.main()
