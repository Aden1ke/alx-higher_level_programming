#!/usr/bin/python3
""" This function prints name of a person"""


def print_square(size):
    """
    Print the function that prints a square.

    Args:
        size: the amount of # to print

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
