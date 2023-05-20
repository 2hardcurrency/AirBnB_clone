#!/usr/bin/python3
"""Modules containing the class f Amenity"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Class of Review"""

    place_id = ""
    user_id = ""
    text = ""
