#!/usr/bin/python3
""" These are unittests for base_model.py file """


import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from time import sleep


class TestBaseModel_instances(unittest.TestCase):
    """ tests the creation of instances from parent class Base Model """

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
