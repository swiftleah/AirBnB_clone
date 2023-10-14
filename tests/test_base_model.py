#!/usr/bin/python3
""" These are unittests for base_model.py file """


import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel_instances(unittest.TestCase):
    """ tests the creation of instances from parent class Base Model """

    def test_no_arg_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))
