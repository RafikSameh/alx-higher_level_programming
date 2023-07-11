#!/usr/bin/python3
"""Define a class checker"""


def is_same_class(obj, a_class):
    """check the type of the object"""
    if a_class == type(obj):
        return True
    else:
        return False
