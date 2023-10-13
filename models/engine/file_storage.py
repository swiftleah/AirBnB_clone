#!/usr/bin/python3
""" File Storage class that will serialize instances to JSON file
and deserialize to instances """


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ class File Storage:
    private class attributes file_path (path to
    JSON file ) & objects (dict - stores objects by
    class name and id ) """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary of private attribute objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file (__file_path) """
        data = {}
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()
        with open(self.__file_path, "w", encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        try:
            with open(self.__file_path) as f:
                data = json.load(f)
                for objects in data.values():
                    class_name = objects["__class__"]
                    del objects["__class__"]
                    self.new(eval(class_name)(**objects))
        except FileNotFoundError:
            return

    def classes(self):
        """ Returns a dict of available classes for serialization"""
        return {
                "BaseModel": BaseModel,
                "user": User
                }
