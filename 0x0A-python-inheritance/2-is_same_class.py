#!/usr/bin/python3
"""Defines a class that checks."""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of the specified class; else False.
    """
    return type(obj) is a_class
