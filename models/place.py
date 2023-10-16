#!/usr/bin/python3
"""Creating a class Place which inherit BaseModel"""

from models.base_model import BaseModel
import json


class Place(BaseModel):
    """class City"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
