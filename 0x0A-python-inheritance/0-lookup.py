#!/usr/bin/python3
"""function that returns list of attributes and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of an object"""
    return (dir(obj))
