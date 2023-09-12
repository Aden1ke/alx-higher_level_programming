#!/usr/bin/python3
"""Converts an object to its JSON representati
on as a string."""
import json


def to_json_string(my_obj):
    """function that Converts an object to its JSON string."""
    return json.dumps(my_obj)
