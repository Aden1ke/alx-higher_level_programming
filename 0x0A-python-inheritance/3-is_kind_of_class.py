#!/usr/bin/python3
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the class or its subclasses;
        else False.
    """
    return isinstance(obj, a_class)
