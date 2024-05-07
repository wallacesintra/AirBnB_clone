#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test the base class for all future classes that will store datasets.
    """

    def test_init_from_dict(self):
        """
        Test initialization of BaseModel from dictionary.
        """
        my_model_json = {
            'id': '123456',
            'created_at': '2021-06-29T15:00:00.000000',
            'updated_at': '2021-06-29T15:00:00.000000',
            'name': 'Test model'
        }
        my_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, '123456')
        self.assertEqual(my_model.name, 'Test model')
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_to_dict_returns_correct_key(self):
        """
        Test to_dict method to ensure keys are correctly handled.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        model_dict = my_model.to_dict()
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['name'], 'My First Model')
        self.assertEqual(model_dict['my_number'], 89)


if __name__ == '__main__':
    unittest.main()
