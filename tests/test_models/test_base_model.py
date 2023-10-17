#!/usr/bin/python3
"""
Unittest for class BaseModel
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Run with `python3 -m unittest -v tests/test_models/test_base_model.py`
    """
    myModel = BaseModel()

    def test_if_doc(self):
        self.assertIsNotNone(self.myModel.__doc__)
        self.assertIsNotNone(self.myModel.save.__doc__)
        self.assertIsNotNone(self.myModel.to_dict.__doc__)

    def test_base_model(self):
        self.myModel.name = "AirBnb"
        self.myModel.propert = "Project"
        self.myModel.save()
        to_json = self.myModel.to_dict()

        self.assertEqual(self.myModel.name, to_json["name"])
        self.assertEqual(self.myModel.propert, to_json["propert"])
        self.assertEqual("BaseModel", to_json["__class__"])
        self.assertEqual(self.myModel.id, to_json["id"])

    def test_attributes(self):
        self.assertTrue(hasattr(self.myModel, "__init__"))
        self.assertTrue(hasattr(self.myModel, "save"))
        self.assertTrue(hasattr(self.myModel, "to_dict"))

    def test_init(self):
        self.assertTrue(isinstance(self.myModel, BaseModel))

    def test_save(self):
        self.myModel.name = "AirBnb"
        self.myModel.propert = "Project"
        self.myModel.save()
        self.assertNotEqual(self.myModel.created_at, self.myModel.updated_at)
        self.assertEqual(self.myModel.name, "AirBnb")
        self.assertEqual(self.myModel.propert, "Project")

    def test_to_dict(self):
        self.myModel.name = "AirBnb"
        self.myModel.propert = "Project"
        self.myModel.save()
        to_json = self.myModel.to_dict()
        self.assertEqual(self.myModel.__class__.__name__, 'BaseModel')
        self.assertIsInstance(to_json['created_at'], str)
        self.assertIsInstance(to_json['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
