#!/usr/bin/python3
"""Creating the class FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
        """class FileStorage"""

        __file_path = "file.json"
        __objects = {}
        classDict = {"BaseModel": BaseModel, "User": User, "State": State,
                     "City": City, "Amenity": Amenity, "Place": Place,
                     "Review": Review}

        def all(self):
            """
            a method that returns the dictionary __objects
            """

            return self.__objects

        def new(self, obj):
            """
            a method that sets the key and value of dictionary __objects
            """

            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

        def save(self):
            """
            a method to serialize dictionary __objects to __file_path
            """

            se_dict = {}
            for key, clname in self.__objects.items():
                se_dict[key] = clname.to_dict()

            with open(self.__file_path, 'w') as to_serial:
                str_serial = json.dumps(se_dict)
                to_serial.write(str_serial)

        def reload(self):
            """
            a method to deserialize file contents to __objects
            """
            try:
                with open(self.__file_path) as to_deser:
                    deser = json.load(to_deser)

                dict_deser = {}
                for k, v in deser.items():
                    key = k.split(".")[0]
                    dict_deser[k] = self.classDict[v["__class__"]](**v)

                self.__objects = dict_deser
            except FileNotFoundError:
                pass
