#!/usr/bin/python3
""" Unittests for file_storage.py """


import os
import unittest
import models
import json
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.user import User


class TestFileStorage_instances(unittest.TestCase):
    """ unittests for instances of filestorage """

    def test_filestoreage_type(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_initialization(self):
        self.assertTrue(type(models.storage), FileStorage)

class TestFileStorage_public_methods(unittest.TestCase):
    """ unittests for methods of File_Storage """

    def all_testing(self):
        self.assertTrue(dict, type(models.storage.all()))

    def new_testing(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def reload_testing(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
