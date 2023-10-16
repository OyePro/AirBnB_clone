#!/usr/bin/python3
"""Defining the class BaseModel"""
from uuid import uuid4
from datetime import datetime as dtime
import models as models


class BaseModel:
    """Class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initializing BaseModel"""

        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    pass
                elif k == "created_at":
                    self.__dict__[k] = dtime.strptime(v, time_format)
                elif k == "updated_at":
                    self.__dict__[k] = dtime.strptime(v, time_format)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = dtime.now()
            self.updated_at = dtime.now()
            models.storage.new(self)

    def __str__(self):
        """printing the class name, id and instances of BaseModel"""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """update the current date time"""
        self.updated_at = dtime.now()
        models.storage.save()

    def to_dict(self):
        """
           function to return a dictionary containing all
           keys and value of instance
        """
        return_dict = {}
        return_dict["__class__"] = str(self.__class__.__name__)
        for keys, values in self.__dict__.items():
            if keys in ["created_at", "updated_at"]:
                return_dict[keys] = values.isoformat()
            else:
                return_dict[keys] = values
        return return_dict
