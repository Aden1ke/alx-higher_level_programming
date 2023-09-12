#!/usr/bin/python3
""" append a text file and count number of text"""


def append_write(filename="", text=""):
    """ function that append to a text file """
    with open(filename, 'a', encoding='utf-8') as file:
        count = file.write(text)
    return count
