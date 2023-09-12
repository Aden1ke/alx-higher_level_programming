#!/usr/bin/python3
"""Writes an object to a text file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using a JSON."""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
