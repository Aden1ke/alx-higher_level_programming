#!/usr/bin/python3
""" write a text file and count number of text"""


def write_file(filename="", text=""):
    """ function that write to a text file """
    with open(filename, 'w', encoding='utf-8') as file:
        count = file.write(text)
    return count
