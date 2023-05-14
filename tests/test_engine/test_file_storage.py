#!/usr/bin/python3
"""
Test for FileStorage
"""


import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class FileStorageTest(unittest.TestCase):

    def test_a(self):
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)

    def test_b(self):
        storage = FileStorage()
        base = BaseModel()
        storage.new(base)
        key = type(base).__name__ + '.' + base.id
        self.assertEqual(storage.all()[key], base)

    def test_reload(self):
        base1 = BaseModel({id: 8})
        base1.save()
        storage.save()
        self.assertEqual(storage.reload(), None)

    def test_private_attr(self):
        base = BaseModel()
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_path = storage.file_path
        with self.assertRaises(AttributeError):
            file_path = storage.__file_path
        with self.assertRaises(AttributeError):
            file_path = storage.objects
        with self.assertRaises(AttributeError):
            file_path = storage.__objects
