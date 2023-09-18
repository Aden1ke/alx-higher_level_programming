#!/usr/bin/python3
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle

class RectangleTests(unittest.TestCase):
    """Tests for Rectangle class."""
    def setUp(self):
        self.rect = Rectangle(15, 20)
    def test_width(self):
        """Testing width"""
        self.assertEqual(self.rect.width, 15)
    def test_height(self):
        """Testing height"""
        self.assertEqual(self.rect.height, 20)
    def test_x_val(self):
        """testing the x value"""
        self.rect.x = 0
        self.assertEqual(self.rect.x, 0)
    def test_y_val(self):
        """testing the x value"""
        self.rect.y = 0
        self.assertEqual(self.rect.y, 0)
    def test_x_neg(self):
        """testing assigning neg to x"""
        with self.assertRaises(ValueError):
            self.rect.x = -1
    def test_y_neg(self):
        """testing assigning neg to y"""
        with self.assertRaises(ValueError):
            self.rect.y = -1
    def test_width_zero(self):
        """testing assigning 0 to width"""
        with self.assertRaises(ValueError):
            self.rect.width = 0
    def test_height_zero(self):
        """testing assigning 0 to height"""
        with self.assertRaises(ValueError):
            self.rect.height = 0
    def test_string_assign_width(self):
        """test assigning string to width"""
        with self.assertRaises(TypeError):
            self.rect.width = "4"
    def test_string_assign_height(self):
        """test assigning string to height"""
        with self.assertRaises(TypeError):
            self.rect.height = "4"
    def test_bool_assign_width(self):
        """test assigning bool to width"""
        with self.assertRaises(TypeError):
            self.rect.width = True
    def test_bool_assign_height(self):
        """test assigning bool to height"""
        with self.assertRaises(TypeError):
            self.rect.height = True
    def test_none_assign_width(self):
        """test assigning None to width"""
        with self.assertRaises(TypeError):
            self.rect.width = None
    def test_none_assign_height(self):
        """test assigning None to height"""
        with self.assertRaises(TypeError):
            self.rect.height = None
    def test_float_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.rect.width = 7.8
    def test_float_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.rect.height = 7.8
    def test_list_assign_width(self):
        """testing assigning float value to width"""
        with self.assertRaises(TypeError):
            self.rect.width = [8, 9]
    def test_list_assign_height(self):
        """testing assigning float value to height"""
        with self.assertRaises(TypeError):
            self.rect.height = [8, 9]
    def test_string_assign_x(self):
        """test assigning string to x"""
        with self.assertRaises(TypeError):
            self.rect.x = "4"
    def test_string_assign_y(self):
        """test assigning string to y"""
        with self.assertRaises(TypeError):
            self.rect.y = "4"
    def test_bool_assign_x(self):
        """test assigning bool to x"""
        with self.assertRaises(TypeError):
            self.rect.x = True
    def test_bool_assign_y(self):
        """test assigning bool to y"""
        with self.assertRaises(TypeError):
            self.rect.y = True
    def test_none_assign_x(self):
        """test assigning None to x"""
        with self.assertRaises(TypeError):
            self.rect.x = None
    def test_none_assign_y(self):
        """test assigning None to y"""
        with self.assertRaises(TypeError):
            self.rect.y = None
    def test_float_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.rect.x = 7.8
    def test_float_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.rect.y = 7.8
    def test_list_assign_x(self):
        """testing assigning float value to x"""
        with self.assertRaises(TypeError):
            self.rect.x = [8, 9]
    def test_list_assign_y(self):
        """testing assigning float value to y"""
        with self.assertRaises(TypeError):
            self.rect.y = [8, 9]
    def test_id(self):
        """test checking id"""
        r = Rectangle(1, 2, 3, 4, 27)
        self.assertEqual(r.id, 27)
    def test_area(self):
        """testing area"""
        self.assertEqual(self.rect.area(), self.rect.height * self.rect.width)
    def test_normal_update(self):
        """normal testing of the update function"""
        self.rect.update(12, 67, 22, 1, 9)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.width, 67)
        self.assertEqual(self.rect.height, 22)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 9)
    def tearDown(self):
        del self.rect
