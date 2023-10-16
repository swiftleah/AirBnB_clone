#!/usr/bin/python3
""" unittesting for State.py """


import unittest
import os
import models
from time import sleep
from models.state import State

class testState_instances(unittest.TestCase):
    """ unittesting for instances of State.py """

    def test_instance_state(self):
        self.assertIn(State(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
