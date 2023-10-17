#!/usr/bin/python3
"""Creating a class User that inherits BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """class User which inherits BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
