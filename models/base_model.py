#!/usr/bin/python3
""" BaseModel Class Module """
import uuid
from datetime import datetime


class BaseModel:
    """ BaseModel Class """
    def __init__(self):
        """ Initialization Method """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """ Update the attribute to the current datetime Method """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Get a dict of the BaseModel Method """
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return (my_dict)

    def __str__(self):
        """ Get the string representation of the BaseModel Method """
        name = self.__class__.__name__
        return (f"[{name}] ({self.id}) {self.__dict__}")
