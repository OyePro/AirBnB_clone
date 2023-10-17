#!/usr/bin/python3
"""Unittest for class State"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_state.py`
    """

    state = State()
    state.name = "OYO"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    def test_if_doc(self):
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)
        self.assertTrue("OYO", self.state.name)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.state.name), str)

    def test_save(self):
        self.state.age = 90
        self.state.height = 1.75
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)
        self.assertAlmostEqual(90, self.state.age)
        self.assertAlmostEqual(1.75, self.state.height)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.state), True)


if __name__ == "__main__":
    unittest.main()
