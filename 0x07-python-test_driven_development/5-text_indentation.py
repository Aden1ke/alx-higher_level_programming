#!/usr/bin/python3
""" This function prints name of a person"""


def text_indentation(text):
    """
    Print the full text.

    Args:
        text (str): string to print.

    Raises:
        TypeError: text must be a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        if char in ['.', '?', ':']:
            print("\n\n")
        else:
            print(char, end='')
