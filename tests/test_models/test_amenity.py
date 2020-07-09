#!/usr/bin/python3
"""
    Test Amenity module
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def test_isinstance_Amenity(self):
        """test if the data is an type User"""
        data = Amenity()
        self.assertTrue(isinstance(data, BaseModel))

    def test_name(self):
        """ Test type name """
        data = Amenity()
        name = getattr(data, "name")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
