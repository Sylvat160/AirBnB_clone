#!/usr/bin/python3
"""
Unittest for BaseModel class
"""


import unittest
import sys
import os



from models.base_model import BaseModel
from datetime import datetime
import uuid


class BaseModelTest(unittest.TestCase):
    """
    Test cases for BaseModel class
    """

    def test_attr_class(self):
        """ checks if the classes use to generate attribute"""
        base = BaseModel()
        base2 = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertNotEqual(base.id, base2.id)

    def test_str(self):
        """
        Testing __str__ method
        """
        base = BaseModel()
        base_str = base.__str__()
        self.assertEqual(base_str,
                         f"[{type(base).__name__}] \
                         ({base.id}) {base.__dict__}")
