#!/usr/bin/python3
"""BaseModel class"""


import uuid
from datetime import datetime


class BaseModel():
    """ Defines all common attributes/methods for other classes """
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from .__init__ import storage
            storage.new(self)

    def __str__(self):
        """ String representation """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime """
        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
