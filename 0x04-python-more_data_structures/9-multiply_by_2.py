#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new = {}
        for k, v in a_dictionary.items():
            new[k] = v*2
    return new
