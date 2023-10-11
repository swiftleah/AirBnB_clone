#!/usr/bin/python3
""" Parent class BaseModel with common attributes for other classes """


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
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def save(self):
        """ Defining time when instance is updated """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ contains all keys/values of __dict__ of instance.
        added key class with class name of specific object.
        created_at and updated_at are converted with ISO format """
        class_name = self.__class__.__name__
        instance_dict = self.__dict__
        format_created_at = self.created_at.isoformat()
        format_updated_at = self.updated_at.isoformat()

        instance_dict['__class__'] = class_name
        instance_dict['created_at'] = format_created_at
        instance_dict['updated_at'] = format_updated_at
        return instance_dict


    def __str__(self):
        """ string representation of BaseModel """
        class_name = self.__class__.__name__
        return f'({class_name}, {self.id}, {self.__dict__})'
