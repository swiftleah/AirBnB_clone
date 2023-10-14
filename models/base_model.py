#!/usr/bin/python3
""" Parent class BaseModel with common attributes for other classes """


import models
import uuid
from datetime import datetime


class BaseModel:
    """ class BaseModel
    assigns UUID to an instance
    keeps track of time when instance is created
    and updated """
    def __init__(self, *args, **kwargs):
        """ Defining attributes above.
        if kwargs not empty: creating instance from
        dictionary. 'created_at' and 'updated_at' converted into
        datetime objects using datetime.strptime().

        if kwargs empty - creating normal instance where 'id',
        'created_at' and 'updated_at' is set. """
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """ Defining time when instance is updated """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ contains all keys/values of __dict__ of instance.
        added key class with class name of specific object.
        created_at and updated_at are converted with ISO format """

        instance_dict = self.__dict__.copy()

        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

    def __str__(self):
        """ string representation of BaseModel """
        return f'({self.__class__.__name__}, {self.id}, {self.__dict__})'
