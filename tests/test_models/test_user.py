#!/usr/bin/python3
"""
    Test user module
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def test_isinstance_User(self):
        """test if the data is an type User"""
        data = User()
        self.assertTrue(isinstance(data, BaseModel))

    def test_attributes_User(self):
        """ Test user attributes """

        data = User()
        self.assertTrue("email" in data.__dir__())
        self.assertTrue("first_name" in data.__dir__())
        self.assertTrue("last_name" in data.__dir__())
        self.assertTrue("password" in data.__dir__())


if __name__ == '__main__':
    unittest.main()
