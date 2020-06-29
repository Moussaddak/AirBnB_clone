#!/usr/bin/python3
""" BaseModel Class prototype """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel of all other classes """

    def __init__(self, *args, **kwargs):
        """ initialization of instance attribute
        id : unique id number of instance
        created_at : when an instance is created
        updated_at : when the last modification of an instance
        """
        if kwargs:
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value,
                            "%Y-%m-%dT%H:%M:%S.%f"))
                elif not key == '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        magic method
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of the instance"""
        d = self.__dict__
        d.update(__class__=self.__class__.__name__)
        d.update(created_at=self.created_at.isoformat())
        d.update(updated_at=self.updated_at.isoformat())
        return d
