#!/usr/bin/python3
""" unittests for amenity.py """


import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instance(unittest.TestCase):
    """ unittesting for instances of amenity """

    def test_amenity_type(self):
        self.assertIn(Amenity(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
