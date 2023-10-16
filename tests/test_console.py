#!/usr/bin/python3
""" unittests for console.py """


import os
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from models.engine.file_storage import FileStorage
import sys
from console import HBNBCommand


class TestHBNBCommand_prompting(unittest.TestCase):
    """ Unittests for HBNB Command shell """

    def test_prompt_str(self):
        self.assertTrue("(hbnb) ", HBNBCommand.prompt)


class TestHBNBCommand_help(unittest.TestCase):
    """ unittesting for command help on shell """

    def test_help_EOF(self):
        exitmsg = "exits program when input is 'EOF'"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(exitmsg, output.getvalue().strip())


class TestHBNBCommand_exit(unittest.TestCase):
    """ unittesting for exit command in shell """

    def test_quit_command(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_command(self):
        """ seeing if input 'EOF' causes shell to quit """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))


class TestHBNBCommand_create(unittest.TestCase):
    """ unittesting 'create' command which creates instance based
        off parent class BaseModel """

    def test_create_no_class_name_given(self):
        errormsg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(errormsg, output.getvalue().strip())


if __name__ == "__main__":
    unittest.main()
