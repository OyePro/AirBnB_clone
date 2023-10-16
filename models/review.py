#!/usr/bin/python3
"""Creating a class Review which inherit BaseModel"""

from models.base_model import BaseModel
import json


class Review(BaseModel):
    """class Review"""

    place_id = ""
    user_id = ""
    text = ""
