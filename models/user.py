#!/usr/bin/python3
""" Inherits from parent clas 'BaseModel' """


from models.base_model import BaseModel


class User(BaseModel):
    """ User class that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
