#!/usr/bin/python3
""" Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """" Class Square inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    # setters and getters for size
    @property
    def size(self):
        """ Returning private attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Setting private attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the arguments in the class"""
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the Square."""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }

    def __str__(self):
        """update string of the Square."""
        return (
                f"[Square] ({self.id}) "
                f"{self.x}/{self.y} - "
                f"{self.width}"
                )
