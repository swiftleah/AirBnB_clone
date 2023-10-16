#!/usr/bin/python3
""" Inherits from parent class 'BaseModel' 
"""
from models import *
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenity class that inherits from BaseModel 
    """
    name = ""
