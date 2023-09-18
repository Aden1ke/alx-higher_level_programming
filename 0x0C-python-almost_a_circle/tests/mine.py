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
        self.assertEqual(rect2.id, 2)

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

class TestRectangle_height(unittest.TestCase):
    """ Test with string height (not an integer) or (must be > 0) """
    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "new", 5, 6, 42)

    def test_none_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None, 5, 6, 42)

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, 4.5, 5, 6, 42)

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True, 5, 6, 42)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [2, 3], 5, 6, 42)

    def test_tupile_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, (2, 3, 4), 5, 6, 42)

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, {2, 3, 4}, 5, 6, 42)

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, range(3), 5, 6, 42)

    def test_zero_height(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
             Rectangle(2, 0, 5, 6, 42)

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(4, -2, 5, 6, 42)


class TestRectangle_x(unittest.TestCase):
    """ Test with string x (not an integer) or (must be > 0) """
    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "new", 6, 42)

    def test_none_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, None, 6, 42)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, 5.4, 6, 42)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, True, 6, 42)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, [2, 3], 6, 42)

    def test_tupile_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, (2, 3, 4), 6, 42)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, {2, 3, 4}, 6, 42)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, range(3), 6, 42)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -5, 6, 42)


class TestRectangle_y(unittest.TestCase):
    """ Test with string width (not an integer) or (must be >= 0) """
    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, "new", 42)

    def test_none_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, None, 42)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, 6.5, 42)

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, True, 42)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, [2, 3], 42)

    def test_tupile_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, (2, 3, 4), 42)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, {2, 3, 4}, 42)

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 5, range(3), 42)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 5, -6, 42)


class TestRectangle_order_of_error(unittest.TestCase):
    """Unittests for testing Rectangle order of error attribute."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", "height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("wifth", 2, "x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 2, 3, " y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height", "x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "height", 2, "y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 2, -4, -3)


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing the area of rectangle"""
    def test_area(self):
        rect = Rectangle(10, 5, 0, 0, 0)
        self.assertEqual(rect.area(), 50)


    def test_area_large(self):
        rect = Rectangle(5000000000000000, 10000000000000000, 2, 4, 1)
        self.assertEqual(rect.area(), 50000000000000000000000000000000)

    def test_area_changed_attributes(self):
        rect = Rectangle(2, 5, 5, 6, 1)
        rect.width = 2
        rect.height = 4
        self.assertEqual(rect.area(), 8)

if __name__ == "__main__":
    unittest.main()
