#!/usr/bin/python3
""" unittests for console.py """


import os
import unittest
from models import storage
from models.engine.file_storage import FileStorage
import sys
from console import HBNBCommand


class TestHBNBCommand_prompting(unittest.TestCase):
    """ Unittests for HBNB Command shell """

    def test_prompt_str(self):
        self.assertTrue("(hbnb) ", HBNBCommand.prompt)
