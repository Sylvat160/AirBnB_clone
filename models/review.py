#!/usr/bin/python3
"""
Defines the state model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel
    """
    user_id = ""
    place_id = ""
    text = ""
