#!/usr/bin/python3
""" unittesting for review.py """


import os
import unittest
from time import sleep
from models.review import Review
import models


class TestReview_instances(unittest.TestCase):
    """ unittesting for instances for review.py """

    def test_instance_review(self):
        self.assertIn(Review(), models.storage.all().values())


if __name__ == "__main__":
    unittest.main()
