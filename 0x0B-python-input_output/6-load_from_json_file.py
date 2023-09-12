#!/usr/bin/python3
"""create an object to a text file."""
import json


def load_from_json_file(filename):
    """create an object to a text file using a JSON."""
    with open(filename, 'r') as file:
        json.load(file)
