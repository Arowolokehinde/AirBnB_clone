#!/usr/bin/python3
from datetime import datetime
import uuid
"""This imports the datetime and the uuid module"""


class BaseModel:
    """This is the base model class"""
    def __init__(self, created_at=None, id=None, updated_at=None):
        """The public instance attribute of the class that contains
        the id, created_at and updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = self.created_at

    def save(self):
        """This method updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ This method returns a dictionary containing all
        keys/values of __dict__ of the instance """

        dict_cpy = self.__dict__.copy()
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()
        dict_cpy['__class__'] = self.__class__.__name__

        return dict_cpy

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
