#!/usr/bin/python3
""" File Storage class that will serialize instances to JSON file
and deserialize to instances """


import json
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State


class FileStorage:
    """ class File Storage:
    private class attributes file_path (path to
    JSON file ) & objects (dict - stores objects by
    class name and id ) """
    __file_path = "file.json"
    __objects = {}

    def get(self, cls, id):
        """ Retrieves an object based on class name and id """
        key = "{}.{}".format(cls, id)
        if key in self.__objects:
            return self.__objects[key]
        return None

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

    def delete(self, cls, id):
        """ Deletes an object based on class name and id """
        key = "{}.{}".format(cls, id)
        if key in self.__objects:
            del self.__objects[key]
            self.save()
        else:
            return False

    def reload(self):
        """ deserializes JSON file to __objects """
        try:
            with open(self.__file_path) as f:
                data = json.load(f)
                for key, obj_data in data.items():
                    class_name = obj_data["__class__"]
                    if class_name in self.classes():
                        obj = self.classes()[class_name](**obj_data)
                        self.__objects[key] = obj
        except FileNotFoundError:
            return

    def classes(self):
        """ Returns a dict of available classes for serialization"""
        return {
                "BaseModel": BaseModel,
                "user": User,
                "Place": Place,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Review": Review
                }
