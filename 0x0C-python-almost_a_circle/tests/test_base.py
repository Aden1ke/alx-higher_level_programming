#!/usr/bin/python3
""" unittest for the base class and id"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    def test_assign_id(self):
        """Test if id is assigned correctly when provided"""
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_assign_empty_id(self):
        """Test if id is assigned correctly when it is not provided"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_logic(self):
        """Test if id logic is correct when it is not provided"""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, obj2.id - 1)

    if __name__ == "__main__":
        unittest.main()
