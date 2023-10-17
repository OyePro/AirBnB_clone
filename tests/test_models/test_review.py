#!/usr/bin/python3
"""Unittest for class review"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Run with `python3 -m unittest -v tests/test_models/test_review.py`
    """
    rev = Review()
    rev.place_id = "Ibadan-001"
    rev.user_id = "123-879-098"
    rev.text = "AirBnB"

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)

    def test_if_doc(self):
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)
        self.assertTrue("Ibadan-001", self.rev.place_id)
        self.assertTrue("123-879-098", self.rev.user_id)
        self.assertTrue("AirBnB", self.rev.text)

    def test_attributes_are_strings(self):
        self.assertEqual(type(self.rev.text), str)
        self.assertEqual(type(self.rev.place_id), str)
        self.assertEqual(type(self.rev.user_id), str)

    def test_save(self):
        self.rev.age = 90
        self.rev.save()
        self.assertNotEqual(self.rev.created_at, self.rev.updated_at)
        self.assertTrue(90, self.rev.age)

    def test_to_dict(self):
        self.assertEqual('to_dict' in dir(self.rev), True)


if __name__ == "__main__":
    unittest.main()
