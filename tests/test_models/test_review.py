#!/usr/bin/python3
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_instance(self):
        """Test creation of Review instance."""
        my_review = Review()
        self.assertIsInstance(my_review, Review)

    def test_attributes(self):
        """Test attributes for Review."""
        my_review = Review()
        my_review.text = "Great place, had a lovely time!"
        my_review.place_id = "Place_001"
        my_review.user_id = "User_123"
        self.assertTrue(hasattr(my_review, 'text'))
        self.assertTrue(hasattr(my_review, 'place_id'))
        self.assertTrue(hasattr(my_review, 'user_id'))
        self.assertEqual(my_review.text, "Great place, had a lovely time!")
        self.assertEqual(my_review.place_id, "Place_001")
        self.assertEqual(my_review.user_id, "User_123")


if __name__ == "__main__":
    unittest.main()
