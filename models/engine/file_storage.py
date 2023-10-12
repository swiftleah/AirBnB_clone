#!/usr/bin/python3
""" File Storage class that will serialize instances to JSON file and deserialize to instances """


import json


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
