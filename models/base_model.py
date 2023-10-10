#!/usr/bin/python3
""" Parent class BaseModel with common attributes for other classes """


import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel
    assigns UUID to an instance
    keeps track of time when instance is created
    and updated """
    def __init__(self):
        """ Defining attributes above """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def time_update(self):
        """ Defining time when instance is updated """
        self.updated_at = datetime.now()
