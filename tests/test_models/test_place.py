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
    myPlace.user_id = "jam-01"
    myPlace.name = "Ibadan"
    myPlace.description = "City of Brown Roof"
    myPlace.number_rooms = 72
    myPlace.number_bathrooms = 40
    myPlace.max_guest = 288
    myPlace.price_by_night = 1500
    myPlace.latitude = 78.5
    myPlace.longitude = 87.6
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

    def test_attr_val(self):
        self.assertEqual(self.myPlace.city_id, "Ibadan-001")
        self.assertEqual(self.myPlace.user_id, "jam-01")
        self.assertEqual(self.myPlace.name, "Ibadan")
        self.assertEqual(self.myPlace.description, "City of Brown Roof")
        self.assertEqual(self.myPlace.number_rooms, 72)
        self.assertEqual(self.myPlace.number_bathrooms, 40)
        self.assertEqual(self.myPlace.max_guest, 288)
        self.assertEqual(self.myPlace.price_by_night, 1500)
        self.assertEqual(self.myPlace.longitude, 87.6)
        self.assertEqual(self.myPlace.latitude, 78.5)
        self.assertEqual(self.myPlace.amenity_ids, [])

    def test_attr_not_None(self):
        self.assertNotEqual(type(self.myPlace.city_id), None)
        self.assertNotEqual(type(self.myPlace.user_id), None)
        self.assertNotEqual(type(self.myPlace.name), None)
        self.assertNotEqual(type(self.myPlace.description), None)
        self.assertNotEqual(type(self.myPlace.number_rooms), None)
        self.assertNotEqual(type(self.myPlace.number_bathrooms), None)
        self.assertNotEqual(type(self.myPlace.max_guest), None)
        self.assertNotEqual(type(self.myPlace.price_by_night), None)
        self.assertNotEqual(type(self.myPlace.longitude), None)
        self.assertNotEqual(type(self.myPlace.latitude), None)
        self.assertNotEqual(type(self.myPlace.amenity_ids), None)

    def test_save(self):
        self.myPlace.age = 90
        self.myPlace.save()
        self.assertNotEqual(self.myPlace.created_at, self.myPlace.updated_at)
        self.assertEqual(self.myPlace.age, 90)
        place = Place()
        place.save()
        with open("file.json", "r") as f:
            self.assertIn(("Place." + place.id), f.read())

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.myPlace), True)


if __name__ == "__main__":
    unittest.main()
