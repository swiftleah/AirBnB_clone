#!/usr/bin/python3
""" unittesting for place.py """


import os
import unittest
from time import sleep
from models.place import Place


class TestPlace_instances(unittest.TestCase):
    """ unittesting for place """

    def test_instance_place(self):
        self.assertIn(Place(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
