#!/usr/bin/python3
class Base:
    """
    This class will be the base of all other classes in this project
    __nb_objects is used to keep track of the num of instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.
        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
