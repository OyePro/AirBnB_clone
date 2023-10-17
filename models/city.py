#!/usr/bin/python3
"""Creating a class City which inherit BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """class City"""

    state_id = ""
    name = ""
