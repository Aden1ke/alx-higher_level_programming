#!/usr/bin/python3
"""Defines an inherited class that checks."""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    from the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a subclass of the class;
        else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
