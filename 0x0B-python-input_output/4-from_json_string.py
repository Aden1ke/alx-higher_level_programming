#!/usr/bin/python3
"""Parses a JSON string."""
import json


def from_json_string(my_str):
    """Parses a JSON string and returns the corresponding Python."""
    return json.loads(my_str)
