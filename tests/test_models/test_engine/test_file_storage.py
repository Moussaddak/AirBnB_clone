#!/usr/bin/python3
"""
    TestFileStorage module
"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    def test_isinstance_FileStorage(self):
        """test if the data is an type FileStorage"""
        data1 = FileStorage()
        data2 = storage.all()

        self.assertTrue(isinstance(data1, FileStorage))
        self.assertTrue(isinstance(data2, FileStorage))


if __name__ == '__main__':
    unittest.main()
