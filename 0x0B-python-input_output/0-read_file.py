#!/usr/bin/python3
""" Reads a text file and print contents"""


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end="")
