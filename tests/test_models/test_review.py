#!/usr/bin/python3
"""
    Test Review module
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_isinstance_Review(self):
        """test if the data is an type User"""
        data = Review()
        self.assertTrue(isinstance(data, BaseModel))

    def test_city_id(self):
        """ Test type city_id """
        data = Review()
        city_id = getattr(data, "city_id")
        self.assertIsInstance(city_id, str)

    def test_user_id(self):
        """ Test type user_id """
        data = Review()
        user_id = getattr(data, "user_id")
        self.assertIsInstance(user_id, str)

    def test_text(self):
        """ Test type text """
        data = Review()
        text = getattr(data, "text")
        self.assertIsInstance(text, str)


if __name__ == '__main__':
    unittest.main()
