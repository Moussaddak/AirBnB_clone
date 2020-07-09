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

    def test_email(self):
        """ Test type name """
        data = User()
        name = getattr(data, "email")
        self.assertIsInstance(name, str)

    def test_first_name(self):
        """ Test type name """
        data = User()
        name = getattr(data, "first_name")
        self.assertIsInstance(name, str)

    def test_last_name(self):
        """ Test type last_name """
        data = User()
        name = getattr(data, "last_name")
        self.assertIsInstance(name, str)

    def test_password(self):
        """ Test type password """
        data = User()
        name = getattr(data, "password")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
