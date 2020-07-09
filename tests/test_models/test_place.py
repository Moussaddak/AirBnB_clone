#!/usr/bin/python3
"""
    Test Place module
"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def test_isinstance_Place(self):
        """test if the data is an type User"""
        data = Place()
        self.assertTrue(isinstance(data, BaseModel))

    def test_city_id(self):
        """ Test type city_id """
        data = Place()
        city_id = getattr(data, "city_id")
        self.assertIsInstance(city_id, str)

    def test_user_id(self):
        """ Test type user_id """
        data = Place()
        user_id = getattr(data, "user_id")
        self.assertIsInstance(user_id, str)

    def test_name(self):
        """ Test type name """
        data = Place()
        name = getattr(data, "name")
        self.assertIsInstance(name, str)

    def test_description(self):
        """ Test type description """
        data = Place()
        description = getattr(data, "description")
        self.assertIsInstance(description, str)

    def test_number_rooms(self):
        """ Test type number_rooms """
        data = Place()
        number_rooms = getattr(data, "number_rooms")
        self.assertIsInstance(number_rooms, int)

    def test_number_bathrooms(self):
        """ Test type number_bathrooms """
        data = Place()
        number_bathrooms = getattr(data, "number_bathrooms")
        self.assertIsInstance(number_bathrooms, int)

    def test_max_guest(self):
        """ Test type max_guest """
        data = Place()
        max_guest = getattr(data, "max_guest")
        self.assertIsInstance(max_guest, int)

    def test_price_by_night(self):
        """ Test type price_by_night """
        data = Place()
        price_by_night = getattr(data, "price_by_night")
        self.assertIsInstance(price_by_night, int)

    def test_latitude(self):
        """ Test type latitude """
        data = Place()
        latitude = getattr(data, "latitude")
        self.assertIsInstance(latitude, float)

    def test_longitude(self):
        """ Test type longitude """
        data = Place()
        longitude = getattr(data, "longitude")
        self.assertIsInstance(longitude, float)

    def test_amenity_ids(self):
        """ Test type amenity_ids """
        data = Place()
        amenity_ids = getattr(data, "amenity_ids")
        self.assertIsInstance(amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
