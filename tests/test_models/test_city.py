#!/usr/bin/python3
""" unittesting for city """


import os
import unittest
from time import sleep
from models.city import city


class TestCity_instances(unittest.TestCase):
    """ unittesting for instance city """

    def test_instance_city(self):
        self.assertIn(City(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
