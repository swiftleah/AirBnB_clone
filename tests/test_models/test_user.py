#!/usr/bin/python3
""" unittests for user.py """


import os
import models
import unittest
from time import sleep
from datetime import datetime
from models.user import User


class TestUser_instances(unittest.TestCase):
    """ Unittesting for instances of User class based off of BaseModel """

    def test_different_ids(self):
        Person1 = User()
        sleep(0.02)
        Person2 = User()
        self.assertNotEqual(Person1.id, Person2.id)

    def test_different_creation_times(self):
        Person1 = User()
        sleep(0.02)
        Person2 = User()
        self.assertLess(Person1.created_at, Person2.created_at)

    def test_different_updated_times(self):
        Person1 = User()
        sleep(0.02)
        Person2 = User()
        self.assertLess(Person1.updated_at, Person2.updated_at)

    def test_email_type(self):
        self.assertEqual(str, type(User.email))

    def test_password_type(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_type(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_type(self):
        self.assertEqual(str, type(User.last_name))


class TestUser_save(unittest.TestCase):
    """ unittesting for save method """

    def test_save(self):
        User1 = User()
        sleep(0.05)
        first_update = User1.updated_at
        User1.save()
        self.assertLess(first_update, User1.updated_at)

    def test_save_to_file(self):
        User1 = User()
        User1.save()
        User1id = "User." + User1.id
        with open("file.json", "r") as f:
            self.assertIn(User1id, f.read())


class TestUser_to_dict(unittest.TestCase):
    """ unittesting to_dict for User """

    def test_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_dict_attributes(self):
        User1 = User()
        User1.name = "Leah"
        User1.my_number = 99
        self.assertEqual("Leah", User1.name)
        self.assertIn("my_number", User1.to_dict())


if __name__ == "__main__":
    unittest.main()
