#!/usr/bin/python3
"""Unittest for class City"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_city.py`
    """

    myCity = City()
    myCity.name = "Ibadan"
    myCity.state_id = "Ibadan-001"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.myCity.__class__, BaseModel), True)

    def test_if_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.myCity.__dict__)
        self.assertTrue('created_at' in self.myCity.__dict__)
        self.assertTrue('updated_at' in self.myCity.__dict__)
        self.assertTrue('state_id' in self.myCity.__dict__)
        self.assertTrue('name' in self.myCity.__dict__)
        self.assertTrue("Ibadan", self.myCity.name)
        self.assertTrue("Ibadan-001", self.myCity.state_id)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.myCity.name), str)
        self.assertEqual(type(self.myCity.state_id), str)

    def test_save(self):
        self.myCity.age = 90
        self.myCity.save()
        self.assertNotEqual(self.myCity.created_at, self.myCity.updated_at)
        self.assertAlmostEqual(self.myCity.age, 90)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.myCity), True)


if __name__ == "__main__":
    unittest.main()
