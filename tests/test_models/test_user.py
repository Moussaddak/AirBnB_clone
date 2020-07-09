#!/usr/bin/python3
"""
    Test user module
"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def test_isinstance_User(self):
        """test if the data is an type User"""
        data = User()
        self.assertTrue(isinstance(data, User))


if __name__ == '__main__':
    unittest.main()
