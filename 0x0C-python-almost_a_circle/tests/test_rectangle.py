#!/usr/bin/python3
"""this modules are test for models/rectangle.py"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_validation(unittest.TestCase):
    def test_width_height_assignment(self):
        """Test if width and height are assigned correctly"""
        rect = Rectangle(2, 4)
        self.assertEqual(rect.width, 2)
        self.assertEqual(rect.height, 4)

    def test_x_y_assignment(self):
        """Test if x and y are assigned correctly"""
        rect = Rectangle(2, 4, 5, 6)
        self.assertEqual(rect.x, 5)
        self.assertEqual(rect.y, 6)

    def test_id_assignment(self):
        """Test if id is assigned correctly"""
        rect1 = Rectangle(2, 4, 5, 6, 42)
        self.assertEqual(rect1.id, 42)
        rect2 = Rectangle(2, 4, 5, 6)
        self.assertEqual(rect2.id, 1)

class TestRectangle_width(unittest.TestCase):
    """ Test with string width (not an integer) or (must be > 0) """
    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("new", 4, 5, 6, 42)

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 4, 5, 6, 42)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(3.5, 4, 5, 6, 42)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4, 5, 6, 42)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([2, 3], 4, 5, 6, 42)

    def test_tupile_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((2, 3, 4), 4, 5, 6, 42)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({2, 3, 4}, 4, 5, 6, 42)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 4, 5, 6, 42)

    def test_zero_width(self):
         with self.assertRaisesRegex(ValueError, "width must be > 0"):
             Rectangle(0, 4, 5, 6, 42)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4, 5, 6, 42)


if __name__ == "__main__":
    unittest.main()
