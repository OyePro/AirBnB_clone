#!/usr/bin/python3
"""Unittest for class Place"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_place.py`
    """

    myPlace = Place()
    myPlace.city_id = "Ibadan-001"
    myPlace.user_id = "234-567-890"
    myPlace.name = "Ibadan"
    myPlace.description = "City of Brown Roof"
    myPlace.number_rooms = 0
    myPlace.number_bathrooms = 0
    myPlace.max_guest = 0
    myPlace.price_by_night = 0
    myPlace.latitude = 0.0
    myPlace.longitude = 0.0
    myPlace.amenity_ids = []

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.myPlace.__class__, BaseModel), True)

    def test_if_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.myPlace.__dict__)
        self.assertTrue('created_at' in self.myPlace.__dict__)
        self.assertTrue('updated_at' in self.myPlace.__dict__)
        self.assertTrue('city_id' in self.myPlace.__dict__)
        self.assertTrue('user_id' in self.myPlace.__dict__)
        self.assertTrue('name' in self.myPlace.__dict__)
        self.assertTrue('description' in self.myPlace.__dict__)
        self.assertTrue('number_rooms' in self.myPlace.__dict__)
        self.assertTrue('number_bathrooms' in self.myPlace.__dict__)
        self.assertTrue('max_guest' in self.myPlace.__dict__)
        self.assertTrue('price_by_night' in self.myPlace.__dict__)
        self.assertTrue('latitude' in self.myPlace.__dict__)
        self.assertTrue('longitude' in self.myPlace.__dict__)
        self.assertTrue('amenity_ids' in self.myPlace.__dict__)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.myPlace.city_id), str)
        self.assertEqual(type(self.myPlace.user_id), str)
        self.assertEqual(type(self.myPlace.name), str)
        self.assertEqual(type(self.myPlace.description), str)
        self.assertEqual(type(self.myPlace.number_rooms), int)
        self.assertEqual(type(self.myPlace.number_bathrooms), int)
        self.assertEqual(type(self.myPlace.max_guest), int)
        self.assertEqual(type(self.myPlace.price_by_night), int)
        self.assertEqual(type(self.myPlace.latitude), float)
        self.assertEqual(type(self.myPlace.longitude), float)
        self.assertEqual(type(self.myPlace.amenity_ids), list)

    def test_save(self):
        self.myPlace.save()
        self.assertNotEqual(self.myPlace.created_at, self.myPlace.updated_at)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.myPlace), True)


if __name__ == "__main__":
    unittest.main()
