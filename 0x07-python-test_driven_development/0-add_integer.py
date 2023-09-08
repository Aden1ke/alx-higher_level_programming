#!/usr/bin/python3
""" This function adds only integers or float"""


def add_integer(a, b=98):
    """
    Add two integers or floats.
    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.
    Returns:
        int: The addition of a and b.
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return (a + b)
