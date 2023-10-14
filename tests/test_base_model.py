#!/usr/bin/python3
""" These are unittests for base_model.py file """


import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from time import sleep


class TestBaseModel_instances(unittest.TestCase):
    """ tests the creation of instances from parent class BaseModel """

    def test_no_arg_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_models_created_different_times(self):
        Model1 = BaseModel()
        sleep(0.1)
        Model2 = BaseModel()
        self.assertNotEqual(Model1.created_at, Model2.created_at)

    def test_two_models_updated_different_times(self):
        Model1 = BaseModel()
        sleep(0.1)
        Model2 = BaseModel()
        self.assertNotEqual(Model1.updated_at, Model2.updated_at)

class TestBaseModel_save(unittest.TestCase):
    """ tests for 'save' in parent class BaseModel """

    def test_save(self):
        Model = BaseModel()
        sleep(0.1)
        first_updated_at = Model.updated_at
        Model.save()
        self.assertLess(first_updated_at, Model.updated_at)

class TestBaseModel_to_dict(unittest.TestCase):
    """ tests for 'to_dict' in parent class BaseModel """

    def test_type_dict(self):
        M = BaseModel()
        self.assertEqual(dict, type(M.to_dict()))

    def test_dict_datetimes_are_strings(self):
        M = BaseModel()

        self.assertEqual(str, type(M.to_dict()["created_at"]))
        self.assertEqual(str, type(M.to_dict()["updated_at"]))

if __name__ == "__main__":
    unittest.main()
