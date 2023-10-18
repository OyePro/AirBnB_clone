#!/usr/bin/python3
"""Unittest for class Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_amenity.py`
    """

    amenity = Amenity()
    amenity.name = "Gym"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel), True)

    def test_if_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)
        self.assertTrue("Gym", self.amenity.name)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.amenity.name), str)
        self.assertNotEqual(type(self.amenity.name), None)

    def test_save(self):
        self.amenity.age = 90
        self.amenity.save()
        self.assertNotEqual(self.amenity.created_at, self.amenity.updated_at)
        self.assertAlmostEqual(90, self.amenity.age)
        amen = Amenity()
        amen.save()
        with open("file.json") as f:
            self.assertIn(("Amenity." + amen.id), f.read())

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.amenity), True)


if __name__ == "__main__":
    unittest.main()
