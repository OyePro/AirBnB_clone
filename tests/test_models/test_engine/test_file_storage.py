#!/usr/bin/python3
"""Unittest for class FileStorage"""

import unittest
import json
import os
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Run with
    `python3 -m unittest -v tests/test_models/test_engine/test_file_storage.py`
    """
    user = User()

    @classmethod
    def setUpClass(cls):
        cls.rev = Review()
        cls.rev.place_id = "Ibadan-001"
        cls.rev.user_id = "123-456-789"
        cls.rev.text = "AirBnB"

    @classmethod
    def teardown(cls):
        del cls.rev

    def teardown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """
        Tests method: all (returns dictionary <class>.<id> : <obj instance>)
        """
        storage = FileStorage()
        instances_dict = storage.all()
        self.assertIsNotNone(instances_dict)
        self.assertEqual(type(instances_dict), dict)
        self.assertIs(instances_dict, storage._FileStorage__objects)

    def test_new(self):
        """
        Tests method: new (saves new object into dictionary)
        """
        m_storage = FileStorage()
        instances_dict = m_storage.all()
        newUser = User()
        newUser.id = 1234980
        newUser.name = "AirBnB"
        m_storage.new(newUser)
        key = newUser.__class__.__name__ + "." + str(newUser.id)
        self.assertIsNotNone(instances_dict[key])

    def test_reload(self):
        """
        Tests method: reload (reloads objects from string file)
        """
        with self.assertRaises(TypeError):
            storage.reload(None)
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
        storage.save()
        storage.reload()
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            self.assertTrue(isinstance(obj, BaseModel))

    def test_save(self):
        with self.assertRaises(TypeError):
            storage.save(None)
        newUser = User()
        storage.save()
        save = ""
        with open("file.json") as f:
            save = f.read()
        self.assertIn(("User." + newUser.id), save)


if __name__ == "__main__":
    unittest.main()
