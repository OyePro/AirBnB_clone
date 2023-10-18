#!/usr/bin/python3
"""Unittest for class User"""

import unittest
import os
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_user.py`
    """

    myUser = User()
    myUser.first_name = "Betty"
    myUser.last_name = "John"
    myUser.email = "airbnb@mail.com"
    myUser.password = "root"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.myUser.__class__, BaseModel), True)

    def test_doc(self):
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        self.assertTrue('email' in self.myUser.__dict__)
        self.assertTrue('id' in self.myUser.__dict__)
        self.assertTrue('created_at' in self.myUser.__dict__)
        self.assertTrue('updated_at' in self.myUser.__dict__)
        self.assertTrue('password' in self.myUser.__dict__)
        self.assertTrue('first_name' in self.myUser.__dict__)
        self.assertTrue('last_name' in self.myUser.__dict__)

    def test_attributes(self):
        self.assertTrue("Betty", self.myUser.first_name)
        self.assertTrue("root", self.myUser.password)
        self.assertTrue("airbnb@mail.com", self.myUser.email)
        self.assertTrue("John", self.myUser.last_name)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.myUser.email), str)
        self.assertEqual(type(self.myUser.password), str)
        self.assertEqual(type(self.myUser.first_name), str)
        self.assertEqual(type(self.myUser.last_name), str)

    def test_save(self):
        self.myUser.age = 90
        self.myUser.state = "Oyo"
        self.myUser.save()
        self.assertNotEqual(self.myUser.created_at, self.myUser.updated_at)
        self.assertEqual(self.myUser.age, 90)
        self.assertEqual(self.myUser.state, "Oyo")
        user = User()
        user.save()
        with open("file.json") as f:
            self.assertIn(("User." + user.id), f.read())

    def test_attr_not_None(self):
        self.assertNotEqual(type(self.myUser.email), None)
        self.assertNotEqual(type(self.myUser.password), None)
        self.assertNotEqual(type(self.myUser.first_name), None)
        self.assertNotEqual(type(self.myUser.last_name), None)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.myUser), True)


if __name__ == "__main__":
    unittest.main()
