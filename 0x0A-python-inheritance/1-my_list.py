#!/usr/bin/python3
"""This module inherits from the list class created"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
