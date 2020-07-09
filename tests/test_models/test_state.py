#!/usr/bin/python3
"""
    Test State module
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def test_isinstance_State(self):
        """test if the data is an type User"""
        data = State()
        self.assertTrue(isinstance(data, BaseModel))

    def test_name(self):
        """ Test type name """
        data = State()
        name = getattr(data, "name")
        self.assertIsInstance(name, str)


if __name__ == '__main__':
    unittest.main()
