#!/usr/bin/python3
""" Inherits from parent class 'BaseModel' """


from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits from BaseModel """
    name = ""

    def __str__(self):
        """ Return a string of two characters """
        return self.name[:2].ljust(2)
