#!/usr/bin/python3

""" Class file storage """
import json
from os import path
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User


class FileStorage:
    """ serializes / deserializes an instances:
     file path :: JSON file path (string)
     objects :: store all objects (dictionary) """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def path(cls):
        """ return path of JSON file """
        return cls.__file_path

    def all(self):
        """ return dictionary of objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.__dict__.get("id")
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        d = {}
        for key, value in FileStorage.__objects.items():
            d[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as file:
            file.write(json.dumps(d))

    def reload(self):
        """  deserializes the JSON file to __objects """
        if path.exists(FileStorage.__file_path) and path.getsize(
                FileStorage.__file_path):
            with open(FileStorage.__file_path) as file:
                for key, value in (json.load(file)).items():
                    obj = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = obj
