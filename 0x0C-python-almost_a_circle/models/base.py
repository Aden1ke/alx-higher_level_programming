#!/usr/bin/python3
"""Defines a base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            json_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(json_list)
            file.write(json_str)

    @classmethod
    def from_json_string(cls, json_string):
        """Return a list of instances from a JSON string."""
        if json_string is None or json_string == "":
            return []
        json_list = json.loads(json_string)
        instances = [cls.create(**attrs) for attrs in json_list]
        return instances

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with given attributes."""
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        elif cls.__name__ == "Square":
            instance = cls(1)
        instance.update(**dictionary)
        return instance
