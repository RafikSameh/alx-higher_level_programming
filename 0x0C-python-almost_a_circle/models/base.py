#!/usr/bin/python3
"""derive a base class"""


class Base:
    """represent a base class"""
    __nb_objects = 0

    def __int__(self, id=None):
        """class initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
