#!/usr/bin/python3
"""
    Test City module
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):

    def test_isinstance_City(self):
        """test if the data is an type User"""
        data = City()
        self.assertTrue(isinstance(data, BaseModel))

    def test_name(self):
        """ Test type name """
        data = City()
        name = getattr(data, "name")
        self.assertIsInstance(name, str)

    def test_state_id(self):
        """ Test type name """
        data = City()
        name = getattr(data, "state_id")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
