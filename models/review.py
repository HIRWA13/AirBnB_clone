#!/usr/bin/python3
"""This module creates a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """This class is for managing review objects"""

    place_id = ""
    user_id = ""
    text = ""
