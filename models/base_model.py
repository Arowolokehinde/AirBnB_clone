#!/usr/bin/python3
from datetime import datetime
import uuid
"""This imports the datetime and the uuid module"""


class BaseModel():
    """This is the base model class"""
    def __init__(self, created_at=None, id=None, updated_at=None):
        """The public instance attribute of the class that contains
        the id, created_at and updated_at"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """This method updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This method returns a dictionary containing all
        keys/values of __dict__ of the instance """
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__

        return self.__dict__

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
