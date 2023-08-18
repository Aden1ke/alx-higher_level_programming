#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for j in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(j, a_dictionary[j]))
