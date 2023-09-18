#!/usr/bin/python3
'''
    Class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    """" Class Rectangle inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Base.
        Args:
            width(int): width of rectangle
            height(int): height of rectangle
            x(int): position of rectangle
            y(int): position of rectangle
            id (int): The identity of the new Base.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # setters and getters for different attributes
    @property
    def width(self):
        """ Returning private attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting private attribute"""
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """ Returning private attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting private attribute"""
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ Returning private attribute """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting private attribute"""
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """ Returning private attribute """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting private attribute"""
        self.validate("y", value)
        self.__y = value

    # end

    # area of the rectangle
    def area(self):
        """ Return area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ print the rectangle with character #"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args, **kwargs):
        """Updates the arguments in the class"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def validate(self, attr_name, value):
        if not isinstance(value, int):
            raise TypeError(f"{attr_name} must be an integer")
        if attr_name == 'x' or attr_name == 'y':
            if value < 0:
                raise ValueError(f"{attr_name} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attr_name} must be > 0")

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle."""
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """update string printof the Rectangle."""
        return (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}/{self.height}"
                )
